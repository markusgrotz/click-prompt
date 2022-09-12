# click-prompt 

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/click-prompt)](https://pypi.org/project/click-prompt/) 
[![PyPI version](https://img.shields.io/pypi/v/click-prompt)](https://pypi.org/project/click-prompt/) 


click-prompt provides more beautiful interactive options for the Python click
library. The library is inspired by a post on [stackoverflow.com](https://stackoverflow.com/questions/54311067/)

## Usage

The library can be used in two ways: 1) as decorator, or 2) as type parameter.

### With decorators


```python
import click
from click_prompt import choice_option

@click.command()
@choice_option('--fruit', type=click.Choice(['Apples', 'Bananas', 'Grapefruits', 'Mangoes']))
def select_fruit(fruit: str):
    print(fruit)
```

### As class

```python
import click
from click_prompt import ChoiceOption

@click.command()
@click.option('--fruit', 
              type=click.Choice(['Apples', 'Bananas', 'Grapefruits', 'Mangoes']),
              cls=ChoiceOption)
def select_fruit(fruit: str):
    print(fruit)
```

## Example

![Example](./docs/example_cli.gif)


## Available Decorators

Here is a list of available decorators that can be used with the click library
instead of a `click.Option` decorator

 - `choice_option`: Select a single item out of a list. Use the parameter
   `multiple=True` to select multiple items out of a list
 - `confirm_option`: Yes/No confirmation
 - `filepath_option`: Select a file path with auto completion
 - `auto_complete_option`: Auto completion given a list

for every `click.Option` there is also a `click.Argument` implementation
