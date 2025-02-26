from app.commands import Command
#creating the GreetCommand class

class GreetCommand(Command):
    def execute(self):
        print("Hello, World!")