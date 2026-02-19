import boto3

def get_s3_client():
    """
    Cria cliente S3 usando IAM Role automaticamente.
    Funciona em EC2 ou Lambda sem precisar de Access Key.
    """
    return boto3.client("s3")
