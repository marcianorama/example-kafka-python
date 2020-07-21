import json
from kafka import KafkaConsumer
import re
import base64
from PIL import Image
import requests
from io import BytesIO


# topic = 'test-topic'
topic = 'streaming-ocr-request'
bootstrap_servers=['localhost:9092']
consumer_timeout=1000
group_id='test-topic-group'

consumer = KafkaConsumer(
    auto_offset_reset='earliest',
    consumer_timeout_ms=consumer_timeout,
    group_id=group_id,
    bootstrap_servers=bootstrap_servers,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )
# To consume latest messages and auto-commit offsets
consumer.subscribe(topic)

running =True
while(True):
    try:
        for message in consumer:
            print (
              "> consuming message from %s partition=%d with offset=%d and key=%s" % (
                message.topic, message.partition, message.offset, message.key
              )
            )
            if message is None:
                continue
            else:
                # print('Received message: {0}'.format(message.value))
                parsed_string = re.sub(r"[“|”|‛|’|‘|`|´|″|′|']", '"', str(message.value))
                # ex: text
                # json_data = json.loads(parsed_string)
                # print('url = ',json_data['url'])

                # ex: image
                json_read = json.loads(parsed_string)

                print('image link= ', json_read['image'])

                response = requests.get(json_read['image'])
                img = Image.open(BytesIO(response.content))
                # process img file
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()