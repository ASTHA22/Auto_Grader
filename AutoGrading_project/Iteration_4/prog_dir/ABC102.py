#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, count, log
from pyspark.sql.types import FloatType
from pyspark.sql.functions import lower, regexp_replace, split, expr
from pyspark.sql.functions import *


# In[2]:


# Create a SparkSession
spark = SparkSession.builder.appName("TF-IDF").getOrCreate()


# In[3]:


# Split text into words and normalize them
df = spark.read.text("/Users/asthasingh/song_dataset/*") \
    .withColumn("song", regexp_replace(input_file_name(), ".*/", "")) \
    .withColumn("text", lower(expr("regexp_replace(value, '[^a-zA-Z\\s]+', '')"))) \
    .withColumn("token", split("text", "\\s+")) \
    .select("song", explode("token").alias("token"))




# In[5]:


# Compute the term frequency of each token in each document
tf = df.groupBy("token", "song") \
       .agg(expr("count(*)").alias("freq")) \
       .withColumn("tf", expr("freq / sum(freq) over (partition by song)"))


# In[6]:


# Compute the inverse document frequency of each token
# Compute the inverse document frequency of each token
idf = (
    df.groupBy("token", "song")
    .agg(count("*").alias("tf"))
    .groupBy("token")
    .agg(count("*").alias("df"))
    .withColumn("idf", log(lit(len(df.select("song").distinct().collect()))) - log(col("df")))
)


# In[7]:


# Compute the TF-IDF of each token in each document
tfidf = tf.join(idf, "token") \
          .withColumn("tf_idf", col("tf") * col("idf")) \
          .select("song", "token", "tf", "idf", "tf_idf")




# In[10]:


import sys
# Show all the rows in the tfidf dataframe
tfidf.show(n=2147483647)
