import mysql.connector

try:
  with mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'password',
  ) as connection:
    create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    with connection.cursor() as cursor:
      cursor.execute(create_db_query)
      print("Database 'alx_book_store' created successfully!")
      cursor.close()
      connection.close()
except mysql.connector.Error as e:
  print(e)