from config import get_s3_client

def restore_file(bucket, object_name):
    s3 = get_s3_client()

    s3.restore_object(
        Bucket=bucket,
        Key=object_name,
        RestoreRequest={
            "Days": 7,
            "GlacierJobParameters": {
                "Tier": "Standard"
            }
        }
    )

    print("Solicitação de restauração enviada.")
