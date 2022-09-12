from typing import Optional
from typing import Sequence
from typing import Union
from typing import Mapping
from typing import Any
from typing import Tuple

import click
from click.core import ParameterSource
from click.core import Context

from click_prompt.core.parameter import PromptParameter
from click_prompt.core.parameter import ChoiceParameter
from click_prompt.core.parameter import ConfirmParameter
from click_prompt.core.parameter import FilePathParameter
from click_prompt.core.parameter import AutoCompleteParameter


class PromptArgument(click.Argument, PromptParameter):
    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = None,
        prompt: Union[bool, str] = True,
        multiple: bool = False,
        **kwargs
    ):
        self.prompt = prompt
        super().__init__(param_decls, **kwargs)

    def consume_value(
        self, ctx: Context, opts: Mapping[str, Any]
    ) -> Tuple[Any, ParameterSource]:

        value = opts.get(self.name)  # type: ignore
        source = ParameterSource.COMMANDLINE

        if value is None:
            value = self.prompt_for_value(ctx)
            source = ParameterSource.PROMPT

        return value, source


class ChoiceArgument(ChoiceParameter, PromptArgument):
    pass


class ConfirmArgument(ConfirmParameter, PromptArgument):
    pass


class FilePathArgument(FilePathParameter, PromptArgument):
    pass


class AutoCompleteArgument(AutoCompleteParameter, PromptArgument):
    pass
