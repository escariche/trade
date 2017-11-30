import threading
import os
from urllib2 import urlopen
from sys import argv

myIP = urlopen('http://ip.42.pl/raw').read()
# topic = argv[1]
topic = 'test000'

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def extract():
    os.system('/home/ec2-user/kafka/kafka_2.11-1.0.0/bin/kafka-console-consumer.sh --bootstrap-server '+ myIP  +':9092 --topic '+ topic +' --from-beginning > /home/ec2-user/kafka/kafka_2.11-1.0.0/test000.txt$

set_interval(extract, 1)
