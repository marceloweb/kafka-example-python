from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(5):
    producer.send('NOVA_VENDA',b'0009-- Python')
    producer.flush()