from product import Product
import sqlite3

if __name__ == "__main__" :
    try :
        product = Product("product.db")
        conn = sqlite3.connect(product.db_path)
        product.create_db(conn)
        # product.insert_product(conn)
        # product.insert_product(conn)
        # product.insert_product(conn)
        product.display_product(conn)
        # product.delete_product(conn)
        # product.display_product(conn)
        # product.update_price(conn)
        # product.display_product(conn)
        product.filter(conn)
    
    except Exception as e:
        print(e)

    finally :
        conn.close()

