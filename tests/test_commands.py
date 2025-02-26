import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from calculator.calculation import Calculation

def test_add_command(capfd):
    command = AddCommand(2, 3)  # ✅ Provide x and y
    result = command.execute()
    assert result == 5, "The AddCommand should return 5 when adding 2 and 3"

def test_subtract_command(capfd):
    command = SubtractCommand(10, 4)  # ✅ Provide x and y
    result = command.execute()
    assert result == 6, "The SubtractCommand should return 6 when subtracting 4 from 10"

def test_divide_command(capfd):
    command = DivideCommand(8, 2)  # ✅ Provide x and y
    result = command.execute()
    assert result == 4, "The DivideCommand should return 4 when dividing 8 by 2"

def test_multiply_command(capfd):
    command = MultiplyCommand(6, 3)  # ✅ Provide x and y
    result = command.execute()
    assert result == 18, "The MultiplyCommand should return 18 when multiplying 6 and 3"