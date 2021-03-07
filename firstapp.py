from pyspark import SparkContext
import pyspark
print(pyspark.__version__)
import random

NUM_SAMPLES = 1000000000
sc = SparkContext("spark://spark:7077", "test")

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))