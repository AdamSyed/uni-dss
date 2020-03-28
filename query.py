import pandas as pd
import pymysql

host = "uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com"
port = 3306
dbname = 'uni_dss'
user = "admin"
password = "msci436project"

conn = pymysql.connect(host, user = user, port = port, passwd = password, db=dbname)

# response = pd.read_sql("",con=conn)

# response = pd.read_sql(sql,con=conn)

# response = pd.read_sql("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'uni_dss';",con=conn)

response = pd.read_sql("SELECT * FROM student_course;",con=conn)

print(response)