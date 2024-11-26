from search import astar_search, breadth_first_graph_search, depth_first_graph_search

def run_algorithm(problem, algorithm):
    if algorithm == 'A*':
        return astar_search(problem)
    elif algorithm == 'Breadth-First Search':
        return breadth_first_graph_search(problem)
    elif algorithm == 'Depth-First Search':
        return depth_first_graph_search(problem)
    return None
