# from contextlib import closing
import sqlite3

class ProductClass :
    def __init__(self, dbName) :  
        self.dbName = dbName     
        pass

    # Create databse
    def createDb(self, conn) :
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS PRODUCT(
            PID INTEGER PRIMARY KEY, 
            NAME TEXT,
            QUANTITY INTEGER,
            PRICE INTEGER
        );
        
        """
        cursor.execute(query)
        conn.commit()

    # INSERTS PRODUCT INTO DATABSE
    def dbInsert(self, conn) :
        cursor = conn.cursor()
        num = int(input("Enter the number of products you want to insert : "))
        for i in range(num) :
            pId, name, qty, price = int(input("Enter PID : ")), input("Enter product name : "), int(input("Enter Quantity : ")), int(input("Enter Price : "))
            recordObj = (pId, name, qty, price)
            cursor.execute("INSERT INTO PRODUCT VALUES (?,?,?,?)", recordObj)
        conn.commit()

    # DISPLAY ALL PRODUCTS DETAILS
    def displayAll(self, conn) :
        cursor = conn.cursor()
        rsp = cursor.execute("SELECT * FROM PRODUCT;")
        print("\nPRODUCT DETAILS ARE")
        print("\nId Name Qty Price")
        for row in rsp.fetchall() :
            for data in row :
                print(data, end = " ")
            print()
        print()

    # DELETES PRODUCT WITH GIVEN PRODUCT ID
    def delete(self, conn) :
        cur = conn.cursor()
        pId = int(input("Enter product Id : "))
        cur.execute("DELETE FROM PRODUCT WHERE PID = ?", (pId,))
        conn.commit()
    
    # INCREASES PRICE BY 10%
    def update(self, conn) :
        cur = conn.cursor()
        cur.execute("UPDATE PRODUCT SET PRICE = PRICE + (PRICE*0.1) WHERE PRICE < 50")
        conn.commit()
    
    # DISPLAYS ALL PRODUCTS WHOSE QUANTITY IS LESS THAN 40
    def displayNames(self, conn) :
        cur = conn.cursor()
        cur.execute("SELECT NAME FROM PRODUCT WHERE QUANTITY<40")
        for data in cur.fetchall() :
            print(data[0])


    
