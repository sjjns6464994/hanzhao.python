import pandas as pd
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="123456",
  database="data",
)

df = pd.read_csv('data07.csv')

mycursor = mydb.cursor()


for index,row in df.iterrows():
  sql = "INSERT INTO testdata1 (`phone`,`profession`,lastest_date,total_price) VALUES (%s, %s, %s,%s)"
  val = (row['手机号码'], row['职业'],row['最近上线时间'],row['消费价格'])
  mycursor.execute(sql, val)

mydb.commit()



import pandas as pd
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="123456",
  database="data",
)

df = pd.read_csv('模拟数据2.csv')

mycursor = mydb.cursor()


for index,row in df.iterrows():
  sql = "INSERT INTO testdata (`name`,`number`,idnum,birthday,mail) VALUES (%s, %s, %s,%s,%s)"
  val = (row['姓名'], row['手机号码'], row['身份证号码'],row['出生年月'],row['邮箱'])
  mycursor.execute(sql, val)

mydb.commit()
