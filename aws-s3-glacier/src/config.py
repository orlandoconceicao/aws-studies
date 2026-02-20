import boto3

def get_s3_client():
    """
    Usa IAM Role automaticamente (EC2 ou Lambda).
    """
    return boto3.client("s3")
