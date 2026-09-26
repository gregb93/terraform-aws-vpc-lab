# AWS Multi-Tier Infrastructure with Terraform

## Project Overview

This project demonstrates the deployment of a secure AWS cloud infrastructure using Terraform.

The environment includes public and private networking, EC2 compute resources, IAM roles, AWS Systems Manager (SSM), a private Amazon RDS MySQL database, AWS Secrets Manager, and Python automation.

The infrastructure was built incrementally using Infrastructure as Code (IaC) and version controlled with Git and GitHub.

## Architecture

The environment includes:

- Custom AWS VPC
- Public and private subnets
- Internet Gateway
- NAT Gateway
- Public and private route tables
- Amazon EC2 instances
- Security groups
- IAM role and instance profile
- AWS Systems Manager Session Manager
- Amazon RDS MySQL in private networking
- AWS Secrets Manager for database credentials
- Python automation using Boto3 and PyMySQL
## Security Design

This project follows several AWS security best practices:

- The RDS MySQL database is deployed in private subnets and is not publicly accessible.
- The private EC2 instance is managed through AWS Systems Manager Session Manager instead of exposing SSH to the internet.
- IAM roles provide AWS permissions to EC2 without storing AWS access keys on the instance.
- Database credentials are stored in AWS Secrets Manager instead of being hard-coded in the Python application.
- Security groups restrict communication between resources.
- The private EC2 instance can communicate with RDS over MySQL port 3306.
- A NAT Gateway provides outbound internet access for resources in private subnets without allowing unsolicited inbound internet traffic.

## Python RDS Automation

A Python script connects securely to the private RDS MySQL database.

The script:

1. Retrieves database credentials from AWS Secrets Manager using Boto3.
2. Reads deployment-specific configuration from environment variables.
3. Connects to the private RDS endpoint using PyMySQL.
4. Queries the `server_inventory` table.
5. Displays the inventory records.
6. Closes the database connection.

Sensitive credentials and deployment-specific endpoints are not stored directly in the Python source code.
