from kafka import KafkaProducer
import json
from sensor_utils import get_sensor_data
from kafka_utils import build_json_producer

producer =build_json_producer(["server number"]) #•exemple 127.0.0.1

data = {
    'houses': [
            get_sensor_data(), 
            get_sensor_data()
    ]
}

producer.send("house_features", data)
producer.flush()