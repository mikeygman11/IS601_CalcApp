from app.commands import Command
#creating the DivideCommand class

class DivideCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def execute(self):
        if self.y == 0:
            return "Error: Division by zero."
        return self.x / self.y