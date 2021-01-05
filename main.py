import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nonbinary24",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE My_Company")

# mycursor.execute("CREATE TABLE workers \
# (id INT AUTO_INCREMENT PRIMARY KEY, \
# FIRST_NAME VARCHAR(255), \
# LAST_NAME VARCHAR(255), \
# EMAIL VARCHAR(255), \
# PHONE_NUMBER VARCHAR(255), \
# HIRE_DATE DATE, \
# JOB_ID VARCHAR(255), \
# SALARY DECIMAL(10,2), \
# COMMISSION_PCT DECIMAL(3,2), \
# MANAGER_ID INTEGER(3), \
# DEPARTMENT_ID INTEGER(3))")
#
# # sqlFormula = "INSERT INTO workers (FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER,\
#  HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID)\
#  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# worker = [("Noy", "Kats", "noy@gmail.com", "052-236-1234", "14-01-11", "AI_PROG", 17000.00, 1.25, 100, 20),
#     ("Marie", "Lis", "marie@gmail.com", "052-678-8345", "19-03-01", "AI_PROG", 18000.00, 2.00, 100, 20),
#     ("Yohad", "Erkin", "yohad@gmail.com", "058-164-5896", "17-12-25", "MKTG", 13500.00, 4.00, 110, 60),
#     ("Shir", "Bester", "shir@gmail.com", "057-254-3487", "17-11-20", "IT_PROG", 21000.00, 1.50, 101, 30),
#     ("Yael", "Zakar", "yael@gmail.com", "058-254-7843", "18-09-20", "IT_PROG", 19500.00, 1.25, 101, 30),
#     ("Inbal", "Rot", "inbal@gmail.com", "057-348-1178", "20-02-14", "FE_PROG", 23000.00, 1.75, 102, 40),
#     ("Itamar", "Heller", "itamar@gmail.com", "053-681-6647", "19-02-01", "MKTG", 15000.00, 3.50, 110, 60),
#     ("Dvir", "Shalem", "dvir@gmail.com", "050-791-3327", "16-05-18", "FE_PROG", 16500.00, 1.50, 102, 40),
#     ("Naama", "Shalem", "naama@gmail.com", "054-7552-1017", "17-10-29", "AI_PROG", 17500.00, 2.00, 100, 20),
#     ("Shaked", "Nefesh", "shked@gmail.com", "055-995-7366", "19-12-05", "MKTG", 14000.00, 5.50, 110, 60)]
# mycursor.executemany(sqlFormula, worker)
# mydb.commit()