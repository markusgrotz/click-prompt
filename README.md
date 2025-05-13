
# click-prompt

[![Supported Python Versions](https://img.shields.io/pypi/pyversions/click-prompt)](https://pypi.org/project/click-prompt/) 
[![PyPI version](https://img.shields.io/pypi/v/click-prompt)](https://pypi.org/project/click-prompt/) 
[![License](https://img.shields.io/pypi/l/click-prompt)](https://github.com/markusgrotz/click-prompt/blob/main/LICENSE.md)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://black.readthedocs.io/en/stable/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/click-prompt)

**click-prompt** extends the [Click](https://click.palletsprojects.com/) command-line interface library by adding intuitive, interactive prompts. It's perfect for building more user-friendly CLI tools.

This library is inspired by a post on [stackoverflow.com](https://stackoverflow.com/questions/54311067/).

Contributions are welcome! [Open a pull request](https://github.com/markusgrotz/click-prompt/pulls) or [submit an issue](https://github.com/markusgrotz/click-prompt/issues).

## Installation

To install `click-prompt`, use pip:

```bash
pip install click-prompt
```

## Usage

Here’s a basic example using the `choice_option` decorator:

```python
import click
from click_prompt import choice_option

@click.command()
@choice_option('--fruit', type=click.Choice(['Apples', 'Bananas', 'Grapefruits', 'Mangoes']))
def select_fruit(fruit: str):
    """Prompt user to select a fruit from a list."""
    print(f"You selected: {fruit}")

if __name__ == '__main__':
    select_fruit()
```

## Example

For more examples see the file [example.py](https://github.com/markusgrotz/click-prompt/blob/main/example.py).

![Example](https://github.com/markusgrotz/click-prompt/blob/main/docs/example_cli.gif?raw=true)

## Available Decorators

Each of these decorators replaces a `click.Option` (and also works with `click.Argument`):

- **`choice_option`**  
  Prompt the user to select one (or more with `multiple=True`) from a list.

- **`confirm_option`**  
  Yes/No confirmation prompt.

- **`filepath_option`**  
  Prompt the user to select a file path with auto-completion.

- **`auto_complete_option`**  
  Input prompt with tab completion from a list of choices.

- **`input_text_option`**  
  Prompt the user for free-form text input.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/markusgrotz/click-prompt/blob/main/LICENSE.md) file for more information.
