import mysql.connector

mydb = mysql.connector.connect(
  host="uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com",
  port=3306,
  user="admin",
  passwd="msci436project",
  database="uni_dss"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE student;"

sql = "INSERT INTO student_category VALUES (1,'Engineering'),(1,'Commerce/Business');"

mycursor.execute(sql)

mydb.commit()