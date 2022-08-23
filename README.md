# click-prompt

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/click-prompt/0.0.1)](https://pypi.org/project/click-prompt/) 
[![PyPI version](https://badge.fury.io/py/click-prompt.svg)](https://badge.fury.io/py/click-prompt)


click-prompt provides more beautiful interactivate options for the Python click
library.


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
