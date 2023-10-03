class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = []
        
        for i in range(width):
            row = []
            for j in range(height):
                row.append(None)
                print(row)
            self.array.append(row)
            print(self.array)
            
    def in_bounds(self, x, y):
        return (x >= self.width >= 0 or y >= self.height >= 0)
    
    
    def get(self, x, y):
        if(self.in_bounds(x,y)):
            return 'error'
        
        current_value = self.array[x][y]
        return current_value
    
    def set(self, x, y, value):
        if(self.in_bounds(x,y)):
            return 'error'
        self.array[x][y] = value
        print(self.array)
    
    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'
    
    def __eq__(self, other):
        if(not isinstance(other, Grid)):
            return False
        return self.array == other.array