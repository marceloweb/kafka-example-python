from kafka import KafkaConsumer
import configs

def consumer():
   conf = configs.load('configs/kafka/kafka.yml')
   message = 'test'
   consumer = KafkaConsumer(conf['consumer']['topic'], group_id=conf['consumer']['group_id'], bootstrap_servers=conf['consumer']['host'])
   for msg in consumer:
      print (msg)
