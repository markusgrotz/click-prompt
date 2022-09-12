#!/usr/bin/env python3


from typing import Sequence

import click

# import rich_click as click

from click_prompt import choice_option
from click_prompt import confirm_option
from click_prompt import filepath_option
from click_prompt import auto_complete_option
from click_prompt import choice_argument

FRUITS = [
    "Apples",
    "Bananas",
    "Grapefruits",
    "Mangoes",
    "Oranges",
    "Pears",
    "Peaches",
    "Raspberries",
    "Strawberries",
    "Watermelons",
]


@click.group()
def cli(**kwargs):
    pass


@cli.command()
@choice_option("--fruit", type=click.Choice(FRUITS), prompt="What do you want to eat?")
def single(fruit: str):
    print(fruit)


@cli.command()
@choice_option(
    "--fruit",
    prompt="Select smoothie ingredients",
    type=click.Choice(FRUITS),
    multiple=True,
)
def multiple(fruit: Sequence[str]):
    print(fruit)


@cli.command()
@confirm_option("--confirm", prompt="Do you really want to ?")
def confirm(confirm: bool):
    print(confirm)


@cli.command()
@click.option("--confirm", prompt="Confirm", is_flag=True)
def confirm_click(confirm: bool):
    print(confirm)


@cli.command()
@filepath_option("--path", default="/tmp/foo")
def file(path: str):
    print(path)


@cli.command()
@auto_complete_option("--complete", type=click.Choice(FRUITS))
def auto_choice(complete: str):
    print(complete)


@cli.command()
@auto_complete_option(
    "--complete", prompt="What is your favourite fruit?", choices=FRUITS
)
def auto(complete: str):
    print(complete)


@cli.command()
@choice_argument("fruit", type=click.Choice(FRUITS))
def argument(fruit: str):
    print(fruit)


if __name__ == "__main__":
    cli()
