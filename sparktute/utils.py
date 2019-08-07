""":mod:`sparktute.utils`

"""
import pyspark


def simple_rdd(spark) -> pyspark.RDD:
    """Create a simple Spark RDD.

    """
    return spark.sparkContext.parallelize(['test1', 'test2', 'test3'])
