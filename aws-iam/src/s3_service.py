from config import get_s3_client

def listar_arquivos(bucket_name):
    s3 = get_s3_client()
    
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if "Contents" not in response:
        return []

    arquivos = [obj["Key"] for obj in response["Contents"]]
    return arquivos
