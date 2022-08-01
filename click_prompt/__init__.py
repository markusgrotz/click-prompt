import click
import questionary

from typing import Any
from typing import Optional
from typing import Union
from typing import List
from typing import Sequence


class ChoiceOption(click.Option):
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

    def __init__(self,  
            param_decls: Optional[Sequence[str]] = None,
            prompt: Union[bool, str] = True,
            **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, multiple=True, **kwargs)
        if not isinstance(self.type, click.Choice):
            raise Exception('ChoiceOption type arg must be click.Choice')

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        if len(self.type.choices) == 1:
            return [self.type.choices[0]]
        return questionary.checkbox(self.prompt, choices=self.type.choices).unsafe_ask()


class ConfirmOption(click.Option):
 
    def __init__(self,  
            param_decls: Optional[Sequence[str]] = None,
            prompt: Union[bool, str] = True,
            **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, is_flag=True, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.confirm(self.prompt, default=self.default).unsafe_ask()


class FilePathOption(click.Option):
 
    def __init__(self,  
            param_decls: Optional[Sequence[str]] = None,
            prompt: Union[bool, str] = True,
            **kwargs):
        click.Option.__init__(self, param_decls, prompt=prompt, **kwargs)
        self.default = self.default or '~'

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.path(self.prompt, default=self.default).unsafe_ask()

class AutoCompleteOption(click.Option):
 
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
        return questionary.autocomplete(self.prompt, choices=self.choices, default=self.default).unsafe_ask()

