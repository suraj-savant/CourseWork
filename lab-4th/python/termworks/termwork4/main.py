from product import ProductClass
import sqlite3

def main() :
    try :
        db = ProductClass("./product.db")
        conn = sqlite3.connect(db.dbName)
        db.createDb(conn)

        while True :
            option = int(input("Enter (1)Insert (2)DisplayAll (3)Delete (4)Update (5)Filter (6) Exit\nEnter option >> "))
            if(option == 1) :
                db.dbInsert(conn)
            elif(option == 2) :
                db.displayAll(conn)
            elif(option == 3) :
                db.delete(conn)
            elif(option == 4) :
                db.update(conn)
            elif(option == 5) :
                db.displayNames(conn)     
            elif(option == 6) :
                return   
            else :
                print("Enter valid option")
    except :
        print("DB ERROR")

    finally :
        conn.close()


if __name__ == '__main__' :
    main()
   