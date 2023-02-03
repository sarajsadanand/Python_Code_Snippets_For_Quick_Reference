#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://youtu.be/Pjn4P39310g

# MySQL Insaller --> https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.29.0.msi
# timestamp: 26:20

# SQL from python
# timestamp: 04:11:00


# In[13]:


# import libraries
import mysql.connector  #pip install mysql-connector-python
from mysql.connector import Error
import pandas as pd


# In[14]:


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

pwd = "password123" # put the MySQL terminal password
db = "my_db"
connection = create_server_connection("localhost", "root", pwd)


# In[15]:


# Create my_db database instance
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_db_query = "CREATE DATABASE my_db"

create_database(connection, create_db_query)


# In[22]:


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# In[23]:


# Execute sql queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query ran successfully")
    except Error as err:
        print(f"Error: '{err}'")


# In[28]:


# Create a table
create_orders_table = """
CREATE TABLE ORDERS(
ORDER_ID INT PRIMARY KEY,
CUSTOMER_NAME VARCHAR(30) NOT NULL,
PRODUCT_NAME VARCHAR(30) NOT NULL,
DATE_ORDERED DATE,
QUANTITY INT,
UNIT_PRICE FLOAT,
PHONE_NUMBER VARCHAR(20));
"""

pwd = "password123" # put the MySQL terminal password
db = "my_db"

connection = create_db_connection("localhost", "root", pwd, db)
execute_query(connection,create_orders_table)


# In[36]:


# Insert data
data_orders = """
insert into orders values
(101, 'Steve', 'Laptop', '2018-06-12', 2, 800, '6293730802'),
(102, 'Jos', 'Books', '2019-02-10', 10, 12, '8367489124'),
(103, 'Stacy', 'Trousers', '2019-12-25', 5, 50, '8976123645'), 
(104, 'Nancy', 'T-Shirts', '2018-07-14', 7, 30, '7368145099'),
(105, 'Maria', 'Headphones', "2019-05-30", 6, 48, '8865316698'),
(106, 'Danny', 'Smart TV', '2018-08-20', 10, 300, '7720130449');
"""
connection = create_db_connection("localhost", "root", pwd, db)
execute_query(connection,data_orders)


# In[37]:


# To read query and display the result
def read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# In[46]:


# Select year of order for each customer
q2 = """
select customer_name,year(date_ordered) from orders;
"""
connection = create_db_connection("localhost", "root", pwd, db)
results = read_query(connection, q2)
for results in results:
    print(results)


# In[51]:


# Using the select
q1 = """
select * from orders
"""
connection = create_db_connection("localhost", "root", pwd, db)
dat = read_query(connection, q1)
for p in dat:
    print(p)


# In[59]:


# Creating DataFrame using the above data
from_db = [] # empty list

for i in dat:
    data_list = list(i)
    print(data_list)
    from_db.append(data_list) # list within a list

print("---------------------------------")
print(from_db)

col_names = ["ORDER_ID", "CUSTOMER_NAME","PRODUCT_NAME","DATE_ORDERED","QUANTITY","UNIT_PRICE","PHONE_NUMBER"]

df = pd.DataFrame(from_db, columns = col_names)


# In[56]:


df


# In[ ]:




