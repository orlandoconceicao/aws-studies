import json
from src.sns_client import get_sns_client
from src.config import SNS_TOPIC_ARN

def publish_message(message_body):

    sns = get_sns_client()

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=json.dumps(message_body)
    )

    return response
