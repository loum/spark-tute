"""Global fixture arrangement at the `sparktute` package level.

"""
import os
import tempfile
import logging as log
import shutil
import pytest
import pyspark.sql as ps

if not os.environ.get('JAVA_HOME'):
    os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-1.8.0-openjdk-amd64'


@pytest.fixture(scope='session')
def spark_session(request):
    """Set up the Spark context with appropriate config for test.
    """
    def fin():
        """Clean up.
        """
        spark.stop()
    request.addfinalizer(fin)

    spark = ps.SparkSession.builder.master('local')\
        .appName('Spark Tute PyTest')\
        .config('spark.executor.memory', '2g')\
        .config('spark.executor.cores', '2')\
        .config('spark.cores.max', '10')\
        .config('spark.ui.port', '4050')\
        .config('spark.logConf', True)\
        .config('spark.debug.maxToStringFields', 100)\
        .getOrCreate()

    return spark


@pytest.fixture(scope='module')
def working_dir(request):
    """Temporary working directory.
    """
    def fin():
        """Tear down.
        """
        log.info('Deleting working temporay test directory: "%s"', dirpath)
        shutil.rmtree(dirpath)

    request.addfinalizer(fin)
    dirpath = tempfile.mkdtemp()
    log.info('Created temporary test directory: "%s"', dirpath)

    yield dirpath
