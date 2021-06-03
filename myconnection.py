# This file contains the fonction used to connect Python to the MySQL database
# Database name: Bookstore

# To install the library PyMySQL on Windows or Ubuntu, run the following command line in the shell: pip install PyMySQL


import pymysql


# Function returning a connection

def get_connection():
    connection = pymysql.connect(host='localhost', user='postgres',
    password='darkaby', database='Bookstore')
    return connection
