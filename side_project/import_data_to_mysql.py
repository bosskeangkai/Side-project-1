import mysql.connector
import pandas as pd
from mysql.connector import Error
import datetime


try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "*********",
        database = "superstore",
        charset='utf8mb4'
    )

    if connection.is_connected():
        print('Connected to MySQL database')
    
    dataframe = pd.read_csv('./datasets/datasets.csv', parse_dates=['order_date','ship_date'], encoding='utf-8')

    cursor = connection.cursor()

    table_name = 'transaction'

    for _, row in dataframe.iterrows():
        # Escape special characters in string values
        escaped_values = [connection._cmysql.escape_string(value) if isinstance(value, str) else value for value in row]

        insert_query = f"INSERT INTO {table_name} ({', '.join(dataframe.columns)}) VALUES ({', '.join(['%s'] * len(dataframe.columns))})"
        
        cursor.execute(insert_query, escaped_values)

    connection.commit()
    print('Data inserted successfully')

except Error as e:
    print(f'Error while connecting to MySQL: {e}')

finally:
    cursor.close()
    connection.close()