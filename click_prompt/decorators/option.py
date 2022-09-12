from functools import wraps
import click

from click_prompt.core.option import ChoiceOption
from click_prompt.core.option import ConfirmOption
from click_prompt.core.option import FilePathOption
from click_prompt.core.option import AutoCompleteOption


def choice_option(*args, **kwargs):
    def decorator(f):
        return click.option(*args, **kwargs, cls=ChoiceOption)(f)

    return decorator


def confirm_option(*args, **kwargs):
    def decorator(f):
        return click.option(*args, **kwargs, cls=ConfirmOption)(f)

    return decorator


def filepath_option(*args, **kwargs):
    def decorator(f):
        return click.option(*args, **kwargs, cls=FilePathOption)(f)

    return decorator


def auto_complete_option(*args, **kwargs):
    def decorator(f):
        return click.option(*args, **kwargs, cls=AutoCompleteOption)(f)

    return decorator
