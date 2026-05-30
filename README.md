# aws-cost-optimization-system
Event-driven AWS cost optimization system using EC2, CloudWatch, Lambda, and S3 to detect and log idle instances automatically.
#  AWS Cost Optimization System (Event-Driven Serverless Architecture)

## 📌 Project Overview

The AWS Cost Optimization System is a fully serverless, event-driven cloud automation solution designed to detect underutilized EC2 instances and log optimization decisions in real time.

This system demonstrates how organizations can reduce cloud waste by automatically identifying idle compute resources and applying rule-based decision-making using AWS services.

---

## 🎯 Problem Statement

In real-world cloud environments, companies often face:

- Idle EC2 instances running without workload
- Increasing AWS bills due to unused compute resources
- Lack of automated monitoring and cost optimization
- Manual intervention required to detect waste

This project solves these issues using an automated AWS-based monitoring system.

---

## 💡 Solution Architecture

The system follows an event-driven architecture:


EC2 Instances → CloudWatch Metrics → CloudWatch Alarm → AWS Lambda → Amazon S3 (Logs)


---

## ☁️ AWS Services Used

### 1. Amazon EC2
 
- Hosts virtual servers for testing idle, normal, and high-load scenarios  
- Generates CPU utilization metrics used for monitoring  

---

### 2. Amazon CloudWatch 
- Monitors EC2 CPU utilization in real time  
- Creates alarms based on threshold rules  
- Triggers automation when conditions are met  

---

### 3. AWS Lambda
 
- Executes serverless Python code when CloudWatch alarm triggers  
- Implements rule engine logic for cost optimization  
- Processes CPU usage and determines instance status  

---

### 4. Amazon S3
 
- Stores JSON logs of optimization decisions  
- Maintains execution history for auditing and reporting  

---

## ⚙️ System Workflow

### Step 1: EC2 Monitoring
- EC2 instances generate CPU utilization metrics continuously

### Step 2: CloudWatch Evaluation
- CloudWatch monitors CPU usage every 5 minutes
- Metric: `CPUUtilization`

### Step 3: Alarm Condition
The alarm is triggered when:


CPUUtilization < 5%


This defines the instance as IDLE.

---

### Step 4: Lambda Execution
When alarm state becomes **IN ALARM**, AWS Lambda is triggered.

Lambda performs:

- Reads CPU value from event
- Applies rule-based logic:
  - CPU < 5% → IDLE
  - CPU 5–70% → NORMAL
  - CPU > 70% → HIGH LOAD
- Generates structured output (JSON)

---

### Step 5: S3 Logging
- Lambda stores results in Amazon S3 bucket
- Each execution creates a timestamped JSON file

{
  "instance_id": "ec2-idle-1",
  "cpu": 3,
  "status": "IDLE - WASTING COST 💸",
  "action": "STOP or ALERT",
  "timestamp": "2026-05-29 17:52:57"
}                                                                                                                            
  ---
  🚀 Key Learnings
Built event-driven serverless architecture on AWS
Learned real-time monitoring using CloudWatch
Implemented automation using AWS Lambda
Understood cloud cost optimization strategies (FinOps basics)
🏁 Conclusion

This project demonstrates a production-style AWS architecture for detecting and handling idle EC2 instances.
It simulates real-world cost optimization systems used in cloud engineering environments.
