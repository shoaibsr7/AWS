# AWS Tagging Scripts
This repository contains Python scripts for tagging AWS resources using the Boto3 library. The scripts demonstrate how to tag EC2 instances, EBS volumes, and snapshots.

# Requirements
1. Python 3.x
2. Boto3 library
3. AWS CLI

# EC2 Instance Tagging
The `ec2_tagging.py` script demonstrates how to tag an EC2 instance with the same tags as its attached EBS volumes. The script uses the Boto3 library to connect to AWS and retrieve the necessary information. Once the tags are obtained, the script applies them to the instance using the `create_tags` method.

# Steps to Run the Script
1. Open `ec2_tagging.py` in a text editor.
2. Replace `INSTANCE_ID` with the instance ID you want to tag.
3. Save the file.
4. Open a terminal window and navigate to the directory containing `ec2_tagging.py`.
5. Run the command python `ec2_tagging.py`.

# EBS Volume Tagging
The `ebs_volume_tagging.py` script demonstrates how to tag an EBS volume with the same tags as its attached EC2 instance. The script uses the Boto3 library to connect to AWS and retrieve the necessary information. Once the tags are obtained, the script applies them to the volume using the `create_tags` method.

# Steps to Run the Script
1. Open `ebs_volume_tagging.py` in a text editor.
2. Replace `VOLUME_ID` with the volume ID you want to tag.
3. Save the file.
4. Open a terminal window and navigate to the directory containing `ebs_volume_tagging.py`.
5. Run the command python `ebs_volume_tagging.py`.

# EBS Snapshot Tagging
The `ebs_snapshot_tagging.py` script demonstrates how to tag EBS snapshots with the same tags as their associated EC2 instance. The script uses the Boto3 library to connect to AWS and retrieve the necessary information. Once the tags are obtained, the script applies them to the snapshots using the `create_tags` method.

# Steps to Run the Script
1. Open `ebs_snapshot_tagging.py` in a text editor.
2. Replace `VOLUME_ID` with the volume ID you want to tag.
3Save the file.
4. Open a terminal window and navigate to the directory containing `ebs_snapshot_tagging.py`.
5. Run the command python `ebs_snapshot_tagging.py`.

Note: Before running any of these scripts, make sure you have the necessary permissions and credentials to access the AWS resources you want to tag.