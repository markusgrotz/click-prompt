"""
Module for defining the argument decorators.
"""

import click

from click_prompt.core.argument import ChoiceArgument
from click_prompt.core.argument import ConfirmArgument
from click_prompt.core.argument import FilePathArgument
from click_prompt.core.argument import AutoCompleteArgument
from click_prompt.core.argument import InputTextArgument


def choice_argument(*args, **kwargs):
    """
    Argument decorator for :class:`~click_prompt.core.parameter.ChoiceParameter`
    """

    def decorator(f):
        return click.argument(*args, **kwargs, cls=ChoiceArgument)(f)

    return decorator


def confirm_argument(*args, **kwargs):
    """
    Argument decorator for :class:`~click_prompt.core.parameter.ConfirmParameter`
    """

    def decorator(f):
        return click.argument(*args, **kwargs, cls=ConfirmArgument)(f)

    return decorator


def filepath_argument(*args, **kwargs):
    """
    Argument decorator for :class:`~click_prompt.core.parameter.FilePathParameter`
    """

    def decorator(f):
        return click.argument(*args, **kwargs, cls=FilePathArgument)(f)

    return decorator


def auto_complete_argument(*args, **kwargs):
    """
    Argument decorator for :class:`~click_prompt.core.parameter.AutoCompleteParameter`
    """

    def decorator(f):
        return click.argument(*args, **kwargs, cls=AutoCompleteArgument)(f)

    return decorator


def input_text_argument(*args, **kwargs):
    """
    Argument decorator for :class:`~click_prompt.core.parameter.InputTextParameter`
    """

    def decorator(f):
        return click.argument(*args, **kwargs, cls=InputTextArgument)(f)

    return decorator
