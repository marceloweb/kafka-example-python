from kafka import KafkaProducer
import random
from json import dumps
import configs

def configuration():
   file = configs.load('configs/kafka/kafka.yml')
   conf = {
         'bootstrap.servers': file['consumer']['host'],
         'group.id': "%s-consumer" % file['consumer']['group_id'],
         'session.timeout.ms': 6000,
         'default.topic.configs': {'auto.offset.reset': 'smallest'},
         'security.protocol': 'SASL_SSL',
         'sasl.mechanisms': 'SCRAM-SHA-256',
         'sasl.username': file['consumer']['username'],
         'sasl.password': file['consumer']['password']
   }

def producer():
   number = random.randint(100,1000)
   message = "TEST::::::: >> {} <<".format(number)
   bmessage = {'message' :message}

   producer = KafkaProducer(bootstrap_servers=conf['producer']['host'], 
                           value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))
   producer.send(conf['producer']['topic'], value=bmessage)
   producer.flush()

