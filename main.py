import sqlite3

con = sqlite3.connect("book_Data.DB")

cursor = con.cursor()

cursor.execute('''
       CREATE TABLE IF NOT EXISTS book_Data(
               id INTEGER PRIMARY KEY,
               name TEXT not null
               )

''')

con.commit()


def list_of_book():
    cursor.execute("SELECT * FROM  book_Data")
    for row in cursor.fetchall():
        print('\n')
        print(f"ID = {row[0]} , NAME = {row[1]}")
    con.commit()

def add_book(name):
    cursor.execute("INSERT INTO book_Data(name)VALUES(?)",(name,))
    con.commit()

def update_book(id ,name):
    cursor.execute("UPDATE book_Data SET name=? Where id=?",(name,id))
    print("Book data update ")
    con.commit()
    

def delete_book(id):
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


