from functools import wraps
import click

from click_prompt.core.argument import ChoiceArgument
from click_prompt.core.argument import ConfirmArgument
from click_prompt.core.argument import FilePathArgument
from click_prompt.core.argument import AutoCompleteArgument


def choice_argument(*args, **kwargs):
    def decorator(f):
        return click.argument(*args, **kwargs, cls=ChoiceArgument)(f)

    return decorator


def confirm_argument(*args, **kwargs):
    def decorator(f):
        return click.argument(*args, **kwargs, cls=ConfirmArgument)(f)

    return decorator


def filepath_argument(*args, **kwargs):
    def decorator(f):
        return click.argument(*args, **kwargs, cls=FilePathArgument)(f)

    return decorator


def auto_complete_argument(*args, **kwargs):
    def decorator(f):
        return click.argument(*args, **kwargs, cls=AutoCompleteArgument)(f)

    return decorator
