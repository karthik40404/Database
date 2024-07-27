import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="karthik_kv",
  password="Karthik.404"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")           