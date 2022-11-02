# Node implementation
# All important code made by Jarod Najera 862179022
import copy
from operator import attrgetter

class Node:
    def __init__(self, key, depth):
        self.key = key
        self.depth = depth
        self.fn = 0
    
    def __eq__(self, right):
        if not isinstance(right, Node):
            return NotImplemented
        
        return self.key == right.key
    
    def Print_Key(self):
        print(self.key)

    # Move empty space (0) Up if possible
    def Up_Operator(self):
        child = copy.deepcopy(self.key)
        for x in range(3):
            for y in range(3):
                if child[x][y] == 0:
                    if x == 0:
                        return None
                    else:
                        temp = child[x-1][y]
                        child[x-1][y] = 0
                        child[x][y] = temp
                        return child
        return child

    # Move empty space (0) Down if possible 
    def Down_Operator(self):
        child = copy.deepcopy(self.key)
        for x in range(3):
            for y in range(3):
                if child[x][y] == 0:
                    if x == 2:
                        return None
                    else:
                        temp = child[x+1][y]
                        child[x+1][y] = 0
                        child[x][y] = temp
                        return child
        return child
    
    # Move empty space (0) Left if possible
    def Left_Operator(self):
        child = copy.deepcopy(self.key)
        for x in range(3):
            for y in range(3):
                if child[x][y] == 0:
                    if y == 0:
                        return None
                    else:
                        temp = child[x][y-1]
                        child[x][y-1] = 0
                        child[x][y] = temp
                        return child
        return child
    
    # Move empty space (0) Right if possible
    def Right_Operator(self):
        child = copy.deepcopy(self.key)
        for x in range(3):
            for y in range(3):
                if child[x][y] == 0:
                    if y == 2:
                        return None
                    else:
                        temp = child[x][y+1]
                        child[x][y+1] = 0
                        child[x][y] = temp
                        return child
        return child

    # Calculate f(n) using Misplaced Tiles Heuristic
    def Calc_Misplaced_fn(self):
        if self.key == None:
                self.fn = 1000000000
                return

        misplaced_tiles = 0
        if self.key[0][0] != 1 and self.key[0][0] != 0:
            misplaced_tiles += 1
        if self.key[0][1] != 2 and self.key[0][1] != 0:
            misplaced_tiles += 1
        if self.key[0][2] != 3 and self.key[0][2] != 0:
            misplaced_tiles += 1
        if self.key[1][0] != 4 and self.key[1][0] != 0:
            misplaced_tiles += 1
        if self.key[1][1] != 5 and self.key[1][1] != 0:
            misplaced_tiles += 1
        if self.key[1][2] != 6 and self.key[1][2] != 0:
            misplaced_tiles += 1
        if self.key[2][0] != 7 and self.key[2][0] != 0:
            misplaced_tiles += 1
        if self.key[2][1] != 8 and self.key[2][1] != 0:
            misplaced_tiles += 1
        
        # f(n) = h(n)
        self.fn = misplaced_tiles
    
    # Calculate f(n) using Manhattan Distance Heuristic
    def Calc_Manhattan_fn(self):
        if self.key == None:
            self.fn = 1000000000
            return
        
        misplaced_tiles = 0
        distance = 0
        if self.key[0][0] != 1 and self.key[0][0] != 0:
            misplaced_tiles += 1
            if self.key[0][0] == 2:
                distance += 1
            elif self.key[0][0] == 3:
                distance += 2
            elif self.key[0][0] == 4:
                distance += 1
            elif self.key[0][0] == 5:
                distance += 2
            elif self.key[0][0] == 6:
                distance += 3
            elif self.key[0][0] == 7:
                distance += 2
            elif self.key[0][0] == 8:
                distance += 3
        if self.key[0][1] != 2 and self.key[0][1] != 0:
            misplaced_tiles += 1
            if self.key[0][1] == 1:
                distance += 1
            elif self.key[0][1] == 3:
                distance += 1
            elif self.key[0][1] == 4:
                distance += 2
            elif self.key[0][1] == 5:
                distance += 1
            elif self.key[0][1] == 6:
                distance += 2
            elif self.key[0][1] == 7:
                distance += 3
            elif self.key[0][1] == 8:
                distance += 2
        if self.key[0][2] != 3 and self.key[0][2] != 0:
            misplaced_tiles += 1
            if self.key[0][2] == 1:
                distance += 2
            elif self.key[0][2] == 2:
                distance += 1
            elif self.key[0][2] == 4:
                distance += 3
            elif self.key[0][2] == 5:
                distance += 2
            elif self.key[0][2] == 6:
                distance += 1
            elif self.key[0][2] == 7:
                distance += 4
            elif self.key[0][2] == 8:
                distance += 3
        if self.key[1][0] != 4 and self.key[1][0] != 0:
            misplaced_tiles += 1
            if self.key[1][0] == 1:
                distance += 1
            elif self.key[1][0] == 2:
                distance += 2
            elif self.key[1][0] == 3:
                distance += 3
            elif self.key[1][0] == 5:
                distance += 1
            elif self.key[1][0] == 6:
                distance += 2
            elif self.key[1][0] == 7:
                distance += 1
            elif self.key[1][0] == 8:
                distance += 2
        if self.key[1][1] != 5 and self.key[1][1] != 0:
            misplaced_tiles += 1
            if self.key[1][1] == 1:
                distance += 2
            elif self.key[1][1] == 2:
                distance += 1
            elif self.key[1][1] == 3:
                distance += 2
            elif self.key[1][1] == 4:
                distance += 1
            elif self.key[1][1] == 6:
                distance += 1
            elif self.key[1][1] == 7:
                distance += 2
            elif self.key[1][1] == 8:
                distance += 1
        if self.key[1][2] != 6 and self.key[1][2] != 0:
            misplaced_tiles += 1
            if self.key[1][2] == 1:
                distance += 3
            elif self.key[1][2] == 2:
                distance += 2
            elif self.key[1][2] == 3:
                distance += 1
            elif self.key[1][2] == 4:
                distance += 2
            elif self.key[1][2] == 5:
                distance += 1
            elif self.key[1][2] == 7:
                distance += 3
            elif self.key[1][2] == 8:
                distance += 2
        if self.key[2][0] != 7 and self.key[2][0] != 0:
            misplaced_tiles += 1
            if self.key[2][0] == 1:
                distance += 2
            elif self.key[2][0] == 2:
                distance += 3
            elif self.key[2][0] == 3:
                distance += 4
            elif self.key[2][0] == 4:
                distance += 1
            elif self.key[2][0] == 5:
                distance += 1
            elif self.key[2][0] == 6:
                distance += 3
            elif self.key[2][0] == 8:
                distance += 1
        if self.key[2][1] != 8 and self.key[2][1] != 0:
            misplaced_tiles += 1
            if self.key[2][1] == 1:
                distance += 3
            elif self.key[2][1] == 2:
                distance += 2
            elif self.key[2][1] == 3:
                distance += 3
            elif self.key[2][1] == 4:
                distance += 2
            elif self.key[2][1] == 5:
                distance += 1
            elif self.key[2][1] == 6:
                distance += 2
            elif self.key[2][1] == 7:
                distance += 1

        # f(n) = h(n)
        self.fn = misplaced_tiles + distance
    
    """
    Since h(n) = 0, we do not have to consider it as both weight and
    the cost of expanding each node is the same
    """
    def Uniform_Cost_Search(self):
        # Goal State
        goal_state = [[1,2,3],
                    [4,5,6],
                    [7,8,0]]

        # Make queue and enqueue root
        nodes = [self]
        visited = [] # Prevent state repetition 

        expanded_nodes = 0 # Keep track of expanded nodes

        # Search
        while nodes:
            current_node = nodes.pop(0)

            # Success
            if current_node.key == goal_state:
                return expanded_nodes, current_node.depth
            
            # Uncomment for debugging
            # print(current_node.key, current_node.depth)
            
            # Add current_node to visited[]
            visited.append(current_node)

            # Add Possible Moves to nodes[]
            up = Node(current_node.Up_Operator(), current_node.depth+1)
            down = Node(current_node.Down_Operator(), current_node.depth+1)
            left = Node(current_node.Left_Operator(), current_node.depth+1)
            right = Node(current_node.Right_Operator(), current_node.depth+1)

            if up.key != None and up not in visited:
                nodes.append(up)
            
            if down.key != None and down not in visited:
                nodes.append(down)
            
            if left.key != None and left not in visited:
                nodes.append(left)
            
            if right.key != None and right not in visited:
                nodes.append(right)
    
            expanded_nodes += 1
        
        # Failure
        return expanded_nodes, -1

    def A_Misplaced_Tiles(self):
        # Goal State
        goal_state = [[1,2,3],
                    [4,5,6],
                    [7,8,0]]

        # Make queue and enqueue root
        nodes = [self]
        visited = [] # Prevent state repetition 
        trace = list()

        expanded_nodes = 0 # Keep track of expanded nodes
        max_queue_size = 0

        # Search
        while nodes:
            other = []
            current_node = nodes.pop(0)

            # Success
            if current_node.key == goal_state:
                return expanded_nodes, current_node.depth
            
            # Uncomment for debugging
            # print(current_node.key, current_node.depth)
            
            # Add current_node to visited[]
            visited.append(current_node)

            # Add Best Possible Move to nodes[]
            up = Node(current_node.Up_Operator(), current_node.depth+1)
            down = Node(current_node.Down_Operator(), current_node.depth+1)
            left = Node(current_node.Left_Operator(), current_node.depth+1)
            right = Node(current_node.Right_Operator(), current_node.depth+1)

            up.Calc_Misplaced_fn()
            down.Calc_Misplaced_fn()
            left.Calc_Misplaced_fn()
            right.Calc_Misplaced_fn()

            moves = [up, down, left, right]

            best_fn = min(up.fn, down.fn, left.fn, right.fn)
            
            for move in moves:
                if move.fn == best_fn:
                    if move not in visited:
                        nodes.append(move)
                elif move.key != None and move not in visited:
                    # Other nodes to check
                    other.append(move)
            other.sort(key=attrgetter('fn'))
            trace += other

            if len(nodes) == 0:
                nodes.append(trace.pop(0))

            expanded_nodes += 1
        
        return expanded_nodes, -1
    
    def A_Manhattan_Distance(self):
        # Goal State
        goal_state = [[1,2,3],
                    [4,5,6],
                    [7,8,0]]

        # Make queue and enqueue root
        nodes = [self]
        visited = [] # Prevent state repetition 
        trace = list()

        expanded_nodes = 0 # Keep track of expanded nodes
        max_queue_size = 0

        # Search
        while nodes:
            other = []
            current_node = nodes.pop(0)

            # Success
            if current_node.key == goal_state:
                return expanded_nodes, current_node.depth
            
            # Uncomment for debugging
            # print(current_node.key, current_node.depth)
            
            # Add current_node to visited[]
            visited.append(current_node)

            # Add Best Possible Move to nodes[]
            up = Node(current_node.Up_Operator(), current_node.depth+1)
            down = Node(current_node.Down_Operator(), current_node.depth+1)
            left = Node(current_node.Left_Operator(), current_node.depth+1)
            right = Node(current_node.Right_Operator(), current_node.depth+1)

            up.Calc_Manhattan_fn()
            down.Calc_Manhattan_fn()
            left.Calc_Manhattan_fn()
            right.Calc_Manhattan_fn()

            moves = [up, down, left, right]

            best_fn = min(up.fn, down.fn, left.fn, right.fn)
            
            for move in moves:
                if move.fn == best_fn:
                    if move not in visited:
                        nodes.append(move)
                elif move.key != None and move not in visited:
                    # Other nodes to check
                    other.append(move)
            other.sort(key=attrgetter('fn'))
            trace += other

            if len(nodes) == 0:
                nodes.append(trace.pop(0))

            expanded_nodes += 1
        
        return expanded_nodes, -1