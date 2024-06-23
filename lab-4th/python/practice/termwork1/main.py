
def enqueue(queue : list) :
    element = int(input("Enter enqueue element :"))
    queue.append(element)
    pass

def dequeue(queue :list) :
    element = queue.pop(0)
    print("The dequeu element :", element)
    pass

def display(queue : list) :
    print("\nQueue Elements are :", end = " ")
    for elemnt in queue :
        print(elemnt, end = " ")
    pass

def main() :
    queue = []
    while True :
        choice = int(input("\nEnter the choice (1)Enqueue (2)Dequeue (3)Display (4)Exit : "))
        if(choice == 1) :
            enqueue(queue)
        elif(choice == 2) :
            dequeue(queue)
        elif(choice == 3) :
            display(queue)
        else :
            print("Program Terminated")
            return



if __name__ == "__main__" :
    main()