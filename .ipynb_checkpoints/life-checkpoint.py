
def readGrid(filename):
    grid = []
    with open(filename) as f:
        w, h  = map(int, f.readline().split(maxsplit = 1))
        for y in range(h):
            grid.append([0] * w)
            
        for ind, line in enumerate(f):
            try:
                y, x = map(int, line.split(maxsplit = 1))

                if y < 0 or x < 0:
                    raise ValueError
            
            except ValueError:
                raise Exception(f"Invalid cell on line {ind + 2}")
                
            
            grid[y][x] = 1      
    return grid


def tick(grid):
    h, w = len(grid) -2, len(grid[0]) - 2
    nextgrid = []
    for y in range(h+2):
        nextgrid.append(bitarray(w+2))

    for y, row in enumerate(grid):
        if y==0 or y == h+2:
            continue

    for x, cell in enumerate (row):
        if x==0 or x == w+1:
            continue
        count = 0
        count += grid[y-1][x-1] 
        count += grid[y-1][x]
        count += grid[y-1][x+1]
        count += grid[y+1][x-1]
        count += grid[y+1][x]
        count += grid[y+1][x+1]
        count += grid[y][x-1]
        count += grid[y][x+1]
        
        nextgrid[y][x] = 1 if count == 3 or (count == 2 and cell) else 0
            
    return nextgrid

filename = 'matrix.txt'
grid = readGrid(filename)