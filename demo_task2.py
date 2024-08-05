import mysql.connector

con = mysql.connector.connect(
    host="localhost",      
    user="karthik_kv",     
    password="Karthik.404", 
    database="mydatabase"   
)

cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS customer (cus_id INT PRIMARY KEY, name VARCHAR(255), product_name VARCHAR(255), product_price FLOAT, phno VARCHAR(20))""")

print('\nCustomer Details')
print("1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Group\n7. Order\n8. Exit")

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        cus_id = int(input('Enter ID: '))
        name = input('Enter name: ')
        product_name = input('Enter product name: ')
        product_price = float(input('Enter product price: '))
        phno = input('Enter phone number: ')  
        cursor.execute('INSERT INTO customer (cus_id, name, product_name, product_price, phno) VALUES (%s, %s, %s, %s, %s)',(cus_id, name, product_name, product_price, phno))
        con.commit()
        print("Customer added successfully.")

    elif choice == 2:
        cursor.execute('SELECT * FROM customer')
        data = cursor.fetchall()
        print("{:<10}{:<20}{:<20}{:<15}{:<15}".format("cus_id", "name", "product_name", "product_price", "phno"))
        print('_' * 80)
        for i in data:
            print("{:<10}{:<20}{:<20}{:<15}{:<15}".format(i[0], i[1], i[2], i[3], i[4]))

    elif choice == 3:
        cus_id = int(input('Enter ID: '))
        cursor.execute('SELECT * FROM customer WHERE cus_id = %s', (cus_id,))
        data = cursor.fetchall()
        if data:
            print("{:<10}{:<20}{:<20}{:<15}{:<15}".format("cus_id", "name", "product_name", "product_price", "phno"))
            print('-' * 80)
            for i in data:
                print("{:<10}{:<20}{:<20}{:<15}{:<15}".format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print('Invalid ID')

    elif choice == 4:
        cus_id = int(input("Enter the ID of the customer to update: "))
        cursor.execute("SELECT * FROM customer WHERE cus_id = %s", (cus_id,))
        customer = cursor.fetchone()
        
        if customer:
            print('_' * 50)
            new_name = input(f'Enter new name (current: {customer[1]}): ')
            new_product_name = input(f'Enter new product name (current: {customer[2]}): ')
            new_product_price = float(input(f'Enter new product price (current: {customer[3]}): '))
            new_phno = input(f'Enter new phone number (current: {customer[4]}): ')
            
            cursor.execute('''UPDATE customer SET name = %s, product_name = %s, product_price = %s, phno = %s WHERE cus_id = %s''', (new_name, new_product_name, new_product_price, new_phno, cus_id))
            con.commit()
            print("Updated successfully!")
        else:
            print("Customer ID not found.")

    elif choice == 5:
        cus_id = int(input('Enter ID: '))
        cursor.execute('DELETE FROM customer WHERE cus_id = %s', (cus_id,))
        con.commit()
        print("Customer deleted successfully.")

    elif choice == 6:
        cursor.execute('SELECT name, MAX(product_price) FROM customer GROUP BY name')
        data = cursor.fetchall()
        if data:
            print("{:<20}{:<15}".format("Name", "Max Product Price"))
            print('-' * 35)
            for i in data:
                print("{:<20}{:<15}".format(i[0], i[1]))

    elif choice == 7:
        cursor.execute('SELECT * FROM customer ORDER BY name DESC')
        data = cursor.fetchall()
        if data:
            print("{:<10}{:<20}{:<20}{:<15}{:<15}".format("cus_id", "name", "product_name", "product_price", "phno"))
            print('-' * 80)
            for i in data:
                print("{:<10}{:<20}{:<20}{:<15}{:<15}".format(i[0], i[1], i[2], i[3], i[4]))

    elif choice == 8:
        print("You have exited.")
        break
    else:
        print('Invalid choice')
