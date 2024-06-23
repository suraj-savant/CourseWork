import sqlite3
class Product :
    def __init__(self, db_path : str) -> None:
        self.db_path = db_path
        pass

    def create_db(self, conn : sqlite3.Connection) :
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS PRODUCT(
        PRODUCTID VARCHAR(10) PRIMARY KEY,
        NAME VARCHAR(20) NOT NULL,
        QUANTITY INT NOT NULL,
        PRICE REAL NOT NULL
        );
        """
        cursor.execute(query)
        conn.commit()

    def insert_product(self, conn:sqlite3.Connection) :
        id, name, qty, price = input("Enter id name qty price of product : ").split()
        cursor = conn.cursor()
        query = """
        INSERT INTO PRODUCT VALUES(?,?,?,?);
        """
        cursor.execute(query, (id, name, int(qty), int(price)))
        conn.commit()

    def display_product(self, conn : sqlite3.Connection) :
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PRODUCT;")
        print("\nProduct details are : ")
        for product in cursor.fetchall() :
            for details in product :
                print(details, end = " ")
            print()
    
    def delete_product(self, conn : sqlite3.Connection) :
        cursor = conn.cursor()
        id = input("Enter product id to delete product ")
        cursor.execute("DELETE FROM PRODUCT WHERE PRODUCTID = ?", (id,))
        conn.commit()

    def filter(self, conn : sqlite3.Connection) :
        cursor = conn.cursor()
        cursor.execute("SELECT NAME FROM PRODUCT WHERE QUANTITY <= 30")
        for names in cursor.fetchall() :
            print(names[0])
        conn.commit()



    def update_price(self, conn : sqlite3.Connection) :
        cursor = conn.cursor()
        conn.execute("UPDATE PRODUCT SET PRICE = PRICE+(PRICE * 0.1) WHERE QUANTITY < 50")
        conn.commit()


    

    
