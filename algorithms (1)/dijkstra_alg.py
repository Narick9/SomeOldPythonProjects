

def dijkstra_alg(graph, start, end):
    processed = []
    costs = {}
    parents = {}
    
    for point in graph:
        if point == start:
            costs[start] = 0
        else:
            costs[point] = float("inf")
    
    point = start
    while point:
        for neigh in list(graph[point].keys()):
            cost = costs[point] + graph[point][neigh]
            if cost < costs[neigh]:
                costs[neigh] = cost
                parents[neigh] = point
        processed.append(point)
        point = new_point(graph, costs, processed)
        
    return costs[end]


def new_point(graph, costs, processed):
    low_cost = float("inf")
    low_cost_point = None
    for point in list(graph.keys()):
        if point in list(costs.keys()) and point not in processed:
            if costs[point] < low_cost:
                low_cost = costs[point]
                low_cost_point = point
    return low_cost_point

                
graph_orig = {"start": {"a": 6, "b": 2},
         "a": {"end": 1},
         "b": {"a": 3, "end": 5},
         "end": {}}

graph_a = {"start": {"a": 5, "c": 2},
           "a": {"b": 4, "d": 2},
           "b": {"d": 6, "end": 3},
           "c": {"a": 8, "d": 7},
           "d": {"end": 1},
           "end": {}}

graph_b = {"start": {"a": 10},
           "a": {"b": 20},
           "b": {"end": 30, "c": 1},
           "c": {"a": 1},
           "end": {}}

graph_c = {"start": {"a": 2, "b": 2},
           "a": {"end": 2, "c": 2},
           "c": {"b": -1, "end": 2},
           "b": {"a": 2},
           "end": {}}

graph_great_travel = {"Marin": {"San-Francisco": 10},
                      "San-Francisco": {"Berkly": 14},
                      "Berkly": {"Fremont": 31},
                      "Fremont": {"Palo-Alto": 16},
                      "Palo-Alto": {}}

print("a:", graph_a)
print("a:", dijkstra_alg(graph_a, "start", "end"))
print("\nb:", graph_b)
print("b:", dijkstra_alg(graph_b, "start", "end"))
print("\nc:", graph_c)
print("c:", dijkstra_alg(graph_c, "start", "end"))
print("\ngreat_travel:", graph_great_travel)
print("great_travel:", dijkstra_alg(graph_great_travel, "Marin", "Palo-Alto"))

if __name__ == "__main__":
    print()
    print("Это всего лишь алгоритм!")
    print("Вся его суть в коде")
    input("Press enter to continue...")
