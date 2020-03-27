import pandas as pd
import pymysql

host = "uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com"
port = 3306
dbname = 'uni_dss'
user = "admin"
password = "msci436project"

conn = pymysql.connect(host, user = user, port = port, passwd = password, db=dbname)

# sql = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='uni_dss'"

# response = pd.read_sql(sql,con=conn)

response = pd.read_sql("SELECT * FROM student",con=conn)

print(response)