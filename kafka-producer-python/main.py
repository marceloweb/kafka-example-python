from kafka import KafkaProducer
import random
import json

number = random.randint(1,100)
message = "test: {}".format(number)
bmessage = bytes(message, 'utf-8')

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('NOVA_VENDA', bmessage)
producer.flush()