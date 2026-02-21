from src.publisher import publish_message

if __name__ == "__main__":

    publish_message({
        "event": "order_created",
        "order_id": 123,
        "user": "orlando"
    })

    print("Evento publicado no SNS!")
