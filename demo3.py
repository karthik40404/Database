import sqlite3

con=sqlite3.connect('Database/demo3.db') #connection

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

con.execute('update student set name ="sanu" where name ="qwe"')
con.execute('UPDATE student SET name = "anu" WHERE name = "asd"')
con.execute('UPDATE student SET name="vinu",age=30,mark=80 where name="zxc" ')
con.commit()
data=con.execute('select*from student')

print("{:<10}{:<10}{:<10}".format("age","name","mark"))
print('_'*25)
for i in data:
    print("{:<10}{:<10}{:<10}".format(i[0],i[1],i[2]))