# Node implementation
# All important code made by Jarod Najera 862179022
import copy

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
        
        # f(n) = h(n) + g(n)
        self.fn = misplaced_tiles + self.depth
    
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
            
            print(current_node.key, current_node.depth)
            
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
        trace = []

        expanded_nodes = 0 # Keep track of expanded nodes

        # Search
        while nodes:
            current_node = nodes.pop(0)

            # Success
            if current_node.key == goal_state:
                return expanded_nodes, current_node.depth
            
            print(current_node.key, current_node.depth)
            
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
            print('Up f(n): ', up.fn)
            print('Down f(n): ', down.fn)
            print('Left f(n): ', left.fn)
            print('Right f(n): ', right.fn)

            moves = [up, down, left, right]

            best_fn = min(up.fn, down.fn, left.fn, right.fn)
            
            for move in moves:
                if move.fn == best_fn:
                    if move not in visited:
                        nodes.append(move)
                elif move.key != None:
                    # Other nodes to check
                    other = []
                    other.append(move)
            other.sort(key=lambda x: x.fn)
            trace += other

            if not nodes:
                nodes += trace

            expanded_nodes += 1
        

        
        return expanded_nodes, -1