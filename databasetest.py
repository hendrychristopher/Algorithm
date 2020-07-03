# Il package "mysql-connector" ho dovuto prima scaricarlo, da cmd.exe, col comando
#+          {percorso}\pip3 install mysql-connector
#                          ^       ^
import mysql.connector

miodb = mysql.connector.connect(host="localhost", user="root", passwd="NonCE2Senza3", database="telusko")

miocursore = miodb.cursor()

#miocursore.execute("show databases")
miocursore.execute("select * from students order by name")

for i in miocursore:
    print(i)