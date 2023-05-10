from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import log, col
import string
import os
import math

# Create a SparkSession object
spark = SparkSession.builder.getOrCreate()

# Access the SparkContext
sc = spark.sparkContext


file_contents_rdd = sc.wholeTextFiles("./hw3Q1-files/*")

tokens_rdd = file_contents_rdd.map(lambda x: (os.path.basename(x[0]), x[1].lower().translate(str.maketrans("", "", string.punctuation)).split()))

term_frequency_rdd = tokens_rdd.flatMap(lambda x: [((x[0], token), 1) for token in x[1]]).reduceByKey(lambda x, y: x + y)

term_frequency_df = term_frequency_rdd.map(lambda x: (x[0][0], x[0][1], x[1])).toDF(["song_id", "token", "term frequency"])

document_frequency_rdd = tokens_rdd.flatMap(lambda x: [(token, x[0]) for token in x[1]]).distinct().map(lambda x: (x[0], 1)).reduceByKey(lambda x, y: x + y)

total_documents = file_contents_rdd.count()

inverse_document_frequency_rdd = document_frequency_rdd.map(lambda x: (x[0], math.log(total_documents / x[1])))

inverse_document_frequency_df = inverse_document_frequency_rdd.toDF(['token', 'inverse document frequency'])

tfidf_df = term_frequency_df.join(inverse_document_frequency_df, 'token')

idf_dict = dict(inverse_document_frequency_rdd.collect())

tfidf_rdd = term_frequency_rdd.map(lambda x: (x[0][0], x[0][1], x[1] * idf_dict[x[0][1]]))

tfidf_df = tfidf_rdd.toDF(["song_id", "token", "TF-IDF"])

result_df = tfidf_df.join(term_frequency_df, ["song_id", "token"]).join(inverse_document_frequency_df, 'token').orderBy(col('song_id').asc(), col('TF-IDF'))

result_df.select("song_id", "token", "term frequency", "inverse document frequency", "TF-IDF").show(100)
