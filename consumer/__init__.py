from kafka import KafkaConsumer
import configs

def consumer():
   conf = configs.load('configs/kafka/kafka.yml') 
   consumer = KafkaConsumer('NOVA_VENDA', group_id='ECOMMERCE', bootstrap_servers='localhost:9092')
   for msg in consumer:
      print (msg)
