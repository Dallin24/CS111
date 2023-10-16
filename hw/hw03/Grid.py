from copy import deepcopy

class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = []
        
        for i in range(height):
            row = []
            for j in range(width):
                row.append(None)
            self.array.append(row)
            
    def in_bounds(self, x, y):
        return (self.width >= x >= 0 and self.height >= y >= 0)
    
    def get(self, x, y):
        if not(self.in_bounds(x,y)):
            raise IndexError
        
        current_value = self.array[y][x]
        return current_value
    
    def set(self, x, y, value):
        if not(self.in_bounds(x,y)):
            raise IndexError
        
        self.array[y][x] = value
        return None
    
    @staticmethod
    def check_list_malformed(lst):
        if (type(lst) is not list) or (len(lst) == 0):
            raise ValueError

        for row in lst:
            if not(type(row) is list) or len(row) != len(lst[0]):
                raise ValueError
        
        return False
    
    def copy(self):
        return Grid.build(self.array)
    
    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid.build({self.array})'
    
    def __eq__(self, other):
        if(isinstance(other, Grid)):
            return self.array == other.array
        elif(isinstance(other, list)):
            return self.array == other
        else:
            return False
        
    
    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        
        height = len(lst)
        width = len(lst[0])
        
        new_grid = Grid(width, height)
        
        for y in range(height):
            for x in range(width):
                new_grid.array[y][x] = deepcopy(lst[y][x])
                
        return new_grid
    try:
        yes = ''
    except ValueError as e:
        print(f'An error has occurred: {type(e)}. Error Info: {e}')