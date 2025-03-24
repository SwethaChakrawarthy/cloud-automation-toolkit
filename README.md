# ☁️ Cloud Automation Toolkit with Python & AWS

A modular Python-based toolkit that automates the provisioning of AWS resources including EC2 instances, S3 buckets, and IAM roles using Boto3.

---

## 🔧 Features

- 🚀 Launch Amazon EC2 instances
- 🗂️ Create and manage S3 buckets
- 🔐 Configure IAM roles and policies
- ♻️ Modular and reusable Python scripts
- ✅ Uses `.env` file for secure AWS credential handling
- 🔍 Follows best practices with Boto3 and IAM

---

## 📁 Project Structure


---

## ⚙️ Prerequisites

- Python 3.7+
- AWS account with IAM user credentials
- IAM user permissions: `AmazonEC2FullAccess`, `AmazonS3FullAccess`, `IAMFullAccess`
- Existing EC2 Key Pair in AWS

---

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/cloud-automation-toolkit.git
   cd cloud-automation-toolkit


python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1


