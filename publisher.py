import pika


url_rabbitmq = 'amqps://puakpkye:EhJWLE2emj-rZ9P6x1u7WQAajpIu2_lP@jackal.rmq.cloudamqp.com/puakpkye'
body = 'Teste'
fila = 'Thais'

params = pika.URLParameters(url_rabbitmq)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.basic_publish(exchange=fila,
                      routing_key='',
                      body=body)

connection.close()

print("Direcionado:", body, "para a fila:", fila)
