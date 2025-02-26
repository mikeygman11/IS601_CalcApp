import importlib
import os
import pkgutil
from app.commands import Command, CommandHandler  # Import Command and CommandHandler at the top

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if isinstance(item, type) and issubclass(item, Command) and item != Command:
                            command_name = item.__name__.replace('Command', '')
                            self.command_handler.register_command(command_name, item)
                    except TypeError:
                        continue
    
    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:
            command_name = input(">>> ").strip()
            if command_name.lower() == 'exit':
                break
            self.command_handler.execute_command(command_name)