"""
Provides additional interactive command line interface options for the
click framework using the questionary library
"""

from typing import Any
from typing import Optional
from typing import Union
from typing import List
from typing import Sequence

import click
import questionary


class ChoiceOption(click.Option):
    """
    Allows the user to interactively select a single item given a sequence of
    choices. Code adapted from Stackoverflow [1].

    [1] https://stackoverflow.com/questions/54311067/
    """

    def __init__(self,
                 param_decls: Optional[Sequence[str]] = None,
                 prompt: Union[bool, str] = True,
                 **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, multiple=False, **kwargs)
        if not isinstance(self.type, click.Choice):
            raise Exception('ChoiceOption type arg must be click.Choice')

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        if len(self.type.choices) == 1:
            return self.type.choices[0]
        return questionary.select(self.prompt, choices=self.type.choices).unsafe_ask()



class MultipleOption(click.Option):
    """
    Allows the user to interactively select multiple items from a list given a
    sequence of choices. Interactive selection is skipped if the list only
    contains a single item.
    """

    def __init__(self,
                 param_decls: Optional[Sequence[str]] = None,
                 prompt: Union[bool, str] = True,
                 **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, multiple=True, **kwargs)
        if not isinstance(self.type, click.Choice):
            raise Exception('MultipleOption type arg must be click.Choice')

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        if len(self.type.choices) == 1:
            return [self.type.choices[0]]
        return questionary.checkbox(self.prompt, choices=self.type.choices).unsafe_ask()


class ConfirmOption(click.Option):
    """
    Allows the user to confirm an option. Can be also implemented using click
    onboard features.
    """

    def __init__(self,
                 param_decls: Optional[Sequence[str]] = None,
                 prompt: Union[bool, str] = True,
                 **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, is_flag=True, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.confirm(self.prompt, default=self.default).unsafe_ask()


class FilePathOption(click.Option):
    """
    Allows the user to sepcify a path.
    """

    def __init__(self,
                 param_decls: Optional[Sequence[str]] = None,
                 prompt: Union[bool, str] = True,
                 **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, **kwargs)
        self.default = self.default or '~'

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.path(self.prompt, default=self.default).unsafe_ask()


class AutoCompleteOption(click.Option):
    """
    Auto complete user input.
    """

    def __init__(self,
                 param_decls: Optional[Sequence[str]] = None,
                 prompt: Union[bool, str] = True,
                 choices=None,
                 **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, **kwargs)
        if isinstance(self.type, click.Choice):
            self.choices = self.type.choices
        else:
            self.choices = choices or []
        self.default = self.default or ''

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.autocomplete(self.prompt, self.choices, self.default).unsafe_ask()
