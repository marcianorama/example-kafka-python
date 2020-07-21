from flask import Flask, render_template, Response
from config.kafka_producer_config import producer
from util.message import *
from util.common_util import *
import json
import cv2
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

#Producer API
@app.route('/produce', methods=['GET'])
def get_produce():
    try:
        # topic = 'streaming-crawling-request'
        topic = 'streaming-ocr-request'

        # ex : text
        # text = open('message.json', 'r').read()
        # message = json.loads(text)

        # ex : image
        # with open("image.jpg", "rb") as image_file:
        #     file_image = base64.b64encode(image_file.read())

        # data["image"] = file_image.decode()
        data = {}
        data["image"] = "https://i.imgur.com/5rdD5wy.jpg"
        message = data

        producer().send(
            topic=topic,
            value=message,
            key=str(generate_uuid())
        ).add_callback(success).add_errback(error)

        # block until all async messages are sent
        producer().flush()
        response_message='Send Produce Topic Success'
    except Exception as e:
        print(e)
        response_message = 'Send Produce Topic Failed'
    return Response(response_message)