from upload_service import upload_glacier
from restore_service import restore_file

if __name__ == "__main__":
    bucket_name = "meu-bucket"
    
    # Upload
    upload_glacier("backup.zip", bucket_name, "backup.zip")
    
    # Restore
    # restore_file(bucket_name, "backup.zip")
