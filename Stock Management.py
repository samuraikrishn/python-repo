# First copy this in your my sql server

# -- Create the database
# CREATE DATABASE StockManagement;

# -- Use the newly created database
# USE StockManagement;

# -- Create Users table
# CREATE TABLE Users (
#     user_id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     role VARCHAR(50) NOT NULL
# );

# -- Create Products table
# CREATE TABLE Products (
#     product_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     description TEXT,
#     price DECIMAL(10, 2) NOT NULL,
#     quantity INT NOT NULL
# );

# -- Create Purchases table
# CREATE TABLE Purchases (
#     purchase_id INT AUTO_INCREMENT PRIMARY KEY,
#     product_id INT,
#     quantity INT NOT NULL,
#     purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (product_id) REFERENCES Products(product_id)
# );

# -- Create Sales table
# CREATE TABLE Sales (
#     sale_id INT AUTO_INCREMENT PRIMARY KEY,
#     product_id INT,
#     quantity INT NOT NULL,
#     sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (product_id) REFERENCES Products(product_id)
# );

import mysql.connector
from mysql.connector import Error
import time

# Function to create a database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tiger",
            database="StockManagement"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to execute a query
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Function to fetch results from a query
def fetch_query(connection, query, data=None):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

# Product Management Functions
def add_product(connection):
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    query = """
    INSERT INTO Products (name, description, price, quantity)
    VALUES (%s, %s, %s, %s)
    """
    data = (name, description, price, quantity)
    execute_query(connection, query, data)

def update_product(connection):
    product_id = int(input("Enter product ID to update: "))
    name = input("Enter new product name: ")
    description = input("Enter new product description: ")
    price = float(input("Enter new product price: "))
    quantity = int(input("Enter new product quantity: "))
    query = """
    UPDATE Products
    SET name = %s, description = %s, price = %s, quantity = %s
    WHERE product_id = %s
    """
    data = (name, description, price, quantity, product_id)
    execute_query(connection, query, data)

def delete_product(connection):
    product_id = int(input("Enter product ID to delete: "))
    query = "DELETE FROM Products WHERE product_id = %s"
    data = (product_id,)
    execute_query(connection, query, data)

def get_all_products(connection):
    query = "SELECT * FROM Products"
    products = fetch_query(connection, query)
    for product in products:
        print(product)

# Purchase Management Functions
def add_purchase(connection):
    product_id = int(input("Enter product ID for purchase: "))
    quantity = int(input("Enter purchase quantity: "))
    query = """
    INSERT INTO Purchases (product_id, quantity)
    VALUES (%s, %s)
    """
    data = (product_id, quantity)
    execute_query(connection, query, data)

def get_all_purchases(connection):
    query = "SELECT * FROM Purchases"
    purchases = fetch_query(connection, query)
    for purchase in purchases:
        print(purchase)

# Sales Management Functions
def add_sale(connection):
    product_id = int(input("Enter product ID for sale: "))
    quantity = int(input("Enter sale quantity: "))
    query = """
    INSERT INTO Sales (product_id, quantity)
    VALUES (%s, %s)
    """
    data = (product_id, quantity)
    execute_query(connection, query, data)

def get_all_sales(connection):
    query = "SELECT * FROM Sales"
    sales = fetch_query(connection, query)
    for sale in sales:
        print(sale)

# User Management Functions
def add_user(connection):
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role: ")
    query = """
    INSERT INTO Users (username, password, role)
    VALUES (%s, %s, %s)
    """
    data = (username, password, role)
    execute_query(connection, query, data)

def get_all_users(connection):
    query = "SELECT * FROM Users"
    users = fetch_query(connection, query)
    for user in users:
        print(user)

# Main program with menu-driven interface
if __name__ == "__main__":
    connection = create_connection()

    while True:
        print("\nStock Management System")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Add Purchase")
        print("6. View All Purchases")
        print("7. Add Sale")
        print("8. View All Sales")
        print("9. Add User")
        print("10. View All Users")
        print("11. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(connection)
        elif choice == '2':
            get_all_products(connection)
        elif choice == '3':
            update_product(connection)
        elif choice == '4':
            delete_product(connection)
        elif choice == '5':
            add_purchase(connection)
        elif choice == '6':
            get_all_purchases(connection)
        elif choice == '7':
            add_sale(connection)
        elif choice == '8':
            get_all_sales(connection)
        elif choice == '9':
            add_user(connection)
        elif choice == '10':
            get_all_users(connection)
        elif choice == '11':
            for i in range (3):
                print("Exiting the program.")
                time.sleep(1)
            print("Thank You")
            break
        else:
            print("Invalid choice. Please try again.")

