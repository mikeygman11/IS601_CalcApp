from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass #pragma: no cover -no test

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        """Retrieve command class, get arguments, and execute."""
        if command_name in self.commands:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                command = self.commands[command_name](x, y)  # Instantiate command
                print(f"Result: {command.execute()}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print(f"Unknown command: {command_name}")