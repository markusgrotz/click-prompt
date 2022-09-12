#!/usr/bin/env python3


from typing import Sequence

import click

# import rich_click as click

from click_prompt import ChoiceOption
from click_prompt import ConfirmOption
from click_prompt import FilePathOption
from click_prompt import AutoCompleteOption

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
@click.option(
    "--choice",
    prompt="What do you want to eat?",
    type=click.Choice(FRUITS),
    cls=ChoiceOption,
)
def single(choice: str):
    print(choice)


@cli.command()
@click.option(
    "--options",
    prompt="Select smoothie ingredients",
    type=click.Choice(FRUITS),
    multiple=True,
    cls=ChoiceOption,
)
def multiple(options: Sequence[str]):
    print(options)


@cli.command()
@click.option("--confirm", prompt="Do you really want to ?", cls=ConfirmOption)
def confirm(confirm: bool):
    print(confirm)


@cli.command()
@click.option("--confirm", prompt="Confirm", is_flag=True)
def confirm_click(confirm: bool):
    print(confirm)


@cli.command()
@click.option("--path", cls=FilePathOption, default="/tmp/foo")
def file(path: str):
    print(path)


@cli.command()
@click.option("--complete", type=click.Choice(FRUITS), cls=AutoCompleteOption)
def auto_choice(complete: str):
    print(complete)


@cli.command()
@click.option(
    "--complete",
    prompt="What is your favourite fruit?",
    choices=FRUITS,
    cls=AutoCompleteOption,
)
def auto(complete: str):
    print(complete)


from click_prompt import ChoiceArgument

@cli.command()
@click.argument("fruit", type=click.Choice(FRUITS), cls=ChoiceArgument)
def argument(fruit: str):
    print(fruit)

if __name__ == "__main__":
    cli()
