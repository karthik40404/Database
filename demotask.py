import mysql.connector

con = mysql.connector.connect(
    host="localhost",      
    user="karthik_kv",     
    password="Karthik.404", 
    database="mydatabase"   
)

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS staff_details (emp_id INT, emp_address TEXT)")

# emp_id = int(input('Enter ID: '))
# emp_address = input('Enter address: ')

# cursor.execute('INSERT INTO staff_details (emp_id, emp_address) VALUES (%s, %s)', (emp_id, emp_address))
# con.commit()

# cursor.execute('SELECT * FROM staff_details')
# data = cursor.fetchall()
# print("{:<10} {:<30}".format("emp_id", "emp_address"))
# print('_' * 40)
# for row in data:
#     print("{:<10} {:<30}".format(row[0], row[1]))

#cursor.execute('select staff.emp_id,staff.name,staff.age,staff.salary,staff_details.emp_address from staff join staff_details on staff.emp_id=staff_details.emp_id')
#cursor.execute('select staff.emp_id,staff.name,staff.age,staff.salary,staff_details.emp_address from staff right join staff_details on staff.emp_id=staff_details.emp_id')
cursor.execute('select staff.emp_id,staff.name,staff.age,staff.salary,staff_details.emp_address from staff cross join staff_details')

data = cursor.fetchall()
print('_' * 40)
for row in data:
    print(row)



