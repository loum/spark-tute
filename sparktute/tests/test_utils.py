""":mod:`sparktute.utils` unit test cases.

"""
import os
import pyspark.sql as ps

import sparktute.utils


def test_spark_session(spark_session):
    """Test Spark Session.
    """
    msg = 'Cannot source Spark Session'
    assert isinstance(spark_session, ps.session.SparkSession), msg


def test_simple(spark_session):
    """Test a simple RDD.
    """
    # Given a simple Spark RDD
    rdd = sparktute.utils.simple_rdd(spark_session)

    # when I query
    received = rdd.collect()

    # then I should receive a list of values
    assert received == ['test1', 'test2', 'test3'], 'Simple RDD failure'
