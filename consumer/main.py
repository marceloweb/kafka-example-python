from kafka import KafkaConsumer

consumer = KafkaConsumer('NOVA_VENDA', group_id='ECOMMERCE', bootstrap_servers='localhost:9092')
for msg in consumer:
    print (msg)