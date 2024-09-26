from bitarray import bitarray

def readGrid(filename):
    grid = []
    with open(filename) as f:
        w, h  = map(int, f.readline().split(maxsplit = 1))
        for y in range(h+2):
            grid.append(bitarray(w+2))
            
        for ind, line in enumerate(f):
            try:
                y, x = map(int, line.split(maxsplit = 1))

                if y < 0 or x < 0:
                    raise ValueError
            
            except ValueError:
                raise Exception(f"Invalid cell on line {ind + 2}")
                
            
            grid[y+1][x+1] = 1      
    return grid


def tick(grid):
    h, w = len(grid) - 2, len(grid[0]) - 2
    
    for y, row in enumerate(grid[1:-1]):
        y2 = y+2
        curr = [0] * (w + 2)
        
        for x, cell in enumerate(row[1:-1]):                
            count = grid[y][x] + grid[y][x+1] + grid[y][x+2] + row[x] + row[x+2] + grid[y2][x] + grid[y2][x+1] + grid[y2][x+2]
            
            curr[x + 1] = 1 if count == 3 or (count == 2 and cell) else 0
        if y < 0:
            grid[y] = prev
        prev = curr
    
    grid[y + 1] = curr


filename = 'matrix.txt'
grid = readGrid(filename)