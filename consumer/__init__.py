from kafka import KafkaConsumer
import configs

def configuration():
   file = configs.load('configs/kafka/kafka.yml')
   conf = {
         'bootstrap.servers': str(file['consumer']['host']),
         'group.id': "%s-consumer" % file['consumer']['group_id'],
         'session.timeout.ms': 6000,
         'default.topic.configs': {'auto.offset.reset': 'smallest'},
         'security.protocol': 'SASL_SSL',
         'sasl.mechanisms': 'SCRAM-SHA-256',
         'sasl.username': file['consumer']['username'],
         'sasl.password': file['consumer']['password'] 
   }

def consumer():
   conf = configs.load('configs/kafka/kafka.yml')
   message = 'test'
   consumer = KafkaConsumer(conf['consumer']['topic'], group_id=conf['consumer']['group_id'], bootstrap_servers=str(conf['consumer']['host']))
   for msg in consumer:
      print (msg)
