from src.repository import OrderRepository

if __name__ == "__main__":

    repo = OrderRepository()

    repo.create_order({
        "order_id": "123",
        "user": "orlando",
        "total": 150
    })

    print("Pedido criado!")

    response = repo.get_order("123")
    print(response.get("Item"))
