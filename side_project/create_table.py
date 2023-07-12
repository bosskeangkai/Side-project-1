import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*********',
    database='superstore'
)

# create a table contain columns name that match CSV file
create_table_query= '''
    CREATE TABLE transaction (
        order_id VARCHAR(255),
        order_date DATE,
        ship_date DATE,
        ship_mode CHAR(255),
        customer_name CHAR(255),
        segment VARCHAR(255),
        state VARCHAR(255),
        country VARCHAR(255),
        market VARCHAR(255),
        region VARCHAR(255),
        product_id VARCHAR(255),
        category VARCHAR(255),
        sub_category VARCHAR(255),
        product_name VARCHAR(255),
        sales INT(255),
        quantity INT(255),
        discount FLOAT(5),
        profit FLOAT(5),
        shipping_cost FLOAT(5),
        order_priority VARCHAR(255),
        year YEAR
    )
'''
connection.cursor().execute(create_table_query)

# close the connection 
connection.close()