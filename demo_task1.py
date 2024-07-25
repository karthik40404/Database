import sqlite3

con=sqlite3.connect(('Database/demo_task1.db'))

try:
    con.execute("create table staff(emp_id int,name text,age int,salary real,phno int)") 
except:
    pass

print('\nstaff details')
print("1.add\n2.view\n3.search\n4.update\n5.delete\n6.exit")
emp=[]
while True:
    choice=int(input("enter your choice :"))
    if choice==1:
        emp_id=int(input('enter ID :'))
        name=str(input('enter name: '))
        age=int(input('enter age:'))
        salary=float(input('enter salary:'))
        phno=int(input('enter phno:'))
        con.execute('insert into staff (emp_id,name,age,salary,phno) values(?,?,?,?,?)',(emp_id,name,age,salary,phno))
        con.commit()

    elif choice==2:
        data=con.execute('select*from staff ')
        print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("emp_id","name","age","salary","phno"))
        print('_'*45)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[0],i[1],i[2],i[3],i[4]))
        con.commit()

    
    elif choice == 3:
        emp_id = int(input('Enter ID: '))
        data = con.execute('SELECT * FROM staff WHERE emp_id = ?', (emp_id,))
        f = 0  
        for i in data:
            if i: 
                f = 1
                print("{:<10}{:<20}{:<10}{:<10}{:<15}".format("Emp ID", "Name", "Age", "Salary", "Phone Number"))
                print('-' * 65)
                print("{:<10}{:<20}{:<10}{:<10}{:<15}".format(i[0], i[1], i[2], i[3], i[4]))
        if f == 0:
            print('Invalid ID')
        con.commit()


    elif choice==4:
        emp_id=int(input('enter ID :'))
        name=str(input('enter name: '))
        age=int(input('enter age:'))
        salary=float(input('enter salary:'))
        phno=int(input('enter phno:'))
        con.execute('update into staff (name,age,salary,phno) values(?,?,?,?)',(name,age,salary,phno))
        con.commit()

    elif choice==5:
        emp_id=int(input('enter ID :'))
        data=con.execute('delete from staff where emp_id=?',(emp_id,))
        con.commit()

    elif choice==6:
        print("you are exited")
        break
    else:
        print('invalid')  
