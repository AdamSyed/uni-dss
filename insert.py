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

sql = "INSERT INTO student_course VALUES (1,'Business/Economics',87),(1,'English',89),(1,'Humanities',82),(1,'Information Technology/Programming',86),(1,'Maths',94),(1,'Sciences',91);"

mycursor.execute(sql)

mydb.commit()