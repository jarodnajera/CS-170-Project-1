# main.py
# All important code made by Jarod Najera 862179022
from Node import Node

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
    search = int(input("Enter 0 for Uniform Cost Search, 1 for A* Manhattan Distance, 2 for A* Misplaced Tile:\n"))

    expanded, depth = None, None
    if search == 0:
        expanded, depth = root.Uniform_Cost_Search()
    elif search == 1:
        expanded, depth = root.A_Misplaced_Tiles()

    print(f'It took {expanded} nodes to expand to find the solution at a depth of {depth}')

    
