import mysql.connector

mydb = mysql.connector.connect(
  host="uni-dss.cmuqyhsxn149.us-east-2.rds.amazonaws.com",
  port=3306,
  user="admin",
  passwd="msci436project",
  database="uni_dss"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE university;"

# sql = "INSERT INTO university VALUES (1,'Algoma University','1520 Queen Street East, Sault Ste. Marie, Ontario, Canada P6A 2G4',73368,1965,1400,20,21,31,28,1,1,4,14,5,2),(2,'Brock University','1812 Sir Isaac Brock Way, St. Catharines, ON, L2S 3A1 Canada',133113,1964,19100,21,22,27,30,3,3,4,29,3,6),(3,'Carleton University','1125 COLONEL BY DRIVE, OTTAWA, ON, K1S 5B6, CANADA',994837,1942,30416,22,22,26,30,5,4,4,28,2,9),(4,'Lakehead University','955 Oliver Rd Thunder Bay, ON, P7B5E1',110172,1946,8310,20,15,35,30,3,2,4,15,4,5),(5,'Laurentian University','935 Ramsey Lake Rd. Sudbury, ON P3E 2C6',164926,1960,9500,20,15,33,32,3,2,4,18,4,5),(6,'McMaster University','1280 Main Street West, Hamilton, Ontario  L8S 4L8',579200,1887,30117,32,23,20,25,4,4,5,27,2,8),(7,'Nipissing University','100 College Drive, Box 5002, North Bay, ON, Canada  P1B 8L7',51553,1992,5679,17,17,35,31,1,2,2,23,4,3),(8,'Ontario Tech University (University of Ontario Institute of Technology)','2000 Simcoe Street North, Oshawa, Ontario L1G 0C5, Canada',170071,2002,10113,25,30,25,20,3,3,2,19,3,6),(9,'Queen''s University','99 University Ave, Kingston, ON K7L 3N6',136685,1841,24143,28,25,22,25,3,4,5,28,2,7),(10,'Royal Military College of Canada','13 General Crerar Crescent, Kingston, ON K7K 7B4',136685,1876,2400,20,30,20,30,3,1,5,5,5,4),(11,'Ryerson University','350 Victoria Street, Toronto, ON M5B 2K3',2930000,1948,36347,22,33,30,15,5,4,4,26,2,9),(12,'Trent University','1600 West Bank Drive, Peterborough, ON Canada, K9L 0G2',84230,1964,8940,20,25,29,26,2,2,4,18,4,4),(13,'University of Guelph','50 Stone Road East, Guelph, Ontario, Canada, N1G 2W1',135474,1964,28687,23,19,28,30,3,4,4,34,2,7),(14,'University of Ottawa','75 Laurier Ave. East, Ottawa ON, K1N 6N5 Canada',994837,1848,42587,25,27,20,28,5,4,5,28,2,9),(15,'University of Toronto','27 King''s College Cir, Toronto, ON M5S',2930000,1827,61690,32,38,15,15,5,5,5,29,1,10),(16,'University of Waterloo','200 University Avenue West, Waterloo, ON, Canada  N2L 3G1',113520,1957,41000,38,37,15,10,3,4,4,27,2,7),(17,'University of Windsor','401 Sunset Avenue, Windsor, Ontario N9B 3P4',233763,1963,16491,15,20,35,30,3,3,4,21,3,6),(18,'Western University','1151 Richmond Street, London, Ontario, Canada, N6A 3K7',404669,1878,28386,28,36,15,21,4,4,5,26,2,8),(19,'Wilfrid Laurier University','75 University Ave W, Waterloo, ON N2L 3C5',113520,1960,18589,20,30,25,25,3,3,4,25,3,6),(20,'York University','4700 Keele Street, Toronto, ON, Canada M3J 1P3',2930000,1959,53000,25,20,30,25,5,5,4,33,1,10);"

sql = "INSERT INTO student VALUES(1, 'Adam','Syed', 'adam.syed@rogers.com','password', 20, 40, 30, 15, 15, 4, 3, 3, 25, 3, 5);"

mycursor.execute(sql)

mydb.commit()