import pika
import time

# Connectio Establishment
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Queue Declaration
channel.queue_declare('task_queue', durable=True)


def callback(ch, method, properties, body):
    
    print(" [x] Received %r" % body.decode())

    time.sleep(body.count(b'.'))

    print(" [x] Done")

    #ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='task_queue',
                      #auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()