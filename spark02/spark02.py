from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, DateType,LongType,StringType,IntegerType
from pyspark.sql import functions as F
import pandas as pd


### 1. 创建SparkSession对象
### 2. 读取文件
### 3. RDD转换（SQL）


if __name__ == "__main__":

    spark = SparkSession.builder.appName("dx").master("local[*]").getOrCreate()
    #data01标签表
    structType1 = StructType(
        [
            StructField("date", DateType()),
            StructField("desc_num", StringType()),
            StructField("name", StringType()),
            StructField("phone", StringType()),
            StructField("ssn", StringType()),
        ]#逗号不识别

    )
    data04 = spark.read.option("sep",",").schema(structType1) \
       .csv("data04.csv")
    # call_details = spark.read.option("sep", "\t").option("encoding","utf-8").schema(structType1) \
    #     .csv("data04.csv")
    #
    # data03标签表
    structType2 = StructType(
        [
            StructField("author",  StringType()),
            StructField("profession", StringType()),
            StructField("price", IntegerType()),
        ]
    )

    data05 = spark.read.option("sep",",").schema(structType2) \
        .csv("data05.csv")

    # 读取两个CSV文件
    df1 = pd.read_csv('data04.csv')
    df2 = pd.read_csv('data05.csv')

    # 使用concat函数进行横向合并
    call_all_data_df = pd.concat([df1, df2], axis=1)

    # 输出合并后的结果
    # print(call_all_data_df)

    # import pandas as pd
    #
    # # 读取两个CSV文件
    # df1 = pd.read_csv('file1.csv')
    # df2 = pd.read_csv('file2.csv')
    #
    # # 使用concat函数进行横向合并
    # merged_df = pd.concat([df1, df2], axis=1)
    #
    # # 将合并后的数据保存为新的CSV文件
    call_all_data_df.to_csv('./data06.csv', index=False)


    # call_all_data_df = data04.join(
    #     data05
    #     # call_details["desc_num"] == call_flags["desc_num"]
    # )
    #
    structType3 = StructType(
        [ StructField("date", DateType()),
            StructField("desc_num", StringType()),
            StructField("name", StringType()),
            StructField("phone", StringType()),
            StructField("ssn", StringType()),
            StructField("author", StringType()),
            StructField("profession", StringType()),
            StructField("price", IntegerType()),
        ]
    )

    data06 = spark.read.option("sep", ",").schema(structType3) \
        .csv("data06.csv")

    # data06.show(20)

    call_diff_date_df =data06.selectExpr("*", "12-day(date) as diff_day") #最近登录的时间距离今天的时间，diff_day是新起的别名

    call_rmf_init_df = call_diff_date_df.groupBy(["phone", "profession"]).agg(
        F.min("diff_day").alias("lastest_date"),
        F.sum("price").alias("total_price"),
        # F.sum("duration").alias("to.tal_duration")
    ).select(
        "phone"
        , "profession"
        , "lastest_date"
        , "total_price"
        # , "total_duration"
    )

    sort1 =call_rmf_init_df.sort("lastest_date", ascending=True)
    sort1.write.csv("data07.csv")
    # sort1 = pd. DataFrame(call_rmf_init_df)
    # sort1.to_csv('data07.csv', encoding='utf_8_sig')  # 防止中文乱码
    sort1.show(20)

    # sort1_df = df.sort_values(by='column_name')  # 使用 sort_values 方法对 DataFrame 进行排序

    # df.to_csv('filename.csv', index=False)
    # for i in sort:
    #     if i ==sort[19]:
    #         break
    # call_rmf_init_df.show(20)
    sort2 = call_rmf_init_df.sort("total_price", ascending=False)
    sort2.write.csv("data8.csv")
    # sort2.to_csv('./data08.csv', index=False)
    sort2.show(20)
# df = pd.DataFrame(['',])





