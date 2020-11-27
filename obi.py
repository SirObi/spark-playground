from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('test').setMaster('local[4]')
sc = SparkContext(conf=conf)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
