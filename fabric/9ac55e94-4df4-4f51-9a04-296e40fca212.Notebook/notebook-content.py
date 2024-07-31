# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

def add(a: int, b: int) -> int:
    return a + b

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace
from pyspark.testing.utils import assertDataFrameEqual

def remove_extra_spaces(spark: SparkSession, df: DataFrame, column_name: str) -> DataFrame:
    """Remove extra spaces from the specified column using regexp_replace"""

    df_transformed = df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

    return df_transformed

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
