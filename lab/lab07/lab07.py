class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0
        
    def __str__(self):
        return f"Key: '{self.key}', Pos: {self.pos}"
    
    def __repr__(self):
        return f"Button({self.pos}, '{self.key}')"

class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    buttons of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for item in args:
            self.add_button(item)

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if self.buttons.get(info) != None:
            selected_button = self.buttons.get(info)
            selected_key = selected_button.key
            selected_button.times_pressed += 1
            return selected_key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        string = ''
        for item in typing_input:
            string += str(self.buttons.get(item).key)
            self.buttons.get(item).times_pressed += 1
        return string
    
    def __repr__(self):
        string = 'Keyboard('
        items_list = self.buttons.items()
        
        count = 0
        for item in items_list:
            string += repr(item[1])
            count +=1
            if(count == len(items_list)):
                string += ')'
            else:
                string += ', '
        
        return string
        
    def __str__(self):
        string = ''
        items_list = self.buttons.items()
        
        count = 0
        for item in items_list:
            string += str(item[1])
            count +=1
            
            if(count == len(items_list)):
                string
            else:
                string += ' | '
        
        return string
    
    def add_button(self, addedButton):
        if (addedButton.pos in self.buttons.keys()):
            return
        else:
            self.buttons[addedButton.pos] = addedButton
    
    