from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

#need to add in a couple other random functions later
class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("Add", AddCommand())
        self.command_handler.register_command("Subtract", SubtractCommand())
        self.command_handler.register_command("Divide", DivideCommand())

        self.command_handler.register_command("Multiply", MultiplyCommand())


        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())