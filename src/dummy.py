"arn:aws:sns:us-east-1:082176615813:Platts-Data-Engineering"
import boto3


sns = boto3.client('sns')
# Publish a simple message to the specified SNS topic
response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:587764000924:vish-sns-xplr',
    Message='Requested for the resources. \nYou can verify the details here: https://www.google.com',
    Subject='Data Platform - Resource requested - petchem-analytics'
)

# Print out the response
print(response)