from collections import deque
from typing import Any

class StackUnderFlowException(Exception):
    pass

class InvalidTypeException(Exception):
    pass


class WatsonVM():
    def __init__(self) -> None:
        self.stack = deque([])
    
    def exec(self, opcode_list:list) -> Any:
        for opcode in opcode_list:
            opcode(self.stack)
        return list(self.stack)[0]



def inew(stack:deque) -> None:
    stack.append(0)
    return

def iinc(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is int):
            stack.append(x+1)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def ishl(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is int):
            stack.append(x<<1)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def iadd(stack:deque) -> None:
    if(len(stack) >= 2):
        y = stack.pop()
        x = stack.pop()
        if(type(x) is int and type(y) is int):
            stack.append(x+y)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def ineg(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is int):
            stack.append(-x)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def isht(stack:deque) -> None:
    if(len(stack) >= 2):
        y = stack.pop()
        x = stack.pop()
        if(type(x) is int and type(y) is int):
            stack.append(x<<y)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def itof(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is int):
            stack.append(float(x))
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def itou(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is int):
            stack.append(x)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def finf(stack:deque) -> None:
    stack.append(float('inf'))
    return

def fnan(stack:deque) -> None:
    stack.append(float('nan'))
    return

def fneg(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is float):
            stack.append(-x)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def snew(stack:deque) -> None:
    stack.append("")
    return

def sadd(stack:deque) -> None:
    if(len(stack) >= 2):
        x = stack.pop()
        s = stack.pop()
        if(type(x) is int and type(s) is str):
            stack.append(s+chr(x & 0xFF))
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def onew(stack:deque) -> None:
    stack.append({})
    return

def oadd(stack:deque) -> None:
    if(len(stack) >= 3):
        v = stack.pop()
        k = stack.pop()
        o = stack.pop()
        if(type(k) is str and type(o) is dict):
            o[k] = v
            stack.append(o)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def anew(stack:deque) -> None:
    stack.append([])
    return

def aadd(stack:deque) -> None:
    if(len(stack) >= 2):
        x = stack.pop()
        a = stack.pop()
        if(type(a) is list):
            a.append(x)
            stack.append(a)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def bnew(stack:deque) -> None:
    stack.append(False)
    return

def bneg(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        if(type(x) is bool):
            stack.append(not x)
        else:
            raise InvalidTypeException()
    else:
        raise StackUnderFlowException()
    return

def nnew(stack:deque) -> None:
    stack.append(None)
    return

def gdup(stack:deque) -> None:
    if(len(stack) >= 1):
        x = stack.pop()
        stack.append(x)
        stack.append(x)
    else:
        raise StackUnderFlowException()
    return

def gpop(stack:deque) -> None:
    if(len(stack) >= 1):
        stack.pop()
    else:
        raise StackUnderFlowException()
    return

def gswp(stack:deque) -> None:
    if(len(stack) >= 2):
        y = stack.pop()
        x = stack.pop()
        stack.append(y)
        stack.append(x)
    else:
        raise StackUnderFlowException()
    return



def lexer(watson_code:str) -> list:
    instructions = [{
        'B': "inew",
        'u': "iinc",
        'b': "ishl",
        'a': "iadd",
        'A': "ineg",
        'e': "isht",
        'i': "itof",
        '\'': "itou",
        'q': "finf",
        't': "fnan",
        'p': "fneg",
        '?': "snew",
        '!': "sadd",
        '~': "onew",
        'M': "oadd",
        '@': "anew",
        's': "aadd",
        'z': "bnew",
        'o': "bneg",
        '.': "nnew",
        'E': "gdup",
        '#': "gpop",
        '%': "gswp"
         },
         {
        'S': "inew",
        'h': "iinc",
        'a': "ishl",
        'k': "iadd",
        'r': "ineg",
        'A': "isht",
        'z': "itof",
        'i': "itou",
        'm': "finf",
        'b': "fnan",
        'u': "fneg",
        '$': "snew",
        '-': "sadd",
        '+': "onew",
        'g': "oadd",
        'v': "anew",
        '?': "aadd",
        '^': "bnew",
        '!': "bneg",
        'y': "nnew",
        '/': "gdup",
        'e': "gpop",
        ':': "gswp"
        }]
    
    opcodes = {
    "inew": inew,
    "iinc": iinc,
    "ishl": ishl,
    "iadd": iadd,
    "ineg": ineg,
    "isht": isht,
    "itof": itof,
    "itou": itou,
    "finf": finf,
    "fnan": fnan,
    "fneg": fneg,
    "snew": snew,
    "sadd": sadd,
    "onew": onew,
    "oadd": oadd,
    "anew": anew,
    "aadd": aadd,
    "bnew": bnew,
    "bneg": bneg,
    "nnew": nnew,
    "gdup": gdup,
    "gpop": gpop,
    "gswp": gswp
    }

    output = []
    state = 0
    for inst in list(watson_code):
        if(instructions[state].get(inst) is not None):
            output.append(opcodes[instructions[state][inst]])
        if(state==0 and inst=='?'):
            state = 1
        elif(state==1 and inst=='$'):
            state = 0
    return output
