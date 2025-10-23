# spark_streaming.py
# Autora: Alanis Daniela Barragán Urquiza
# Descripción: Consume los mensajes de Kafka y los procesa con Apache Spark Streaming.

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, count
from pyspark.sql.types import StructType, StringType, IntegerType

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("COVID19-Spark-Kafka") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Definir esquema de los mensajes
schema = StructType() \
    .add("fecha", StringType()) \
    .add("departamento", StringType()) \
    .add("ciudad", StringType()) \
    .add("edad", IntegerType()) \
    .add("sexo", StringType()) \
    .add("estado", StringType())

# Leer flujo de datos desde Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "covid19_topic") \
    .load()

# Decodificar mensajes JSON
covid_data = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Ejemplo: Conteo de casos por departamento
result = covid_data.groupBy("departamento").agg(count("*").alias("total_casos"))

# Salida en consola
query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
