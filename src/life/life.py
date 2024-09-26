from bitarray import bitarray

class Life:
    """
    A class to simulate Conway's Game of Life using a grid.

    Attributes:
    -----------
    filename : str
        The name of the file containing the initial grid configuration.
    grid : list
        The 2D grid that represents the game board, initialized from the file.

    Methods:
    --------
    __init__(filename)
        Initializes the grid and reads the configuration from the file.
    tick(n)
        Advances the simulation by 'n' generations.
    """
    
    def __init__(self, filename):
        """
        Initializes the Life class with a grid read from a file.

        Parameters:
        -----------
        filename : str
            The name of the file containing the width, height, and initial live cells of the grid.
            The file should start with two integers (width, height), followed by the coordinates 
            of live cells in subsequent lines.

        Raises:
        -------
        Exception:
            Raises an exception if any invalid coordinates for live cells are found in the file.
        """
        self.filename = filename
        self.grid = []
        with open(filename) as f:
            self.w, self.h  = map(int, f.readline().split(maxsplit=1))
            
            # Initialize a padded grid (adding 2 extra rows/columns for boundary checks)
            for y in range(self.h + 2):
                self.grid.append([0] * (self.w + 2))
                
            # Reading live cells from the file and placing them on the grid
            for ind, line in enumerate(f):
                try:
                    y, x = map(int, line.split(maxsplit=1))
    
                    if y < 0 or x < 0:
                        raise ValueError
                
                except ValueError:
                    raise Exception(f"Invalid cell on line {ind + 2}")        
                
                # Place the live cell in the grid
                self.grid[y+1][x+1] = 1      
                
    
    def tick(self, n):
        """
        Advances the game by 'n' generations, updating the grid state for each generation.

        Parameters:
        -----------
        n : int
            The number of generations to advance the simulation.

        Functionality:
        --------------
        - For each generation, the grid is updated based on the number of neighboring live cells.
        - Padding is used around the grid to simplify boundary condition handling.
        - The count of live neighbors is calculated for each cell, and the rules of Conway's Game of Life are applied:
            * A live cell with 2 or 3 neighbors survives.
            * A dead cell with exactly 3 neighbors becomes a live cell.
            * All other cells either die or remain dead.
        """
        for i in range(n):
            for y, row in enumerate(self.grid[1:-1]):
                y2 = y + 2  # To look two rows ahead (bottom boundary of 3x3 block)
                curr = [0] * (self.w + 2)  # Initialize current row for the next generation            
                for x, cell in enumerate(row[1:-1]):  # Loop through each cell, skipping boundaries
                    # Count the live neighbors
                    count = (
                        self.grid[y][x] + self.grid[y][x+1] + self.grid[y][x+2] +  # Top row
                        row[x] + row[x+2] +  # Left and right neighbors
                        self.grid[y2][x] + self.grid[y2][x+1] + self.grid[y2][x+2]  # Bottom row
                    )
                    # Apply Game of Life rules
                    curr[x+1] = 1 if count == 3 or (count == 2 and cell) else 0
                if y > 0:
                    # Update the grid with the previous row
                    self.grid[y] = prev
                prev = curr
            # Update the last row after loop ends
            self.grid[y+1] = curr
