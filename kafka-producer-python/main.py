from kafka import KafkaProducer
import random
import json

number = random.randint(1,100)
message = 'test: ' + str(number)
json_message = {'name':'abc', 'email':'abc@example.com'}

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(5):
    producer.send('NOVA_VENDA', message)
    producer.flush()