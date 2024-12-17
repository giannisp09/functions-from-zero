from mylib.calc import add, subtract, multiply, divide, factorial
from calcCLI import cli
from click.testing import CliRunner
import pytest


@pytest.fixture
def runner():
    return CliRunner()


# write test for every function in calcCLI.py
def test_add_command(runner):
    result = runner.invoke(cli, ["add", "2", "2"])
    assert result.exit_code == 0
    assert result.output == "4.0\n"


def test_sub_command(runner):
    result = runner.invoke(cli, ["sub", "2", "2"])
    assert result.exit_code == 0
    assert result.output == "0.0\n"


def test_mul_command(runner):
    result = runner.invoke(cli, ["mul", "2", "2"])
    assert result.exit_code == 0
    assert result.output == "4.0\n"


def test_div_command(runner):
    result = runner.invoke(cli, ["div", "2", "2"])
    assert result.exit_code == 0
    assert result.output == "1.0\n"


def test_add():
    assert add(2, 2) == 4


# write test for every function in calc.py


def test_subtract():
    assert subtract(2, 2) == 0


def test_multiply():
    assert multiply(2, 2) == 4


def test_divide():

    assert divide(2, 2) == 1


def test_factorial():

    assert factorial(5) == 120
