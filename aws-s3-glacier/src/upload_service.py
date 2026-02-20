from config import get_s3_client

def upload_glacier(file_path, bucket, object_name):
    s3 = get_s3_client()

    s3.upload_file(
        file_path,
        bucket,
        object_name,
        ExtraArgs={"StorageClass": "GLACIER"}
    )

    print("Arquivo enviado para Glacier com sucesso.")
