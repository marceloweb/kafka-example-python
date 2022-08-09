from kafka import KafkaProducer
import random
from json import dumps


def producer():
   number = random.randint(100,1000)
   message = "TEST::::::: >> {} <<".format(number)
   bmessage = {'message' :message}

   producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                           value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))
   producer.send('NOVA_VENDA', value=bmessage)
   producer.flush()

