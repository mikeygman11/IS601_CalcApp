import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from calculator.calculation import Calculation
from app.commands import CommandHandler
from app.commands.add import AddCommand

def test_add_command(capfd):
    command = AddCommand(2, 3)  # ✅ Provide x and y
    result = command.execute()
    assert result == 5, "The AddCommand should return 5 when adding 2 and 3"

def test_subtract_command(capfd):
    command = SubtractCommand(10, 4)  
    result = command.execute()
    assert result == 6, "The SubtractCommand should return 6 when subtracting 4 from 10"

def test_divide_command(capfd):
    command = DivideCommand(8, 2)
    result = command.execute()
    assert result == 4, "The DivideCommand should return 4 when dividing 8 by 2"

def test_multiply_command(capfd):
    command = MultiplyCommand(6, 3)  
    result = command.execute()
    assert result == 18, "The MultiplyCommand should return 18 when multiplying 6 and 3"

def test_divide_by_zero():
    """Ensure DivideCommand handles division by zero correctly."""
    command = DivideCommand(5, 0)
    result = command.execute()
    assert result == "Error: Division by zero."

def test_register_command():
    handler = CommandHandler()
    handler.register_command("Add", AddCommand)

    # Ensure 'Add' is registered
    assert "Add" in handler.commands

def test_execute_valid_command(monkeypatch, capfd):
    inputs = iter([5, 3])  # Simulate entering 5 and 3
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock user input
    
    handler = CommandHandler()
    handler.register_command("Add", AddCommand)
    
    # Capture output
    handler.execute_command("Add")
    
    # Capture printed output
    captured = capfd.readouterr()
    assert "Result: 8" in captured.out  # 5 + 3 = 8

def test_execute_unknown_command(monkeypatch, capfd):
    inputs = iter([5, 3])  # Simulate entering 5 and 3
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock user input
    
    handler = CommandHandler()

    # Capture output
    handler.execute_command("Unknown")
    
    # Capture printed output for "Unknown command"
    captured = capfd.readouterr()
    assert "Unknown command: Unknown" in captured.out

def test_execute_invalid_input(monkeypatch, capfd):
    inputs = iter(['a', 'b'])  # Invalid input that cannot be converted to a float
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  # Mock user input
    
    handler = CommandHandler()
    handler.register_command("Add", AddCommand)

    # Capture output
    handler.execute_command("Add")
    
    # Capture printed output for "Invalid input"
    captured = capfd.readouterr()
    assert "Invalid input! Please enter numeric values." in captured.out