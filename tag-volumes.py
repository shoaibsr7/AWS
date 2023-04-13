import boto3

# Connect to EC2 using boto3
client = boto3.client('ec2')

# Define the volume ID
volume_id = 'vol-xxxxxxxx'

# Get the instance ID associated with the given volume ID
response = client.describe_volumes(VolumeIds=[volume_id])
instance_id = response['Volumes'][0]['Attachments'][0]['InstanceId']

# Get the tags associated with the instance ID
response = client.describe_instances(InstanceIds=[instance_id])
tags = response['Reservations'][0]['Instances'][0]['Tags']

# Create tag list from instance tags
tag_list = [{'Key': tag['Key'], 'Value': tag['Value']} for tag in tags]

# Print the tags that will be applied to the volume
print(f"Tags for instance {instance_id}: {tags}")

# Apply the tags to the volume
client.create_tags(Resources=[volume_id], Tags=tag_list)

# Print a message indicating that the tags were applied successfully
print(f"Volume {volume_id} tagged with tags from instance {instance_id}")
