import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Reshiram1",
  database="Music"
)

mycursor = mydb.cursor()

# Creates the db
#mycursor.execute("CREATE DATABASE Music")

# Creates the Song table
#mycursor.execute("CREATE TABLE Song (name VARCHAR(300), bpm int UNSIGNED, M_ID_S int PRIMARY KEY AUTO_INCREMENT)")

# Creates the Chore table
#mycursor.execute("CREATE TABLE Chore (name VARCHAR(300), bpm int UNSIGNED, M_ID_C int PRIMARY KEY AUTO_INCREMENT)")

