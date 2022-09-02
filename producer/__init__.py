from confluent_kafka import Producer
import random
import sys
from json import dumps
import configs
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer

def producer():
   file = configs.load('configs/kafka/kafka.yml')
   number = random.randint(100,1000)
   message = "TEST::::::: >> {} <<".format(number)
   bmessage = {'message' :message}

   conf = {
        'bootstrap.servers': "",
        'session.timeout.ms': 6000,
        'value.serializer': StringSerializer('utf_8'),
        'key.serializer': StringSerializer('utf_8'),
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
	    'sasl.mechanisms': 'SCRAM-SHA-256',
        'sasl.username': file['producer']['username'],
        'sasl.password': file['producer']['password']
    }

   p = SerializingProducer(conf)

   def delivery_callback(err, msg):
        if err:
            sys.stderr.write('%% Message failed delivery: %s\n' % err)
        else:
            sys.stderr.write('%% Message delivered to %s [%d]\n' %
                             (msg.topic(), msg.partition()))

   try:
      p.produce(file['producer']['topic'], key="name", value="Marcx")
   except BufferError as e:
            sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                             len(p))
   p.poll(0)

   sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
   p.flush()

