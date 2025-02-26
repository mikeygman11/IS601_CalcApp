from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register command classes, NOT instances
        self.command_handler.register_command("Add", AddCommand)
        self.command_handler.register_command("Subtract", SubtractCommand)
        self.command_handler.register_command("Divide", DivideCommand)
        self.command_handler.register_command("Multiply", MultiplyCommand)

        print("Type 'exit' to exit.")
        while True:  # REPL (Read, Evaluate, Print, Loop)
            command_name = input(">>> ").strip()
            if command_name.lower() == "exit":
                break
            self.command_handler.execute_command(command_name)