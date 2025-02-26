import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.subract import SubtractCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand

def test_add_command(capfd):
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The Add Command should print 'Adding!'"

def test_subtract_command(capfd):
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The Subtract Command should print 'Subtract!'"

def test_divide_command(capfd):
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The Divide Command should print 'Divide!'"

def test_multiply_command(capfd):
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The Multiply Command should print 'Mult!'"
