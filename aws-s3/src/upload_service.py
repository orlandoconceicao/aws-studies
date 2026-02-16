from src.s3_client import get_s3_client
from src.config import AWS_BUCKET_NAME

def upload_file(file_path, object_name):
    s3 = get_s3_client()

    s3.upload_file(
        file_path,
        AWS_BUCKET_NAME,
        object_name
    )

    return f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{object_name}"
