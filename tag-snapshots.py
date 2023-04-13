import boto3

# Create EC2 client
client = boto3.client('ec2')

# Get list of snapshots for the given volume ID
volume_id = 'vol-xxxxxxxx'
response = client.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': [volume_id]}])
snapshots = response['Snapshots']

# Get the instance ID associated with the given volume ID
response = client.describe_volumes(VolumeIds=[volume_id])
instance_id = response['Volumes'][0]['Attachments'][0]['InstanceId']

# Get the tags associated with the instance ID
response = client.describe_instances(InstanceIds=[instance_id])
tags = response['Reservations'][0]['Instances'][0]['Tags']

# Create tag list from instance tags
tag_list = [{'Key': tag['Key'], 'Value': tag['Value']} for tag in tags]

# Print the tags that will be applied to the snapshots
print(f"Tags for instance {instance_id}: {tags}")

# Tag each snapshot with the same tags as the instance
for snapshot in snapshots:
    client.create_tags(Resources=[snapshot['SnapshotId']], Tags=tag_list)

# Print a message indicating how many snapshots were tagged for the volume.
print(f"{len(snapshots)} snapshots for volume {volume_id} tagged with instance {instance_id}")
