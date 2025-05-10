"""
Contains the option implementations
"""

import click

from click_prompt.core.parameter import ChoiceParameter
from click_prompt.core.parameter import ConfirmParameter
from click_prompt.core.parameter import FilePathParameter
from click_prompt.core.parameter import AutoCompleteParameter
from click_prompt.core.parameter import InputTextParameter


class ChoiceOption(ChoiceParameter, click.Option):
    """
    Option decorator for :class:`~click_prompt.core.parameter.ChoiceArgument`
    """


class ConfirmOption(ConfirmParameter, click.Option):
    """
    Option decorator for :class:`~click_prompt.core.parameter.ConfirmParameter`
    """


class FilePathOption(FilePathParameter, click.Option):
    """
    Option decorator for :class:`~click_prompt.core.parameter.PromptArgument`
    """


class AutoCompleteOption(AutoCompleteParameter, click.Option):
    """
    Option decorator for :class:`~click_prompt.core.parameter.AutoCompleteParameter`
    """


class InputTextOption(InputTextParameter, click.Option):
    """
    Option decorator for :class:`~click_prompt.core.parameter.InputTextParameter`
    """
