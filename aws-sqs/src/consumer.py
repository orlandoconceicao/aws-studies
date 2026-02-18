import json
from src.sqs_client import get_sqs_client
from src.config import SQS_QUEUE_URL

def receive_messages():
    sqs = get_sqs_client()

    response = sqs.receive_message(
        QueueUrl=SQS_QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )

    messages = response.get("Messages", [])

    for message in messages:
        body = json.loads(message["Body"])
        print("Mensagem recebida:", body)

        # deletar após processar
        sqs.delete_message(
            QueueUrl=SQS_QUEUE_URL,
            ReceiptHandle=message["ReceiptHandle"]
        )
