import mysql.connector
from mysql.connector import Error
import sys
import json

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='assignment',
                                         user='root',
                                         password='Aastha123%')

    mySql_insert_query = """INSERT INTO inventory (categories, name,  twitter)  
    VALUES ( %(categories)s , %(name)s , %(twitter)s ) """

    records_to_insert = json.loads(sys.argv[1:][0])

    for rec in records_to_insert:
        print("importing: Name:", rec["name"], "; Categories:", rec["categories"], "; Twitter:", rec["twitter"] )
    cursor = connection.cursor()

    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record(s) inserted successfully into Inventory table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


