from kafka import KafkaConsumer

def consumer():
   consumer = KafkaConsumer('NOVA_VENDA', group_id='ECOMMERCE', bootstrap_servers='localhost:9092')
   for msg in consumer:
      print (msg)
