import mysql.connector
class Database:
    def connect(self):
        connection = mysql.connector.connect(host="localhost", user="root",password="Root@1234",database="batch18")
        return connection
        print("database connection created")