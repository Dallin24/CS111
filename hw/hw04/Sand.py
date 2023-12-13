from Grid import Grid

class Sand:
    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Sand({self.x},{self.y})'
    
    def gravity(self):
        if self.is_move_ok(self.x, self.y+1):
            return (self.x, self.y+1)
        elif self.is_move_ok(self.x-1, self.y+1):
            return (self.x-1, self.y+1)
        elif self.is_move_ok(self.x+1, self.y+1):
            return (self.x+1, self.y+1)
                
        return None
    
    def is_move_ok(self, x_to, y_to):
        if (y_to >= self.grid.height or x_to >= self.grid.width or x_to < 0):
            return False
        
        destination_spot = self.grid.get(x_to, y_to)
        
        if ((destination_spot != None)):
            return False
        
        if(self.x != x_to and (self.grid.get(x_to, y_to - 1) != None)):
            return False
        return True
    
    def move(self, physics):
        if(physics() == None):
            return
        self.grid.set(self.x, self.y, None)
        self.x, self.y = physics()
        self.grid.set(self.x, self.y, self)
        