# main.py
# All important code made by Jarod Najera 862179022
from Node import Node
import timeit

# Driver Code
if __name__ == '__main__':
    # Initialize Start State
    start_state = []
    start_state.append([int(x) for x in input('Enter 1st row:\n').split(' ')])
    start_state.append([int(x) for x in input('Enter 2nd row:\n').split(' ')])
    start_state.append([int(x) for x in input('Enter 3rd row:\n').split(' ')])

    # Create Node for Start State
    root = Node(start_state, 0)

    # Ask for method
    search = int(input("Enter 0 for Uniform Cost Search, 1 for A* Misplaced Tile, 2 for A* Manhattan Distance:\n"))

    expanded, depth = None, None

    # Start search
    if search == 0:
        print('Using Uniform Cost Search...')
        start = timeit.default_timer()
        expanded, depth = root.Uniform_Cost_Search()
        stop = timeit.default_timer()
    elif search == 1:
        print('Using A* Misplaced Tile...')
        start = timeit.default_timer()
        expanded, depth = root.A_Misplaced_Tiles()
        stop = timeit.default_timer()
    else:
        print('Using A* Manhattan Distance...')
        start = timeit.default_timer()
        expanded, depth = root.A_Manhattan_Distance()
        stop = timeit.default_timer()


    print(f'It took {expanded} nodes to expand to find the solution at a depth of {depth}. Time: {stop-start}')

    
