def dfs(grid, row, col):
    grid[row][col] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
            dfs(grid, new_row, new_col)

def find_islands(grid):
    islands = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                dfs(grid, row, col)
                islands += 1
                
    return islands
    
if __name__ == "__main__":
    n = int(input())  
    r = int(input())  
    
    grid = []
    
    for i in range(n):
        grid.append([int(i) for i in input().split()][:r])
        
    print(find_islands(grid))
