import json
from src.sqs_client import get_sqs_client
from src.config import SQS_QUEUE_URL

def send_message(message_body):
    sqs = get_sqs_client()

    response = sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=json.dumps(message_body)
    )

    return response
