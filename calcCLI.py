# #!/usr/bin/env python3

from mylib.calc import add, subtract, multiply, divide, factorial
import click


@click.group()
def cli():
    """A calculator program"""


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    """Add two numbers

    Example:
    ./calcCLI.py add 2 3"""

    # use colored output to print the result
    click.echo(click.style(f"{add(a, b)}", fg="green"))


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_command(a, b):
    """Subtract two numbers

    Example:
    ./calcCLI.py sub 2 3"""

    # use colored output to print the result
    click.echo(click.style(f"{subtract(a, b)}", fg="green"))


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_command(a, b):
    """Multiply two numbers

    Example:
    ./calcCLI.py mul 2 3"""

    # use colored output to print the result
    click.echo(click.style(f"{multiply(a, b)}", fg="green"))


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_command(a, b):
    """Divide two numbers

    Example:
    ./calcCLI.py div 2 3"""

    # use colored output to print the result
    click.echo(click.style(f"{divide(a, b)}", fg="green"))


@cli.command("factorial")
@click.argument("n", type=int)
def factorial_command(n):
    """Calculate the factorial of a number

    Example:
    ./calcCLI.py factorial 5"""

    # use colored output to print the result
    click.echo(click.style(f"{factorial(n)}", fg="green"))


if __name__ == "__main__":
    cli()
