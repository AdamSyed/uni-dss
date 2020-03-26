import pandas as pd
import pymysql

host = "uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com"
port = 3306
dbname = 'uni_dss'
user = "admin"
password = "msci436project"

conn = pymysql.connect(host, user = user, port = port, passwd = password, db=dbname)

response = pd.read_sql("INSERT INTO university VALUES ('1','Algoma University','1520 Queen Street East, Sault Ste. Marie, Ontario, Canada P6A 2G4','73368','1965','1400','20','21','31','28','1','1','4','14','5','2');",con=conn)

# response = pd.read_sql("SELECT * FROM university",con=conn)

print(response)