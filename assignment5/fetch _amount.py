import math
import sqlite3

Books=sqlite3.connect('books.db')
title=input("Enter the book title: ")
quantity=int(input("Enter the quantity: "))
sql="SELECT Price from books WHERE Title='"+title+"';"
curBooks=Books.cursor()
curBooks.execute(sql)
price=curBooks.fetchone()
print(price[0]*quantity)
input('Press Enter to exit')
