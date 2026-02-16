import json
from src.database import get_db_version

def lambda_handler(event, context):
    try:
        version = get_db_version()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Lambda funcionando",
                "db_version": version
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }