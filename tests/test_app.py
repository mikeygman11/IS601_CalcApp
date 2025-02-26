import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.commands import CommandHandler, Command

# Create a dummy command that implements Command.
class TestCommand(Command):
    __test__ = False  # This prevents pytest from collecting it as a test class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def execute(self):
        return self.x + self.y
    
def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

import pytest

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "Unknown command: unknown_command" in captured.out

def test_execute_command_invalid_input(monkeypatch, capfd):
    handler = CommandHandler()
    handler.register_command("Dummy", CommandHandler)
    # Simulate invalid numeric input
    monkeypatch.setattr('builtins.input', lambda _: "notanumber")
    handler.execute_command("Dummy")
    captured = capfd.readouterr().out
    assert "Invalid input" in captured

def test_add_command():
    command = AddCommand(2, 3)
    assert command.execute() == 5

def test_subtract_command():
    command = SubtractCommand(10, 4)
    assert command.execute() == 6

def test_multiply_command():
    command = MultiplyCommand(4, 5)
    assert command.execute() == 20

def test_divide_command():
    command = DivideCommand(10, 2)
    assert command.execute() == 5

def test_divide_by_zero():
    command = DivideCommand(10, 0)
    with pytest.raises(ZeroDivisionError):
        command.execute()

def test_execute_command(monkeypatch, capsys):
    # Instantiate the CommandHandler and register DummyCommand.
    handler = CommandHandler()
    handler.register_command("Test", TestCommand)
    
    # Simulate user input for "Enter first number: " and "Enter second number: "
    inputs = iter(["3", "4"])  # For example, 3 and 4
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    
    # Execute the command; this should trigger the code for x, y input, instantiation, and print.
    handler.execute_command("Test")
    
    # Capture output to verify that our expected result is printed.
    captured = capsys.readouterr().out
    # Since DummyCommand.execute returns 3 + 4 = 7, we expect "Result: 7" to appear in the output.
    assert "Result: 7" in captured