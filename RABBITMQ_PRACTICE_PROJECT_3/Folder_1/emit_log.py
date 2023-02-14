import pika

#Connection Establishment
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaring the Queue
#channel.queue_declare('project3_queue', durable=True)
result = channel.queue_declare(queue='', exclusive=True)

# Declaring the Excahnge
channel.exchange_declare('logs', exchange_type='fanout')

message = "Hey Bro....!!"

channel.basic_publish(
    exchange='logs',
    #routing_key='project3_queue',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
      delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
      )
  )       


print(" [x] sent %r" % message)

connection.close()
