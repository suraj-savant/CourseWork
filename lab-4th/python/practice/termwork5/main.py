

class Customer :
    def __init__(self, name, email) -> None:
        self.__name = name
        self.__email = email
        self.__orders = []

    def get_name(self):
        return self.__name
    
    def get_email(self) :
        return self.__email
    
    def get_ordes(self) :
        return self.__orders
    
    def place_order(self,order) :
        self.__orders.append(order)

class Order :
    def __init__(self, id, products : list) -> None:
        self.__id = id
        self.products = products
        
    def total_price(self) :
        total = 0
        for product in self.products :
            total += product.get_product_price()

        return total
    
    def get_id(self) :
        return self.__id


class Product :
    def __init__(self, name, price) -> None:
        self.__name = name
        self.__price = price

    def get_product_name(self):
        return self.__name
    
    def get_product_price(self) :
        return self.__price
    
if __name__ == "__main__" :
    customer = Customer("Ravi", "ravi@gmail.com")

    product1 = Product("Product1", 250)
    product2 = Product("Product2",150)

    order1 = Order(1,[product1, product2])
    customer.place_order(order1)

    print("Customer Details ")
    print(customer.get_name())
    print(customer.get_email())

    print("Orders")
    for order in customer.get_ordes() :
        for product in order.products :
            print(product.get_product_name(), product.get_product_price())
        print("Total ", order.total_price())
        