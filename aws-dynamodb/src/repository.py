from src.dynamodb_client import get_dynamodb_resource
from src.config import DYNAMODB_TABLE

class OrderRepository:

    def __init__(self):
        dynamodb = get_dynamodb_resource()
        self.table = dynamodb.Table(DYNAMODB_TABLE)

    def create_order(self, order_data):
        return self.table.put_item(Item=order_data)

    def get_order(self, order_id):
        return self.table.get_item(
            Key={"order_id": order_id}
        )

    def delete_order(self, order_id):
        return self.table.delete_item(
            Key={"order_id": order_id}
        )
