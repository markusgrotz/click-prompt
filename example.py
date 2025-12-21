#!/usr/bin/env python3
"""
Example CLI application using click and click_prompt for interactive prompts.
"""

from typing import Sequence

from prompt_toolkit.styles import Style

import click

# import rich_click as click

from click_prompt import choice_option
from click_prompt import confirm_option
from click_prompt import filepath_option
from click_prompt import auto_complete_option
from click_prompt import choice_argument
from click_prompt import input_text_option
from click_prompt import input_text_argument

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
def cli():
    """Main CLI entry point."""


@cli.command()
@choice_option(
    "--fruit",
    type=click.Choice(FRUITS),
    prompt="What do you want to eat?",
    default=FRUITS[3],
)
def single(fruit: str):
    """Handle a single fruit selection."""
    print(fruit)


def get_fruits():
    """Return a subset of fruits as default choices."""
    return FRUITS[3:6] + FRUITS[7:8]


@cli.command()
@choice_option(
    "--fruit",
    prompt="Select smoothie ingredients",
    type=click.Choice(FRUITS),
    multiple=True,
    default=get_fruits,
)
def multiple(fruit: Sequence[str]):
    """Handle multiple fruit selections."""
    print(fruit)


@cli.command()
@confirm_option("--confirm", prompt="Do you really want to ?")
def confirm(confirm: bool):
    """Handle a confirmation prompt."""
    print(confirm)


@cli.command()
@click.option("--confirm", prompt="Confirm", is_flag=True)
def confirm_click(confirm: bool):
    """Handle a confirmation flag using plain Click."""
    print(confirm)


@cli.command()
@filepath_option("--path", default="/tmp/foo")
def file(path: str):
    """Handle a file path input."""
    print(path)


@cli.command()
@auto_complete_option("--fruit", type=click.Choice(FRUITS), default="r")
def auto_choice(fruit: str):
    """Autocomplete fruit selection without prompt."""
    print(fruit)


style = Style(
    [
        ("question", "fg:#FF0000 bg:#00FF00 bold"),
        ("answer", "fg:#FF0000 bg:#FFFFFF"),
    ]
)


@cli.command()
@auto_complete_option("--fruit", type=click.Choice(FRUITS), style=style)
def auto_choice_fancy(fruit: str):
    """Autocomplete fruit selection with a customized styled  prompt.
    https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/styling.html
    """
    print(fruit)


@cli.command()
@auto_complete_option(
    "--fruit", prompt="What is your favourite fruit?", choices=FRUITS, default="m"
)
def auto(fruit: str):
    """Autocomplete fruit selection with prompt."""
    print(fruit)


@cli.command()
@choice_argument("fruit", type=click.Choice(FRUITS))
def argument(fruit: str):
    """Handle a fruit selection as a positional argument."""
    print(fruit)


@cli.command()
@input_text_option(
    "-f", "--fruit", type=click.STRING, prompt="What fruit", default="Bananas"
)
@input_text_option("-q", "--quantity", type=click.INT, prompt="How many", default=2)
def text_opt(fruit: str, quantity: int):
    """Handle fruit and quantity inputs via options."""
    print(f"Fruit: {fruit} | Quantity: {quantity}")


@cli.command()
@input_text_argument("fruit", type=click.STRING, prompt="What fruit")
@input_text_argument("quantity", type=click.INT, prompt="How many")
def text_arg(fruit: str, quantity: int):
    """Handle fruit and quantity inputs via arguments."""
    print(f"Fruit: {fruit} | Quantity: {quantity}")


if __name__ == "__main__":
    cli()
