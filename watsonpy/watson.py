"""watsonpy is a Python library for the WATSON Notation."""

from typing import Any
from .vm import *
import io


def loads(watson_code:str) -> Any:
    vm = WatsonVM()
    return vm.exec(lexer(watson_code))


def load(watsonFile:io.TextIOWrapper) -> Any:
    return loads(watsonFile.read())

def dumps(obj:Any) -> str:
    return ""

def dump(obj:str, watsonFile:io.TextIOWrapper) -> None:
    watsonFile.write(dumps(obj))
    return None
