

import mysql.connector
1

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Flatt07l',
    database = 'cardealership'
)

"""
Project:
Create a Python application that connects to either a MySQL or MongoDB server,
and performs CRUD operations on a database.
    - The application must be able to create, read, update, and delete.
    - Use at least 3 different tables.
    - The tables must contain at minimum 50 records each.
    - The tables must have a primary / foreign key relationship.
"""

cursor = db.cursor()


def insertFunc():
    inputs = []
    count = 0
    
    for i in cursor:
        print(i)
        count += 1
        inputs.append(input('Chose a value to insert into column above(primary keys will not be added): '))
    return inputs



def create_method():
    #create method
    print('\nwhere would you like to create an entry\n')
    choice = int(input("1 - car_table\n2 - owner_table\n3 - employees\n4 - invoice\n"))
    if choice == 1:
        cursor.execute("DESCRIBE car_table")
        inputs = insertFunc()
        input_tuple = (inputs[0],inputs[1],int(inputs[2]), inputs[3])
        cursor.execute('INSERT INTO car_table (make,model,year, color) VALUES (%s, %s,%s,%s)', input_tuple)
        db.commit()
    return

def read_method():
    #read method
    print('\nwhere would you like to read an entry\n')
    choice = input("1 - car_table\n2 - owner_table\n3 - employees\n4 - invoice\n")
    return

def update_method():
    #create method
    print('\nwhere would you like to update an entry\n')
    choice = int(input("1 - car_table\n2 - owner_table\n3 - employees\n4 - invoice\n"))
    
    return

def delete_method():
    #create method
    print('\nwhere would you like to delete an entry\n')
    choice = input("1 - car_table\n2 - owner_table\n3 - employees\n4 - invoice\n")
    return

while True:
    print("\n\n---Menu---")
    print('1. Create')
    print('2. Read')
    print('3. Update')
    print('4. Delete')
    print('5. exit')
    choice = int(input("\n----Select what you would like to do to the database----\n"))
    if(choice == 1): create_method()
    elif(choice == 2): read_method()
    elif(choice == 3): update_method()
    elif(choice == 4): delete_method()
    if(choice == 5): break


    