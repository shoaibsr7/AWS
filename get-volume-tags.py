import boto3

# Connect to AWS using boto3
client = boto3.client('ec2')

# Get all the volumes in AWS
response = client.describe_volumes()

# Loop through the volumes
for volume in response['Volumes']:
    # If there is only one attachment for this volume, skip it
    vol = volume if len(volume['Attachments']) > 1 else 0
    if vol != 0 : print(vol)
    volume_id = volume['VolumeId']
    
    # If there is at least one EC2 instance attached to this volume, assign the instance ID of the first instance in the list to the instance_id variable
    if len(volume['Attachments']) > 0 : instance_id = volume['Attachments'][0]['InstanceId']
    
    # Get all the snapshots for the current volume
    snapshots = client.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': [volume_id]}])['Snapshots']
    
    # Get the tags of the instance
    instance_tags = client.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [instance_id]}])['Tags']
    
    # Create a dictionary with the instance tags
    instance_tags_dict = [{"Key": tag['Key'], "Value":tag['Value']} for tag in instance_tags]
    
    # Print the tags that will be applied to the snapshots
    print(f"Tags for instance {instance_id}: {instance_tags}")
    
    # Tag the snapshots with the instance tags
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        response = client.create_tags(Resources=[snapshot_id], Tags=instance_tags_dict)
    
    # Print a message indicating how many snapshots were tagged for the volume.
    print(f"{len(snapshots)} snapshots for volume {volume_id} tagged with instance {instance_id}")
