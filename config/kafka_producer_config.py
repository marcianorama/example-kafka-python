from kafka import KafkaProducer
import json
import pickle

bootstrap_servers=['localhost:9092']
producer_timeout=2000

def producer():
    producer = KafkaProducer(
        acks=1,
        # acks='all',
        retries=5,
        # compression_type='lz4', #just use default compression: gzip
        request_timeout_ms=producer_timeout,
        bootstrap_servers=bootstrap_servers,
        key_serializer=str.encode,
        # value_serializer=lambda m: json.dumps(m).encode('utf-8')
        #config for image
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
        # value_serializer=lambda m: pickle.dumps(m)
    )
    return producer