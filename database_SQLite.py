import sqlite3

# Creating database   called fine
conn = sqlite3.connect('company_Insta_Perm.db')

# creating cursor for exrxcution commnds in sql database
cursor = conn.cursor()

# Creat table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS employee (
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL,
                  position TEXT NOT NULL,
                  city TEXT NOT NULL)''')

# function for adding the data intyo table
def add_data(name, age,position, city):
    cursor.execute("INSERT INTO employee (name, age,position, city) VALUES (?, ?, ?,?)", (name, age, position,city))
    conn.commit()
    print("the data is successfully aadded .")

# function for extractiion the data
def get_data(filter_query):
    cursor.execute("SELECT * FROM employee WHERE " + filter_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# functuion for update
def update_data(filter_query, new_data):
    cursor.execute("UPDATE employee SET " + new_data + " WHERE " + filter_query)
    conn.commit()
    print("the data is successfully updated .")

# function for deleting data from a table wmployee
def delete_data(filter_query):
    cursor.execute("DELETE FROM employee WHERE " + filter_query)
    conn.commit()
    print("data issuccessfully deleted .")

# main user
if __name__ == "__main__":

    # Add
    add_data("ALi", 26,"ML engineer and Python developer", "Saint Petersburg ")
    add_data("Victor", 20,"Python developer ", "Moscow")
    add_data("Nastya", 18,"intern", "Perm")
    add_data("Yulia", 21,"HR recruiter ", "Kutaisi")
    add_data("Valdimer ", 28,"Data scientist", "Rostov")
    add_data("Andrew", 33,"projetc Manager ", "Moscow")

    # Extract
    get_data("city = 'Moscow'")
    print("\n")

    # Update
    update_data("name = 'Andrew' ", "age = 32")
    get_data("name='Andrew' ")

    # Delete
    delete_data("city = 'Moscow' ")
