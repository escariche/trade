from kafka import KafkaProducer
from kafka.errors import KafkaError

import sched, time
import random
import threading
import json
from datetime import datetime

from sys import argv

from urllib2 import urlopen

myIP = urlopen('http://ip.42.pl/raw').read()
producer = KafkaProducer(bootstrap_servers=[myIP+':9092'])
topic = argv[1]

def getBPM():
    sample = {}
    bpm = random.randint(60, 100)
    sample[str(datetime.now())] = bpm
    json_formated_sample = json.dumps(sample)
    return str(json_formated_sample).encode()

def publish(msg):
    producer.send(topic, msg)
    producer.flush()

#for publishing
def sendMsg(sc):
    print "Sending message..."
    # do your stuff
    publish(getBPM())
    s.enter(5, 1, sendMsg, (sc,))

s = sched.scheduler(time.time, time.sleep)
s.enter(5, 1, sendMsg, (s,))
s.run()
