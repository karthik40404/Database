import sqlite3

# con=sqlite3.connect('demo.db') #connection

# try:
#     con.execute("create table student(age int,name text,mark real)") #create table
# except:
#     pass
# con.execute('insert into student (age,name,mark) values(21,"karlee",34),(22,"brulee",45),(23,"darlee",56)') #add a value
# con.commit()# to save


con=sqlite3.connect('python_programs/database/demo.db') #connection

try:
    con.execute("create table student(age int,name text,mark real)") #create table
except:
    pass

age=int(input('age'))
name=str(input('name'))
mark=float(input('mark'))

con.execute("insert into student(age,name,mark) values (?,?,?)",(age,name,mark))
con.commit()
