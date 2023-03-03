#backend
import sqlite3

def BookData():
    con=sqlite3.connect("book1.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Book_ID text,Book_Name text,Release_Date text,Publisher text,Authors text,Budget text,Pages text,Rating text")
    con.commit()
    con.close()
    
def AddBookRec(Book_ID,Book_Name,Release_Date,Publisher,Authors,Budget,Pages,Rating):
    con=sqlite3.connect("book1.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?,?,?,?,?)", (Book_ID,Book_Name,Release_Date,Publisher,Author,Budget,Pages,Rating))
    con.commit()
    con.close()

def ViewBookData():
    con=sqlite3.connect("book1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteBookRec(id):    
    con=sqlite3.connect("book1.db")    
    cur=con.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    con.commit()
    con.close()  

def SearchBookData(Book_ID="",Book_Name="",Release_Date="",Publisher="",Authors="",Budget="",Pages="",Rating=""):  
    con=sqlite3.connect("book1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM books WHERE Book_ID=? OR Book_Name=? OR Release_Date=? OR Publisher=? OR Authors=? OR Budget=? OR Pages=? OR Rating=?",(Book_ID,Book_Name,Release_Date,Publisher,Authors,Budget,Pages,Rating))
    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateBookData(id,Book_ID="",Book_Name="",Release_Date="",Publisher="",Authors="",Budget="",Pages="",Rating=""):
    con=sqlite3.connect("book1.db")    
    cur=con.cursor()
    cur.execute("UPDATE books SET Book_ID=?,Book_Name=?,Release_Date=?,Publisher=?,Authors=?,Budget=?,Pages=?,Rating=?, WHERE id=?",(Book_ID,Book_Name,Release_Date,Publisher,Authors,Budget,Pages,Rating))
    con.commit()
    con.close()
