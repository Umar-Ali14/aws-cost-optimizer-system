import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

BUCKET_NAME = "cost-optimizer-project-bucket"

def lambda_handler(event, context):

    # CPU value coming from test event or CloudWatch later
    cpu = event.get("cpu", 0)
    instance_id = event.get("instance_id", "test-instance")

    # RULE ENGINE (your logic)
    if cpu < 5:
        status = "IDLE - WASTING COST 💸"
        action = "STOP or ALERT"
    elif cpu < 70:
        status = "NORMAL - OK ✔"
        action = "NO ACTION"
    else:
        status = "HIGH LOAD - SCALE REQUIRED 🔥"
        action = "SCALE UP"

    # create log record
    log_data = {
        "instance_id": instance_id,
        "cpu": cpu,
        "status": status,
        "action": action,
        "timestamp": str(datetime.now())
    }

    # save to S3 (cost optimization history)
    file_name = f"logs/{instance_id}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"

    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(log_data)
        )
    except Exception as e:
        return {
            "error": str(e),
            "message": "S3 write failed (check permissions)"
        }

    return {
        "message": "Execution successful",
        "data": log_data
    }
