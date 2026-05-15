#!/usr/bin/env python
# coding: utf-8

# In[40]:


#Library Management System
import sqlite3
conn=sqlite3.connect('lms.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
)
''')
conn.commit()


# In[30]:


def add_book(title,author,year):
    cursor.execute("INSERT INTO library (title,author,year) VALUES(?,?,?)",(title,author,year))
    conn.commit()
    print("Book is Added successfully.")


# In[43]:


def show_books():
    cursor.execute("SELECT * FROM library")
    rows=cursor.fetchall()
    for row in rows:
        print(row)


# In[27]:


def search_book(title,author):
    cursor.execute("SELECT * FROM library WHERE title=? AND author=?",(title,author))
    result=cursor.fetchone()
    print(result)


# In[25]:


def delete_book(title,author):
    cursor.execute("DELETE FROM library WHERE title=? AND author=?",(title,author))
    print("Book Deleted successfully.")


# In[26]:


def update_book(l_id,title,author,year):
    cursor.execute("UPDATE library SET title=?,author=?,year=? WHERE id=?",(title,author,year,l_id))
    print("Book Updated successfully.")


# In[34]:


def menu():
    while True:
        print("MENU")
        print("Select 1 to Add Book")
        print("Select 2 to View Books")
        print("Select 3 to Search Book")
        print("Select 4 to Remove Book")
        print("Select 5 to Update Book")
        print("Select 6 to Exit")
        Choice=int(input("Enter your Choice: "))
        if Choice==1:
            title=str(input("Enter title Of Book"))
            author=str(input("Enter author Of Book"))
            year=int(input("Enter Year of Book"))
            add_book(title,author,year)
        elif Choice==2:
            show_books()
        elif Choice==3:
            title=str(input("Enter title Of Book"))
            author=str(input("Enter author Of Book"))
            search_book(title,author)
        elif Choice==4:
            title=str(input("Enter title Of Book"))
            author=str(input("Enter author Of Book"))
            delete_book(title,author)
        elif Choice==5:
            title=str(input("Enter title Of Book"))
            author=str(input("Enter author Of Book"))
            year=int(input("Enter Year of Book"))
            l_id=int(input("Enter id Of Book"))
            update_book(l_id,title,author,year)
        elif Choice==6:
            break
        else:
            print("Invalid Choice")


# In[42]:


menu()
conn.close()


# In[ ]:




