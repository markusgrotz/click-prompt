from typing import Any
from typing import Optional
from typing import Union
from typing import List
from typing import Sequence
from typing import Mapping
from typing import Tuple

from abc import ABC
from abc import abstractmethod

import click
from click.core import Context

import questionary


class PromptParameter(click.Parameter, ABC):

    prompt: Union[bool, str]

    @abstractmethod
    def prompt_for_value(self, ctx: Context):
        pass


class ChoiceParameter(PromptParameter, ABC):
    """
    Allows the user to interactively select a single item given a sequence of
    choices. Code adapted from Stackoverflow [1].

    Interactive selection is skipped if the list only contains a single item.

    [1] https://stackoverflow.com/questions/54311067/
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        multiple: bool = False,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, multiple=multiple, **kwargs)

        if not isinstance(self.type, click.Choice):
            print(self.type)
            raise Exception("ChoiceOption type arg must be click.Choice")

    def prepare_choice_list(self, ctx: click.core.Context) -> List[questionary.Choice]:
        """
        Returns a list of choices and check if it is listed as default value
        """
        default = self.get_default(ctx)
        if default is None:
            default = []
        return [questionary.Choice(n, checked=n in default) for n in self.type.choices]

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        if len(self.type.choices) == 1:
            return self.type.choices[0]
        if self.multiple:
            return questionary.checkbox(
                self.prompt, choices=self.prepare_choice_list(ctx)
            ).unsafe_ask()
        else:
            return questionary.select(
                self.prompt, choices=self.type.choices, default=self.get_default(ctx)
            ).unsafe_ask()


class ConfirmParameter(PromptParameter, ABC):
    """
    Allows the user to confirm an option. Can be also implemented using click
    onboard features.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, is_flag=True, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.confirm(
            self.prompt, default=self.get_default(ctx) or False
        ).unsafe_ask()


class FilePathParameter(PromptParameter, ABC):
    """
    Allows the user to sepcify a path.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.path(
            self.prompt, default=self.get_default(ctx) or ""
        ).unsafe_ask()


class AutoCompleteParameter(PromptParameter, ABC):
    """
    Auto complete user input.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        choices=None,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, **kwargs)
        if isinstance(self.type, click.Choice):
            self.choices = self.type.choices
        else:
            self.choices = choices or []

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        return questionary.autocomplete(
            self.prompt, self.choices, self.get_default(ctx) or ""
        ).unsafe_ask()
