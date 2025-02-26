from app.commands import Command
#creating the GoodbyeCommand class

class GoodbyeCommand(Command):
    def execute(self):
        print("Bye!")