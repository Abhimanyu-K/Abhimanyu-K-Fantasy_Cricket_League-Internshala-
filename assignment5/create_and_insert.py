import sqlite3

Books=sqlite3.connect('books.db')
curBooks=Books.cursor()
title=input("Name of the book?")
author=input("Name of the Author?")
price=input("Enter the price.")
curBooks.execute('CREATE TABLE IF NOT EXISTS books(Title, Author, Price)')
curBooks.execute("INSERT INTO books (Title, Author, Price) VALUES(?,?,?);",(title,author,price))
Books.commit()
