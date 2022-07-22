import json 
from kafka import KafkaConsumer
from model_utils import load_model, predict
from kafka_utils import build_json_producer

topic_name = "house_features" 

consumer = KafkaConsumer(
    topic_name, 
    bootstrap_servers=["numéro serveur"], #exemple 127.0.0.1
    value_deserializer= lambda byte_data: json.loads(byte_data.decode('utf-8')) 
)

model = load_model()
producer = build_json_producer(["numéro serveur"])

house_price_topic_name = "house_price_prediction"
for message in consumer: 
    
    result = predict(model, message.value['houses'])
    producer.send(house_price_topic_name, {'house_prices': result.tolist()})
    producer.flush()
