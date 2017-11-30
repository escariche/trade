from kafka import KafkaProducer
from kafka.errors import KafkaError

kafka = KafkaClient("18.217.106.184:9092")
consumer = SimpleConsumer(kafka, "my-group", argv[1])
consumer.max_buffer_size=0
consumer.seek(0,2)
for message in consumer:
 print("OFFSET: "+str(message[0])+"\t MSG: "+str(message[1][3]))
