from kafka import KafkaProducer
import random
from json import dumps
import configs

def producer():
   conf = configs.load('configs/kafka/kafka.yml')
   number = random.randint(100,1000)
   message = "TEST::::::: >> {} <<".format(number)
   bmessage = {'message' :message}

   producer = KafkaProducer(bootstrap_servers=conf['producer']['host'], 
                           value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))
   producer.send(conf['producer']['topic'], value=bmessage)
   producer.flush()

