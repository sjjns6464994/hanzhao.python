from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, DateType,StructField,LongType,IntegerType,StringType

if __name__ == "__main__":

    spark = SparkSession.builder.master("local[*]").appName("aqi").getOrCreate()

    # DataFrame pandas -> DataFrame 分布式
    #                  -> 数据库中的表
    df = spark.read.option("header",True).csv("../files/input/sql/aqi.csv")

    # df.printSchema()
    # print(df.show(10))

    df.createOrReplaceTempView("aqi")
    ### 1. 数据集中有有多少个城市？

    # sql = "select distinct city from aqi"
    # spark.sql(sql).show()

    ### 2. 查看上海市平均的AQI值是多少

    ### select city,aqi(CAST(aqi AS DOUBLE)) from aqi where city = '上海'
    # sql = "select round(avg(CAST(aqi AS DOUBLE)), 2) as aqi_avg from aqi where city = '上海'"
    # spark.sql(sql).show()

    ### 查看每个城市的AQI的平均值

    ### select city, avg(CAST(aqi AS DOUBLE)) from aqi group by city

    sql = "select city, round(avg(CAST(aqi AS DOUBLE)), 2)  as aqi_avg from aqi group by city "
    spark.sql(sql).show()