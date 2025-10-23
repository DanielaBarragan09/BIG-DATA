# kafka_producer.py
# Autora: Alanis Daniela Barragán Urquiza
# Descripción: Casos de COVID-19 en Colombia

from kafka import KafkaProducer
import pandas as pd
import json
import time

# Cargar dataset público
df = pd.read_csv('data/gt2j-8ykr.csv')

# Seleccionar columnas relevantes
df = df[['fecha_reporte_web', 'departamento_nom', 'ciudad_municipio_nom', 'edad', 'sexo', 'estado']].dropna()

# Crear productor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Enviar datos a Kafka
for _, row in df.iterrows():
    message = {
        'fecha': row['fecha_reporte_web'],
        'departamento': row['departamento_nom'],
        'ciudad': row['ciudad_municipio_nom'],
        'edad': int(row['edad']),
        'sexo': row['sexo'],
        'estado': row['estado']
    }
    producer.send('covid19_topic', value=message)
    time.sleep(0.1)

print("Datos enviados exitosamente a Kafka.")
