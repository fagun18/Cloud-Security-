import boto3

# Connect to the EC2 service
ec2 = boto3.client('ec2')

# Define the IP addresses that are allowed to access the security group
ip_addresses = ['111.111.111.111/32', '222.222.222.222/32']

# Create the security group
response = ec2.create_security_group(
    GroupName='my-security-group',
    Description='Security group for my application'
)

# Get the security group ID
security_group_id = response['GroupId']

# Add the IP addresses to the security group
for ip_address in ip_addresses:
    ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpProtocol='tcp',
        FromPort=80,
        ToPort=80,
        CidrIp=ip_address
    )

print("Security group created successfully")
