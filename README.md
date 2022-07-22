# Exemple d'utilisation d'un modèle de ML avec Kafka

## Script python

test_model.py : Tester notre modèle de machine learning
house_features_consumer.py : consumer + producer to send the message to kafka.
house_price_prediction_consumer.py : consumer qui récupère la valeurs prédites et l'insère dans la table.
producer_house_data.py : producer qui envoie les données récupérer via get sensor.

## Fonctions

db_utils.py : Fonctions pour se connecter à MySQL et insérer des données dans la base de données.
sensor_utils.py : Fonctions pour récupérer des données (de façon aléatoire)
model_utils.py : Fonctions pour charger le modèle et faire des prédictions
kafka_utils.py : Fonctions pour que le producer puisse récupérer un fichier json

## Modèle IA

regression.joblib : Modèle de machine learning


