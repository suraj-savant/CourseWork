import csv

def add_book() :
    # books = [
    #     ["book001", "title1", "author1", 250],        
    #     ["book001", "title1", "author1", 250],        
    #     ["book001", "title1", "author1", 250],
    #     ["book001", "title1", "author1", 250],
    #     ["book001", "title1", "author1", 250]
    # ]
    books = []
    count = int(input("Enter the number of books you want to insert"))
    for i in range(count) :
        id, title, author, price = input(f"Enter the id, title, author, price of {i+1}th book").split()
        books.append([id, title, author, price])

    with open("book.csv", "w") as book_file :
        writer = csv.writer(book_file, lineterminator="\n")
        writer.writerows(books)


def seach_book_by_title() :
    title = input("Enter title name : ")
    with open("book.csv", "r") as book_file :
        reader = csv.reader(book_file)
        for book_detail in reader :
            if(book_detail[1] == title) :
                for info in book_detail :
                    print(info, end = " ")
                print()


def seach_book_by_author() :
    author = input("Enter author name : ")
    with open("book.csv", "r") as book_file :
        reader = csv.reader(book_file)
        for book_detail in reader :
            if(book_detail[2] == author) :
                for info in book_detail :
                    print(info, end = " ")
                print()



def seach_book_by_price() :
    price = int(input("Enter price name : "))
    with open("book.csv", "r") as book_file :
        reader = csv.reader(book_file)
        for book_detail in reader :
            if(int(book_detail[3]) <=  price) :
                for info in book_detail :
                    print(info, end = " ")
                print()


def main() :
    menu = {1:add_book, 2: seach_book_by_title, 3: seach_book_by_author, 4: seach_book_by_price }
    while True :
        choice = int(input("\nEnter 1:add_book, 2: seach_book_by_title, 3: seach_book_by_author, 4: seach_book_by_price 5:exit\nEnter option > "))
        if choice == 5 :
            return
        
        menu[choice]()
    pass


if __name__ == "__main__" :
    main()