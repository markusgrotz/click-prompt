"""
Module for defining the option decorators.
"""

import click

from click_prompt.core.option import ChoiceOption
from click_prompt.core.option import ConfirmOption
from click_prompt.core.option import FilePathOption
from click_prompt.core.option import AutoCompleteOption
from click_prompt.core.option import InputTextOption


def choice_option(*args, **kwargs):
    """
    Option decorator for :class:`~click_prompt.core.parameter.ChoiceParameter`
    """

    def decorator(f):
        return click.option(*args, **kwargs, cls=ChoiceOption)(f)

    return decorator


def confirm_option(*args, **kwargs):
    """
    Option decorator for :class:`~click_prompt.core.parameter.ConfirmParameter`
    """

    def decorator(f):
        return click.option(*args, **kwargs, cls=ConfirmOption)(f)

    return decorator


def filepath_option(*args, **kwargs):
    """
    Option decorator for :class:`~click_prompt.core.parameter.FilePathParameter`
    """

    def decorator(f):
        return click.option(*args, **kwargs, cls=FilePathOption)(f)

    return decorator


def auto_complete_option(*args, **kwargs):
    """
    Option decorator for :class:`~click_prompt.core.parameter.AutoCompleteParameter`
    """

    def decorator(f):
        return click.option(*args, **kwargs, cls=AutoCompleteOption)(f)

    return decorator


def input_text_option(*args, **kwargs):
    """
    Option decorator for :class:`~click_prompt.core.parameter.InputTextParameter`
    """

    def decorator(f):
        return click.option(*args, **kwargs, cls=InputTextOption)(f)

    return decorator
