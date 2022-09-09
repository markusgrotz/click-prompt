# click-prompt

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/click-prompt/)](https://pypi.org/project/click-prompt/) 
[![PyPI version](https://badge.fury.io/py/click-prompt.svg)](https://badge.fury.io/py/click-prompt)


click-prompt provides more beautiful interactive options for the Python click
library. The library is inspired by a post on [stackoverflow.com](https://stackoverflow.com/questions/54311067/)

## Usage

```python


import click
from click_prompt import ChoiceOption

@click.command()
@click.option('--fruit', 
              type=click.Choice(['Apples', 'Bananas', 'Grapefruits', 'Mangoes']),
              cls=ChoiceOption)
def select_fruit(fruit: str):
    print(choice)
```


## Available Parameters

for every click.Option there is also a click.Argument  implementation

 - ChoiceOption: Select a single item out of a list
 - MultipleOption: Select multiple items out of a list
 - ConfirmOption: Yes/No confirmation
 - FilePathOption: Select a file path with auto completion
 - AutoCompleteOption: Auto completion given a list

