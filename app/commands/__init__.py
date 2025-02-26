from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class
        print(f"Command '{command_name}' registered. Current mapping: {list(self.commands.keys())}")
    
    def execute_command(self, command_name: str):
        if command_name in self.commands:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                # Instantiate the command with the provided arguments.
                command = self.commands[command_name](x, y)
                print(f"Result: {command.execute()}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print(f"Unknown command: {command_name}")
            # Exit if the command is unknown.
            import sys
            sys.exit(1)