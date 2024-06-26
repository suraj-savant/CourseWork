SuccList = {
    'S': [['A', 12], ['B',4]],
    'A': [['C', 7], ['D',3]],
    'B': [['E', 8], ['F',2]],
    'E':[['H',4]],
    'F':[['I',9], ['G', 0]]
}

start = input("Enter start ").upper()
goal = input("Enter goal ").upper()

def best_first_search():
    open = [[start, 13]]
    closed = []
    is_search_completed = False

    i = 1

    while open and not is_search_completed:
        print(f"\n\nStep {i}")
        N = open.pop(0)

        print(f"Node {N}")
        if goal == N[0]:
            is_search_completed = True
            closed.append(N)
        else:
            closed.append(N)
            child = SuccList.get(N[0], [])
            open = [x for x in child if x not in open and x not in closed] + open
            open.sort(key=lambda x : x[1])
        print(f"Open {open}")
        print(f"Closed {closed}")
        i+=1
    
    return closed, is_search_completed

path, result = best_first_search()

print(f"\nResult\nPathv{path}\nResult {result}")