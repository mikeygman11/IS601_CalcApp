from app import Command
#creating the DivideCommand class

class DivideCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x / self.y