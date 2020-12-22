def clusterCount(numOfRows, grid):
    #Write your code here
    grid = process_grid(grid)
    adjacency_map = create_adjacency_map(grid)
    marked = [[0 for i in range(len(j))] for j in grid]
    output = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            start_node = (r,c)
            if not marked[r][c]:
                dfs(start_node, adjacency_map, marked)
                output += 1
    return output 

                
    

def dfs(start_node, adjacency_map, marked):
    r = start_node[0]
    c = start_node[1]
    fringe = []
    fringe.append(start_node)
    marked[r][c] = 1 
    while fringe:
        node = fringe.pop()
        
        for neighbor in adjacency_map[node]:
            row = neighbor[0]
            column = neighbor[1]
            if marked[row][column] == 0:
                fringe.append(neighbor)
                marked[row][column] = 1
    return 
            
    

def create_adjacency_map(grid):
    output = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            output[(r,c)] = get_valid_neighbors(r,c, grid)
    return output
    

def get_valid_neighbors(r,c, grid):
    curr_value = grid[r][c]
    output = []
    if r - 1 >= 0 and grid[r-1][c]  == curr_value:
        output.append((r-1, c))
        
    if r + 1 < len(grid) and grid[r+1][c] == curr_value:
        output.append((r+1,c))
    if c - 1 >= 0 and grid[r][c -1] == curr_value:
        output.append( (r, c-1))
    
    if c + 1 < len(grid[0]) and grid[r][c+1] == curr_value:
        output.append( (r, c + 1))
        
    return output
    
def process_grid(grid):
    output = []
    for row in grid:
        curr = []
        for i in row:
            curr.append(i)
        output.append(curr)
    return output
            
            
