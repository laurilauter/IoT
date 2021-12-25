# app.py
import os
import sys
from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)
application = app # our hosting requires application in passenger_wsgi



@app.route('/')
def hello_world():
    

    try:
        connection = mysql.connector.connect(host='185.169.68.30',
                                            database='lautrade_sensor',
                                            user='lautrade_lautradesensor',
                                            password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM temp")
            records = cursor.fetchall()
            print("You're connected to database: ", records)





    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template ('index.html', records=records)



if __name__ == "__main__":
    app.run(host='0.0.0.0')