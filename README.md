COVID-19 Data Streaming con Apache Spark y Apache Kafka

Este proyecto procesa datos en tiempo real del COVID-19 en Colombia utilizando **Apache Spark Streaming** y **Apache Kafka**, con datos abiertos obtenidos desde [datos.gov.co](https://www.datos.gov.co/resource/gt2j-8ykr.csv).

---

## Objetivos

- Implementar una arquitectura de **procesamiento de datos en streaming**.  
- Integrar **Apache Kafka** como sistema de mensajería.  
- Analizar flujos de datos del COVID-19 con **Apache Spark**.  
- Visualizar resultados y métricas en tiempo real.

---

## Arquitectura

**Flujo general:**
1. **Kafka Producer** envía registros del dataset CSV.
2. **Kafka Broker** los almacena temporalmente en el tópico `covid19_topic`.
3. **Spark Streaming** consume los mensajes y realiza agregaciones (por departamento, estado, etc.).
4. Los resultados se visualizan en la consola o panel de dashboards.

---

## Estructura del Proyecto
covid19-spark-kafka/
├── data/gt2j-8ykr.csv
├── src/
│ ├── kafka_producer.py
│ └── spark_streaming.py
├── notebooks/covid_analysis.ipynb
├── docs/
│ ├── arquitectura.png
│ ├── flujo_datos.png
│ └── resultados.png
└── README.md

## Requisitos

Instalar dependencias:

```bash
pip install -r src/requirements.txt

