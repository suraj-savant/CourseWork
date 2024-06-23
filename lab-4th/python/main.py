                                            # UNIT 1 PYTHON FUNDAMENTALS

# # ======= hello world program
# print(data [, sep=" "] [, end = "\n"])
# print("Hello World")

# # ==== end and sep arguments ====
# print(1,2,3,4,5, end=" The end\n")
# print(1,2,3,4,5, sep='|')

# # ==== taking input ====
# input([prompt])
# ip = input("Enter something : ")
# print(ip)

# Implicit and explicit continuation
# Divide statements after (), {}, operators
# print("hello world "
#       +"This is second line"
#     , end = "!")

# print()

# # Divide statements at anywhere using \
# print("Hello World \
# is second line"\
# , end = "!")

# # ==== round function ====
# distance, gallons = float(input("Enter the disatance : ")), float(input("Enter the gallons : "))
# mlg = round(distance / gallons, 2)
# print(mlg)

# # ==== string concatination ====
# str1, str2 = "Hello", "World"
# op1 = str1 + " " + str2



# modules


# # ==== comment ====
"""
This is a multiline comment
for x in "banana" :
    print(x)

"""

# # ==== condition statement ====
# marks = int(input("Enter the marks : "))
# grade = ""

# if marks >= 90 :
#     grade = "A"
# elif marks >= 80 :
#     grade = "B"
# elif marks >= 50 :
#     grade = "C"
# elif marks >= 35 :
#     grade = "D"
# else :
#     grade = "F"

# print(f"Marks : {marks} Grade : {grade}")




# # ======= Looping statements ========

# # while loop
# i = 1
# sum = 0
# while i <= 50 :
#     sum += i
#     i += 1
# print("Sum using while loop", sum)



# # # for loop
# for i in range(10) :
#     print(i, end=" ")

# # range() function

# # To loop through a set of code a specified number of times, we can use the range() function,
# # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# for x in range(6):
#   print(x, end = " ")
# print()

# # The range() function defaults to 0 as a starting value, however it is possible to  specify the starting value by 
# #   adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# for x in range(2, 6):
#   print(x, end = " ")
# print()

# # The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by 
# #   adding a third parameter: range(2, 30, 3):

# for x in range(0, 20, 2):
#   print(x, end = " ")
# print()

# # range() in descending order
# for x in range(9, 0, -1) :
#     print(x, end=" ")

# print("Sum using while loop", sum)

# # Sum using for loop

# sum = 0
# for i in range(1, 51) :
#     sum += i

# print("Sum using for loop", sum)




# # ==== functions ====

# # define a function

# def sum(num1 = 0, num2 = 0) :
#     print(f"{num1} + {num2} = {num1+num2}")

# # function call
# sum(10,20)
# sum(num2=20, num1=10)
# sum()

# # pass Statement
# # function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# #     put in the pass statement to avoid getting an error.
# def myfunction():
#   pass

# # function return multiple value
# def assign() :
#     return 2, 2*2

# num, multiple = assign()
# print(f"{num} {multiple}")


# # Calculator using functions
# 
# def add(num1, num2) :
#     return num1 + num2


# def substract(num1, num2) :
#     return num1 - num2


# def product(num1, num2) :
#     return num1 * num2


# def division(num1, num2) :  
#     if(num2 == 0) :
#         print("Cannot divide by zero")
#         return    
#     return num1 / num2


# def main(x, y, opr) :
#     result = 0
#     if(opr == '+') :
#             result = add(num1, num2)
#     elif (opr == '-') :
#         result = substract(num1, num2)
#     elif(opr == '*') :
#         result = product(num1 , num2)
#     elif(opr == '/') :
#         result = division(num1, num2)
#     else :
#         print("Invalid option")

#     print("Result :", str(num1), str(opr), str(num2) , "=", str(result))


# if __name__ == "__main__" :    

#     while True :
#         num1, num2, opr = int(input("Enter num1: ")), int(input("Enter num2: ")), input("Enter opr : ")

#         main(num1, num2, opr)

#         continue_again = int(input("Press Continue(1) Exit(0): "))

#         if(continue_again == 0) :
#             break

# # lambda
# sum = lambda a,b : a+b
# print(sum(10,20))


                                            # UNIT 2  HIGHER DATA STRUCTURE
# # ==== List ====
# Method	        Description
# append()	        Adds an element at the end of the list
# clear()	        Removes all the elements from the list
# copy()	        Returns a copy of the list
# count()	        Returns the number of elements with the specified value
# extend()	        Add the elements of a list (or any iterable), to the end of the current list
# index()	        Returns the index of the first element with the specified value
# insert()	        Adds an element at the specified position
# pop()	            Removes the element at the specified position else removes last element
# remove()	        Removes the item with the specified value
# reverse()	        Reverses the order of the list
# sort()	        Sorts the list

# list = [1,0,3,4,5]
# list.insert(0, 10)
# print(list)
# list.sort(reverse=True)
# print(list)

# # list initialisation with same number
# list = [0] * 5
# print(list)

# # list comprehension
# list = [i for i in range(5)]
# print(list)

# list = [1,2,3,10,4]
# list.reverse()
# list.sort(reverse=False)
# print(list)

# list = [even_num for even_num in range(50+1) if even_num % 2 == 0]
# print(list)


# Create a list with n elements and find their sum
# def main() :
#     n = int(input("Enter a number : "))
#     list = [x for x in range(1, n+1)]
#     print("list is : ", list)
#     sum = 0
#     for item in list :
#         sum += item
#     print("Sum is", sum)

# if __name__ == '__main__':
#     main()

# Access list elements
# list = [[1,2,3,4], ["one", "two", "three", "four"],[ "i", "ii", "iii", "iv"]]
# for l in list :
#     for item in l :
#         print(item, end= " ")
#     print()

# count = list.count([1,2,3,4])
# print(count)


# a, b = 10, 20
# print("Before swapping", a , b)
# a, b = b, a
# print("After swapping",a, b)


# list = ['a', 'A']
# list.sort()
# print(list)

# ==== Tuple ====
# Tuples are used to store multiple items in a single variable.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# fruits = ("apple", "banana", "orange", "apple")

# print(fruits)
# print(fruits.count("apple"))
# print(fruits.index("apple"))



# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# ==== dictionary ====
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Dictionaries cannot have two items with the same key
# Method	        Description
# clear()	        Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()	    Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()   	    Removes the last inserted key-value pair
# setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	        Updates the dictionary with the specified key-value pairs if key not present then updates
# values()	        Returns a list of all the values in the dictionary


# countries = {"CA": "Canada", "US": "United States", "MX": "Mexico"}
# print("IO" in countries)
# for key in countries.keys():
#     print(key)

# for values in countries.values() :
#     print(values)

# for items in countries.items() :
#     print(items)

# for key, value in countries.items() :
#     print(key, value)

# country_list = [["US", "United state"], ["MX", "MEXICO"]]
# countries = dict(country_list)
# print(dict)
# countries.update({"In":"India"})
# print(countries)
# print(len(countries))
# print(countries)

# countries.pop("US")
# print(countries)
# print(countries["CA"])
# print(countries.get("CA"))
# print(countries.get("IN"))

# # access key value
# for coutric in countries.items() :
#     print(f"{coutric[0]} : {coutric[1]} ")

# # access keya
# for key in countries :
#     print(f"{key} : {countries[key]}")

# # access dictionary values
# for value in countries.values() :
#     print(value,  end=" ")

# print(type(countries))

# print(countries)
# for country in countries :
#     print(country, ":", countries[country])


# countries = {"CA": "Canada", "US": "United States", "MX": "Mexico"}
# countries["In"] = "India"
# del countries["In"]
# print(countries)
# for country in countries.items() :
#     print(country)




# countries = {"CA": "Canada", "US": "United States", "MX": "Mexico"}

# for item in countries.values() :
#     print(item)

# countries = [[1,"ONE"], [2,"TWO"], [3, "THREE"] ]
# dictionary = dict(countries)
# print(dictionary)



# list = [
#         {'name':'python', 'code' : 'py21', 'num':22},
#         {'name':'se', 'code' : 'se21', 'num':30},
#         {'name':'java', 'code' : 'java21', 'num':32}        
#        ]

# for course in list :
#     print(len(course))



# # ==== string concatination ====
# str1, str2 = "Hello", "World"
# op1 = str1 + " " + str2


# # String methods
# str = "  hello, world  "
# print(str)
# print(str.split())
# print(str.capitalize())
# print(str.upper())
# print(str.lower())
# print(str.count('l'))
# print(str.isupper())
# print(str.strip())
# print(str.islower())


# datetime
# from datetime import datetime
# from datetime import date
# from datetime import time
# print(datetime.now())
# print(date.today())
# print(date(2003, 1, 10))
# print(time(12, 30, 15, 1256))
# print(datetime(2003, 2, 10, 23, 6, 30, 123456))





                                #UNIT 3 File Handling Exception and Working with database
# File handling in python

# outfile = open("test1.txt", 'w')
# outfile.write("Hello World")
# outfile.close()

# with open("test1.txt", "a") as outfile :
#     outfile.write("Written using file handler")

# with open("test1.txt", "a") as file :
#     file.write(" This is second line")

# with open("test1.txt") as file :
#     print(file.read())
# count =0
# with open("test1.txt") as myFile :
#     content = myFile.readlines()
    
#     for line in content :
#         count += len(line.split())
#         print(line, end="")
#     print("\nWord count", count)

# with open("test1.txt") as myFile :
#   print(myFile.readline(), end="")
#   print(myFile.readline(), end = "")
   

# with open("test1.txt", "r") as readFile :
#     content = readFile.readlines()
#     capital = [line.upper() for line in content]
#     with open("write.txt", "w") as writeFile :
        # writeFile.writelines(capital)
        # for line in content :
        #     writeFile.write(line.upper())   
   

# lines = ["This is first line", "This is second line", "Here is third one"]
# with open("test1.txt", "w") as file :
#     for line in lines :
#         file.write(line)

# with open("test1.txt", "w") as file :
#     file.writelines(lines)

# import csv
# data = [["Book1", "Author1"],["Book2", "Author2"], ["Book3", "Author3"]]

# with open("testfile.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     writer.writerow(["Book4", "Author4", "publisher4"])

# with open("testfile.csv", "r") as file :
#     reader = csv.reader(file)    
#     for row in reader :
#         print(row[0])

# Exception handling in python

# class OtherException(Exception) : 
#     def __str__(self) -> str:
#        return "This is user defined exception"
#     pass
    
# try :
#     with open("test1.txt") as myFile :
#         content = myFile.readline()             
#         while content :
#             print(content, end='')
#             content = myFile.readline()
# except FileNotFoundError as e :
#     print("File not found")  
# except ZeroDivisionError as e :
#     print("Cannot divide by zero")
# except Exception as e :
#     print("Other exception occurred", e)


# DATABASE CONNECTION IN PYTHON

# import sqlite3

# connection = sqlite3.connect("product.db")
# cur = connection.cursor()
# query = """
# CREATE TABLE  IF NOT EXISTS PRODUCT(
#     ID INT PRIMARY KEY,
#     NAME VARCHAR(20),
#     DESCRIPTION VARCHAR(50)
# );

# """

# cur.execute(query)

# insert = """
# INSERT INTO PRODUCT VALUES(1, "book", "THIS IS A PEN");
# INSERT INTO PRODUCT VALUES(2, "pen", "THIS IS A PEN");
# INSERT INTO PRODUCT VALUES(3, "pencil", "THIS IS A PEN");
# INSERT INTO PRODUCT VALUES(4, "pen", "THIS IS A PEN");
# INSERT INTO PRODUCT VALUES(5, "pen", "THIS IS A PEN");

# """


# for row in insert.split('\n') :
#     cur.execute(row)
# connection.commit();

# cur.execute("SELECT * FROM PRODUCT;")
# for record in cur.fetchmany(3) :
#     for data in record :
#         print(data, end = "  ")
#     print()

# print("\nConditional query \n")
# query = "SELECT NAME, DESCRIPTION FROM PRODUCT WHERE ID = ?"
# cur.execute(query, (4,))
# for item in cur.fetchall():
#     print(item[0], item[1])



   
                                            # UNIT 4 OOP IN PYTHON

# OBJECT ORIENTED PROGRAMMING(OOP)

# class Product :    
    
#     def __init__(self, name, price, discountPercent) :
#         self.name = name
#         self.price = price
#         self.discountPercent = discountPercent
#         pass


#     def getDiscountAmount(self) :
#         return (self.price * self.discountPercent) / 100
    
#     def getDiscountPrice(self) :
#         return self.price - self.getDiscountAmount()

#     def __str__(self) :
#         return f" Name : {self.name}\n Price : {self.price}\n Discount: {self.discountPercent} \n Discount Amt :  {self.getDiscountAmount()} \n Discount Price : {self.getDiscountPrice()}"
#         pass


# if __name__ == '__main__' :
#     catelog = [Product("pen", 5, 50), Product("BOOk", 20, 0)]
#     for product in catelog :
#         print(product, end='\n\n=============\n\n')

# plus = lambda num1, num2 : num1+num2; 
# ans = plus(1,2)
# print(ans)

# qty = float(input("QTY "))
# print(qty)

# class Calculator :
    
#     # constructor to initalise a object 
#     def __init__(self, num1, num2) -> None:
#         self.num1 = num1
#         self.num2 = num2

#     add = lambda self : self.num1 + self.num2

#     sub = lambda self : self.num1 - self.num2

#     multiply = lambda self : self.num1 * self.num2

# # program starts execution at here
# def main() :
#     num1,opr,num2 = int(input("Enter num1 : ")), input("Enter operator : "), int(input("Enter num2 : "))
#     if opr == '+' :
#         print()


# if __name__ == '__main__' :
#     main()



# class Product :
#     def __init__(self, name, price, qty) -> None:
#         self.name = name
#         self.price = price
#         self.qty = qty

#     def getDescription(self) :
#         return f"{self.name}  {self.price} {self.qty}"
    
# class Book(Product) :
#     def __init__(self, name, price, qty, author) -> None:
#         super().__init__(name, price, qty)
#         self.author = author
    
    
#     def getDescription(self) :
#         return super().getDescription() + "AUTHOR " + self.author
    
# b1 = Book("Book1", 200, 15, "Author1")
# print(b1.getDescription())

 
# class Person :
#     def __init__(self) -> None:
#         self.name = "Suraj"
#         pass

#     def printname(self) :
#         print(self.name)
#         pass

# class Student(Person) : 
#     def __init__(self) -> None:
#         super().__init__()
#         pass
    
    
#     def printname(self) :
#         print("hii")
#         pass

# student = Student()
# student.printname()



# GUI Programming
# from tkinter import *

# def increment() :
#     myInt.set(myInt.get() + 1)
#     pass

# def reset() :
    
#     myInt.set(0)
#     pass

# root = Tk()
# root.geometry("250x250")

# myInt = IntVar(0)


# Label(root, textvariable=myInt, fg="red").pack()
# Button(root, text="Increment", command= increment).pack()
# Button(root, text = "Reset", command=reset).pack()


# root.mainloop()

# self.tbox2 = Entry(root,font=("arial",12,"bold"),bg="white")
# self.tbox2.place(x=150,y=100)
# num1= int(self.tbox1.get())
#num2= int(self.tbox2.get())
#self.tbox3.insert(END, str(num1+num2))


# from tkinter import *
# from tkinter import messagebox

# def calculate(operation:str) :
#     num1, num2 = tbox1.get(), tbox2.get()
#     if not num1 or not num2 :
#         messagebox.showerror("Error", message="Please Enter num1 and num2")
#         return
        
#     num1 = int(num1)
#     num2 = int(num2)
#     answer = 0

#     if operation == "add" :
#         answer = num1+num2
#     elif operation == "sub" :
#         answer = num1-num2
#     elif operation == "mul" :
#         answer = num1*num2
#     elif operation == "div" :
#         answer = num1/num2
    
#     tbox3.config(state="normal")
#     tbox3.delete(0,END)
#     tbox3.insert(END, str(answer))
#     tbox3.config(state="disabled")
#     pass



# if __name__ == '__main__' :
#     root = Tk()
#     root.title("Calculator")
#     root.geometry("300x250")
#     Label(root, text="Enter first number :", foreground="blue").place(x=20,y=20)
#     Label(root, text="Enter second number :", foreground="blue").place(x=20,y=60)
#     Label(root, text="Result :", foreground="blue").place(x=20,y=100)

#     tbox1 = Entry(root,background="white")
#     tbox1.place(x=160, y=20)
#     tbox2 = Entry(root,background="white")
#     tbox2.place(x=160, y=60)
#     tbox3 = Entry(root,background="white")
#     tbox3.place(x=160, y=100)
#     tbox3.config(state = "disabled")

#     Button(text="Sum", background="blue", foreground="white", command=lambda:calculate("add")).place(x=20, y=140)
#     Button(text="Sub", background="blue", foreground="white", command=lambda:calculate("sub")).place(x=80, y=140)
#     Button(text="Multiply", background="blue", foreground="white", command=lambda:calculate("mul")).place(x=140, y=140)
#     Button(text="Divide", background="blue", foreground="white", command=lambda:calculate("div")).place(x=220, y=140)

#     root.mainloop()


from tkinter import *
from tkinter import messagebox

def calculate() :
    p, t, r = priciple.get(), time.get(), rate.get()
    
    try :
        p, t, r = float(p), float(t), float(r)
        interest = p*t*r/100
    except ValueError as e :
        messagebox.showerror("ERROR", "PLease Enter valid values")
    except Exception as e :
        messagebox.showerror("ERROR","Exception occured")

   
        
    
    intrest.config(state="normal")
    intrest.delete(0, END)
    intrest.insert(END,str(interest))
    intrest.config(state="disabled")
    print("Calculate") 


root = Tk()
root.title("Future Caculator")
root.geometry("250x250")

Label(root , text="PRINCIPLE : ", fg="blue").place(x=10, y=20)
Label(root , text="TIME : ", fg="blue").place(x=10, y=50)
Label(root , text="RATE : ", fg="blue").place(x=10, y=80)
Label(root , text="INTEREST : ", fg="blue").place(x=10, y=110)

priciple = Entry(root, bg="white")
priciple.place(x=100, y= 20)
time = Entry(root, bg="white")
time.place(x=100, y= 50)
rate = Entry(root, bg="white")
rate.place(x=100, y= 80)
intrest = Entry(root, bg="white")
intrest.config(state="disabled")
intrest.place(x=100, y= 110)

Button(root,text="CALCULATE", command=calculate).place(x = 80, y=140)

root.mainloop()
