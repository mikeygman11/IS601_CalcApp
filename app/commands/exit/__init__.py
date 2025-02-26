from app.commands import Command
#creating the ExitCommand class

class ExitCommand(Command):
    def execute(self):
        print("Exit")