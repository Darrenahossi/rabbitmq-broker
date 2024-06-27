import pika

def producer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    while True:
        message = input("Enter message to send: ")
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print(f" [x] Sent '{message}'")

    connection.close()

if __name__ == "__main__":
    producer()
