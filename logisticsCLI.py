from mylib.logistics import (
    calc_distance,
)
import click

# builda click group
@click.group()
def cli():
    """Logistics tool"""


# add a command to calculate the distance between two cities
@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance_command(city1, city2):
    """Calculate the distance between two cities"""
    dist = calc_distance(city1, city2)
    click.echo(f"The distance between {city1} and {city2} is {dist} km")
