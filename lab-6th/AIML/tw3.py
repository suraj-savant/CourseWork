import heapq

def astar(graph, start, goal):
    open_list = [(0, start)]
    parents, g_costs = {}, {node: float('inf') for node in graph}
    g_costs[start] = 0
    f_costs = {node: float('inf') for node in graph}
    f_costs[start] = graph[start][1]
    iteration = 0
    
    while open_list:
        current_f_cost, current = heapq.heappop(open_list)
        iteration += 1
        
        if current == goal:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            final_cost = g_costs[goal]
            print(f"\nFinal Cost: {final_cost}")
            return path, final_cost
        
        for neighbor, move_cost in graph[current][0].items():
            new_cost = g_costs[current] + move_cost
            if new_cost < g_costs[neighbor]:
                parents[neighbor], g_costs[neighbor] = current, new_cost
                f_costs[neighbor] = new_cost + graph[neighbor][1]
                heapq.heappush(open_list, (f_costs[neighbor], neighbor))
        
        print(f"\nIteration {iteration}:")
        print("Current Path:", reconstruct_path(parents, start, current))
        print(f"Evaluation Function Value for {current}: {f_costs[current]}")

    return [], float('inf')

def reconstruct_path(parents, start, node):
    path = [node]
    while node in parents:
        node = parents[node]
        path.append(node)
    path.reverse()
    return path

graph = {
    'A': [{'B': 5, 'C': 10}, 10],
    'B': [{'D': 5, 'E': 5}, 7],
    'C': [{'F': 5}, 7],
    'D': [{'G': 10}, 3],
    'E': [{'G': 7}, 2],
    'F': [{'G': 8}, 1],
    'G': [{}, 0]
}

start_node = 'A'
goal_node = 'G'

print("\nA* Search Path:")
path, cost = astar(graph, start_node, goal_node)
print("Final Path:", path)
print("Total Cost:", cost)
