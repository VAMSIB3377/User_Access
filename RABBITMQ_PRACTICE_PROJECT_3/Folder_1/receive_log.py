import pika
#import time

#Connection Establishment
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaring the Exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    
    print(" [x] received %r" % body.decode())

    #time.sleep(body.count(b'.'))

    print(' [x] Done')

    ch.basic_ack(delivery_tag=method.delivery_tag)


print(' [*] Waiting for messages. To exit press CTRL+C')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue=queue_name, on_message_callback=callback)

channel.start_consuming()