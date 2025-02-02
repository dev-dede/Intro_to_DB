import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dede_teddy",
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_stores")
    print(f"Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'mycursor' in locals() and mycursor: 
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()