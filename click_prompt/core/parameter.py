"""
Parameter module for the click-prompt package.

This module extends the functionality of Click's Parameter class to create
interactive command-line parameters that prompt users for input.

Classes:
    - PromptParameter: Base class for parameters with user prompts.
    - ChoiceParameter: Parameter for selecting from choices.
    - ConfirmParameter: Parameter for yes/no confirmations.
    - FilePathParameter: Parameter for file path input.
    - AutoCompleteParameter: Parameter with autocomplete functionality.
"""

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union
from typing import List
from typing import Sequence

from abc import ABC
from abc import abstractmethod

import click
from click.core import Context

import questionary


class PromptParameter(click.Parameter, ABC):
    """
    Abstract base class for click parameters that require prompting the user for input.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        style: Optional[questionary.Style] = None,
        **kwargs
    ):
        self.style = style
        super().__init__(param_decls, **kwargs)

    def _is_unset_value(self, value: Any) -> bool:
        """
        Checks if a value is unset.

        In newer Click versions (>= 8.3.0), unset values may be represented by a
        sentinel rather than None.
        """
        if value is None:
            return True
        unset_value = getattr(getattr(click, "_utils", None), "UNSET", None)
        return value is unset_value
     

    def get_default_prompt_value(self, ctx: Context) -> Any:
        """
        Return the effective default value for prompts, or None if unset.
        """
        default_value = self.get_default(ctx)
        if self._is_unset_value(default_value):
            return None
        return default_value
    
    @abstractmethod
    def prompt_for_value(self, ctx: Context) -> Any:
        """
        Prompt the user for a value using a questionary interface.
        """

class ChoiceParameter(PromptParameter, ABC):
    """
    Allows the user to interactively select a single item given a sequence of
    choices. Code adapted from Stack Overflow [1].

    Interactive selection is skipped if the list contains only a single item.

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
            raise TypeError("type must be click.Choice")

    def prepare_choice_list(self, ctx: click.core.Context) -> List[questionary.Choice]:
        """
        Return a list of choices and mark those that are default values.
        """
        default = self.get_default_prompt_value(ctx)
        if default is None:
            default = []
        return [questionary.Choice(n, checked=n in default) for n in self.type.choices]

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        if len(self.type.choices) == 1:
            return self.type.choices[0]
        if self.multiple:
            return questionary.checkbox(
                self.prompt, choices=self.prepare_choice_list(ctx), style=self.style
            ).unsafe_ask()
        return questionary.select(
            self.prompt,
            choices=self.type.choices,
            default=self.get_default_prompt_value(ctx),
            style=self.style,
        ).unsafe_ask()


class ConfirmParameter(PromptParameter, ABC):
    """
    Allows the user to confirm an option. This can also be implemented using
    Click's built-in features.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, is_flag=True, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        default_value = bool(self.get_default_prompt_value(ctx))
        return questionary.confirm(
            self.prompt, default=default_value, style=self.style
        ).unsafe_ask()


class FilePathParameter(PromptParameter, ABC):
    """
    Allows the user to specify a path.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        default_path = self.get_default_prompt_value(ctx) or ""
        return questionary.path(
            self.prompt, default=default_path, style=self.style
        ).unsafe_ask()


class AutoCompleteParameter(PromptParameter, ABC):
    """
    Autocomplete user input.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        choices=None,
        meta_information: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        self.meta_information = meta_information or {}
        super().__init__(param_decls, prompt=prompt, **kwargs)
        if isinstance(self.type, click.Choice):
            self.choices = self.type.choices
        else:
            self.choices = choices or []

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        default_value = self.get_default_prompt_value(ctx) or ""
        return questionary.autocomplete(
            self.prompt,
            self.choices,
            default_value,
            meta_information=self.meta_information,
            style=self.style,
        ).unsafe_ask()


class InputTextParameter(PromptParameter, ABC):
    """
    Raw text user input.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        **kwargs
    ):
        super().__init__(param_decls, prompt=prompt, **kwargs)

    def prompt_for_value(self, ctx: click.core.Context) -> Any:
        if self.get_default_prompt_value(ctx) is None:
            default_value = ""
        else:
            default_value = str(self.get_default_prompt_value(ctx))
        return questionary.text(
            self.prompt,
            default=default_value,
            style=self.style,
        ).unsafe_ask()
