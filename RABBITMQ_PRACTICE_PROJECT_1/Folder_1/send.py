import pika


# Connection Establishment
connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Queue Declaration
channel.queue_declare(queue='hello')

# Sending the message using a default exchange
channel.basic_publish(exchange='',
                      routing_key="hello",
                      body="Hello World!")

print("[x] sent 'Hello World!'")

# Closing the connection to make sure the network buffers were flushed
# and our message was actually delivered to RabbitMQ
connection.close()