import sqlite3

con=sqlite3.connect('Database/demo6.db') #connection

try:
    con.execute("create table student(age int,name text,mark real)") #create table
except:
    pass

# students=int(input('enter the limit :'))
# for i in range (students):
#     age=int(input('enter age:'))
#     name=str(input('enter name: '))
#     mark=float(input('enter mark:'))
#     con.execute('insert into student (age,name,mark) values(?,?,?)',(age,name,mark))
# con.commit()

data=con.execute('select name,count(mark) from student group by name')#groupby

for i in data:
    print(i)