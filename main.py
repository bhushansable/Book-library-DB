import sqlite3

DB ="book_Data.DB"
con = sqlite3.connect(DB)

cursor = con.cursor()

cursor.execute('''
       CREATE TABLE IF NOT EXISTS book_Data(
               id INTEGER PRIMARY KEY,
               name TEXT not null
               )

''')

con.commit()


def list_of_book():

    with sqlite3.connect(DB) as con:
             cursor = con.cursor()
             
    cursor.execute("SELECT * FROM  book_Data")
    books = cursor.fetchall()
    return books

def add_book(name):
     with sqlite3.connect(DB) as con:
         cursor = con.cursor()

     cursor.execute("INSERT INTO book_Data(name)VALUES(?)",(name,))
     con.commit()

def update_book(id ,name):

    with sqlite3.connect(DB) as con:
        cursor = con.cursor()

    cursor.execute("UPDATE book_Data SET id=? Where name=?",(id,name))
    print("Book data update ")
    con.commit()
    

def delete_book(id):

    with sqlite3.connect(DB) as con:
        cursor = con.cursor()

    cursor.execute("DELETE FROM book_Data WHERE id=?",(id,))
    print("Book data Delete")
    con.commit()


def main():
    while True:
        print('\n')
        print("Welcome to library ")
        print('\n')
        print('\n-----------------------------------------------')
        print("1 FOR list of all book ")
        print("2 ADD new book")
        print("3 Update book")
        print("4 Delete a book")
        print("5 Exists app")
        print('\n-----------------------------------------------')
        print('\n')

        user = input("Enter Your Choice --> ")

        if user =="1":
            list_of_book()

        elif user =="2":
            name = input("\nEnter your BOOK name --> ")
            add_book(name)

        elif user =="3":
            print('\n')
            id = int(input("Enter book id --> "))
            new_name = input("Enter book name --> ")
            update_book(id,new_name)
        
        elif user =="4":
            print('\n')
            id = int(input("Enter book id --> "))
            delete_book(id)
        
        elif user =="5":
            break

        else:
            print("Invalide TRY agian ")

    
    con.close()

if __name__ == "__main__":
    main()


