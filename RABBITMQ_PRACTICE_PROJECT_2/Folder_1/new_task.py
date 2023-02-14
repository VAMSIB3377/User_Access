import pika
import sys

# Connectio Establishment
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Queue Declaration
channel.queue_declare('task_queue', durable=True)


message = ' '.join(sys.argv[1:]) or "Hello Dude!"


channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                            delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                        )
                      )

print(" [x] sent %r "% message)


channel.close()