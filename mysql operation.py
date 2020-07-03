import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='12345', database='hendry')
myCursor = mydb.cursor()
myCursor.execute('select * from employee')
result = myCursor.fetchall()
for i in result:
    print(i)
print('bye')
print('bye')