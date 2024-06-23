class Customer:
    def __init__(self, name, email):
        self.__name = name  # Customer's name (private)
        self.__email = email  # Customer's email (private)
        self.orders = []  # List to store customer's orders

    def place_order(self, order):
        self.orders.append(order)  # Add the given order to the customer's list of orders

    def get_orders(self):
        return self.orders  # Return the list of customer's orders

    def get_name(self):
        return self.__name  # Getter method to access the private name attribute

    def get_email(self):
        return self.__email  # Getter method to access the private email attribute


class Order:
    def __init__(self, order_id, products):
        self.__order_id = order_id  # Order ID (private)
        self.products = products  # List of products in the order

    def get_order_id(self):
        return self.__order_id  # Getter method to access the private order_id attribute

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.get_price()
        return total_price


class Product:
    def __init__(self, name, price):
        self.__name = name  # Product name (private)
        self.__price = price  # Product price (private)

    def get_name(self):
        return self.__name  # Getter method to access the private name attribute

    def get_price(self):
        return self.__price  # Getter method to access the private price attribute

# Creating objects
customer1 = Customer("Pari", "pari@gmail.com")

product1 = Product("Samsung", 500)
product2 = Product("Nokia", 1500)
product3 = Product("Apple", 2500)


# Placing an order
order1 = Order(1, [product1, product2])
customer1.place_order(order1)

order2 = Order(2, [product1, product3])
customer1.place_order(order2)



# Accessing customer information using the getter methods
print("Customer details : ")
print("Customer Name:", customer1.get_name())
print("Customer Email:", customer1.get_email())

# Accessing order information
orders = customer1.get_orders()
for order in orders:
    print("Order ID:", order.get_order_id())
    print("Products:")
    for product in order.products:
        print(product.get_name(), "Rs", product.get_price())
    print("Total price:", order.get_total_price())