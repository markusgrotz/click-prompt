"""
Contains the argument implementations.
"""

from typing import Optional
from typing import Sequence
from typing import Union
from typing import Mapping
from typing import Any
from typing import Tuple

from abc import ABC

import click
from click.core import ParameterSource
from click.core import Context

import questionary

from click_prompt.core.parameter import PromptParameter
from click_prompt.core.parameter import ChoiceParameter
from click_prompt.core.parameter import ConfirmParameter
from click_prompt.core.parameter import FilePathParameter
from click_prompt.core.parameter import AutoCompleteParameter
from click_prompt.core.parameter import InputTextParameter


class PromptArgument(click.Argument, PromptParameter, ABC):
    """
    Base class for prompt-enabled arguments.
    """

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        multiple: bool = False,
        style: Optional[questionary.Style] = None,
        **kwargs
    ):
        kwargs.pop("is_flag", None)
        super().__init__(param_decls, **kwargs)
        self.style = style
        self.prompt = prompt
        self.multiple = multiple

    def consume_value(
        self, ctx: Context, opts: Mapping[str, Any]
    ) -> Tuple[Any, ParameterSource]:

        value = opts.get(self.name)  # type: ignore
        source = ParameterSource.COMMANDLINE

        if self._is_unset_value(value):
            value = self.prompt_for_value(ctx)
            source = ParameterSource.PROMPT

        return value, source


class ChoiceArgument(ChoiceParameter, PromptArgument):
    """
    Argument class for :class:`~click_prompt.core.parameter.ChoiceParameter`
    """


class ConfirmArgument(ConfirmParameter, PromptArgument):
    """
    Argument class for :class:`~click_prompt.core.parameter.ConfirmParameter`
    """


class FilePathArgument(FilePathParameter, PromptArgument):
    """
    Argument class for :class:`~click_prompt.core.parameter.FilePathParameter`
    """


class AutoCompleteArgument(AutoCompleteParameter, PromptArgument):
    """
    Argument class for :class:`~click_prompt.core.parameter.AutoCompleteParameter`
    """


class InputTextArgument(InputTextParameter, PromptArgument):
    """
    Argument class for :class:`~click_prompt.core.parameter.InputTextParameter`
    """
