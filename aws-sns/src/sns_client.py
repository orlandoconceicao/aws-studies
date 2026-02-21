import boto3
from src.config import AWS_REGION

def get_sns_client():
    return boto3.client(
        "sns",
        region_name=AWS_REGION
    )
