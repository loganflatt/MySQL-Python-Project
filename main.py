

import mysql.connector

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

def chooseTable():
    print('\nwhere would you like to read an entry\n')
    choice = int(input("1 - car_table\n2 - owner_table\n3 - employees\n4 - invoice\n"))
    if choice == 1:
        return 'car_table'
    elif choice == 2:
        return 'owner_table'
    elif choice == 3:
        return 'employees' 
    elif choice == 4:
        return 'invoice'
    else: 
        print('Give a valid input')
        return chooseTable()

def getInputs():
    inputs = []
    for i in cursor:
        print(i)
        inputs.append(input('Chose a value to insert into column above(primary keys will not be added for car table or employees): '))
    return inputs

def printTable():
    print('\nTable:')
    for i in cursor:
        print(i)

def delete(table):
    key = input('Enter the primary key of the row you would like to delete: ')
    cursor.execute(f'DELETE FROM {table} WHERE license_plate = {key}')
    db.commit()
    return 

#create method
def create_method():
    table = chooseTable()
    cursor.execute(f"DESCRIBE {table}")
    inputs = getInputs()
    values = '"' + inputs[0] + '"'
    for i in range(1,len(inputs)):
        values += ', "' + values[i] + '"'
    cursor.execute(f'INSERT INTO {table} (make,model,year,color) VALUES ("{values}")')
    db.commit()
    return


#read method
def read_method():
    table = chooseTable()
    cursor.execute(f'SELECT * FROM {table}')
    printTable()
    return

#update method
def update_method():
    table = chooseTable()
    
    return

#delete method
def delete_method():
    table = chooseTable()
    cursor.execute(f'SELECT * FROM {table};')
    printTable()
    delete('car_table')
        
    
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


    