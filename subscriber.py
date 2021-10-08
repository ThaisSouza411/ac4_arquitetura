import pika


def receiver_message(ch, method, properties, body):
    print("Recepcionou:", body)

url_rabbitmq = 'amqps://puakpkye:EhJWLE2emj-rZ9P6x1u7WQAajpIu2_lP@jackal.rmq.cloudamqp.com/puakpkye'
fila = 'Thais'
params = pika.URLParameters(url_rabbitmq)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_bind(exchange='Thais', queue=fila)
channel.basic_consume(on_message_callback=receiver_message, auto_ack=True, queue=fila)

print("Usando a fila:", fila)

channel.start_consuming()
