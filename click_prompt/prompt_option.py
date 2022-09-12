import click

from click_prompt.prompt_parameter import ChoiceParameter
from click_prompt.prompt_parameter import ConfirmParameter
from click_prompt.prompt_parameter import FilePathParameter
from click_prompt.prompt_parameter import AutoCompleteParameter


class ChoiceOption(ChoiceParameter, click.Option):
    pass

class ConfirmOption(ConfirmParameter, click.Option):
    pass

class FilePathOption(FilePathParameter, click.Option):
    pass

class AutoCompleteOption(AutoCompleteParameter, click.Option):
    pass



