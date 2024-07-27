import sqlite3

dtl=sqlite3.connect('Database/demo7.db') #connection

try:
    dtl.execute("create table detail(name text,place text,cno int,address text)") #create table
except:
    pass

# details=int(input('enter the limit :'))
# for i in range (details):
#     name=str(input('enter name: '))
#     place=str(input('enter place: '))
#     cno=int(input('enter number: '))
#     address=str(input('enter address: '))
#     dtl.execute('insert into detail(name ,place,cno,address) values(?,?,?,?)',(name,place,cno,address))
# dtl.commit()


#data=dtl.execute('select student.age,student.name,student.mark,detail.place,detail.cno,detail.address from student left join detail on student.name=detail.name')
data=dtl.execute('select student.age,student.name,student.mark,detail.place,detail.cno,detail.address from student cross join detail on student.name=detail.name')
for i in data:
    print(i)