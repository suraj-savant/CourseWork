"""
Develop a program to implement queue

"""

def addQ(queue): 
    data = int(input("Enter the item to add : "))
    queue.append(data)
    pass

def delQ(queue:list):
    if len(queue) < 1 :
        print("Queue is empty")
        return
    queue.pop(0)
    pass


def dispQ(queue):
    if len(queue) < 1 :
        print("Queue is empty")
        return
    
    for item in queue :
        print(item, end=" ")
    print("\n")
    pass


def main():
    queue = []    

    while True :
      
        choice = int(input("\nOptions (1)Add (2)Delete (3)Display (4)Exit\nEnter your choice : "))
        if choice == 1 :            
            addQ(queue)
        elif choice == 2 :
            delQ(queue)
        elif choice == 3 :
            dispQ(queue)
        elif choice == 4 :
            return
        else :
            print("Invalid option")
    

if __name__ == '__main__' :
    main()