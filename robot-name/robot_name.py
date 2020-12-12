import random

class Robot:
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    def __init__(self):
        self.name = self.getName()
    
    def getName(self):
        first = ''.join(random.choices(self.letters, k=2))
        second = ''.join(random.choices(self.numbers, k=3))
        return f"{first}{second}"
        
    def reset(self):
        new_name = self.getName()
        if new_name == self.name:
            new_name = self.getName()
        self.setName(new_name)
    
    def setName(self, name):
        self.name = name
        
