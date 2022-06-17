


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
    print('\nwhere would you like to get data from\n')
    choice = int(input("1 - car_table\n2 - owner_table\n3 - employees\n4 - invoice\n\n"))
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

def getCreateInputs(table):
    cursor.execute(f"DESCRIBE {table}")
    inputs = []
    for i in cursor:
        print(i)
        inputs.append(input('Chose a value to insert into column above(primary keys will not be added for car table or employees): '))
    return inputs

def printTable(table):
    cursor.execute(f'SELECT * FROM {table}')
    print('\nTable:')
    for i in cursor:
        print(i)

def delete(table):
    key = input('Enter the primary key of the row you would like to delete: ')
    if table == 'car_table': return f'DELETE FROM {table} WHERE license_plate = {key}'
    if table == 'owner_table': return f'DELETE FROM {table} WHERE plate = {key}'
    if table == 'employees': return f'DELETE FROM {table} WHERE empID = {key}'
    if table == 'invoice': return f'DELETE FROM {table} WHERE plate = {key}'


def formatCreateExecute(inputs, table):
    if table == 'car_table': return f'INSERT INTO {table} (make,model,year,color) VALUES ("{inputs [0]}", "{inputs [1]}", {inputs [2]}, "{inputs [3]}")'
    if table == 'owner_table': return f'INSERT INTO {table} (name, address, phone_number, plate) VALUES ("{inputs [0]}", "{inputs [1]}", "{inputs [2]}", "{inputs [3]}")'
    if table == 'employees': return f'INSERT INTO {table} (name, salary) VALUES ("{inputs [0]}", {inputs [1]})'
    if table == 'invoice': return f'INSERT INTO {table} (employee, sale_date, price) VALUES ({inputs [0]}, "{inputs [1]}", {inputs [2]})'

def updateInputs(table):
    record = input("Enter the key value of the record you would like to change: ")
    cursor.execute(f"DESCRIBE {table}")
    for i in cursor:
        print(i)
    value_name = input("Enter the name of the value to replace: ")
    value = input("Enter the value: ")
    if table == 'car_table': cursor.execute(f'UPDATE {table} SET {value_name} = "{value}" WHERE license_plate = {record}')
    if table == 'owner_table': cursor.execute(f'UPDATE {table} SET {value_name} = "{value}" WHERE plate = {record}')
    if table == 'employees': cursor.execute(f'UPDATE {table} SET {value_name} = "{value}" WHERE empID = {record}')
    if table == 'invoice': cursor.execute(f'UPDATE {table} SET {value_name} = "{value}" WHERE employee = {record}')
    return

#create method
def create_method():
    table = chooseTable()
    inputs = getCreateInputs(table)
    cursor.execute(f'{formatCreateExecute(inputs, table)}')
    db.commit()
    return


#read method
def read_method():
    table = chooseTable()
    printTable(table)
    return

#update method
def update_method():
    table = chooseTable()
    printTable(table)
    updateInputs(table)
    db.commit()
    return

#delete method
def delete_method():
    table = chooseTable()
    printTable(table)
    cursor.execute(f'{delete(table)}')
    db.commit()
    return

while True:
    print("\n\n---Menu---")
    print('1. Create')
    print('2. Read')
    print('3. Update')
    print('4. Delete')
    print('5. exit')
    
    try:choice = int(input("\n----Select what you would like to do to the database----\n"))
    except:print("enter a number 1-5")
    else:
        if(choice == 1): create_method()
        elif(choice == 2): read_method()
        elif(choice == 3): update_method()
        elif(choice == 4): delete_method()
        elif(choice == 5): break
        else: print("enter a number 1-5")


    