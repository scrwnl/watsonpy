from collections import deque
import numpy as np

class WatsonVmError(Exception):
    """
    Exception class for WATSON VM errors
    """



def parse(code:str):
    """
    Parse a string of WATSON code and return a list

    Parameters
    ----------
    code : str
        The string of WATSON code.

    Returns
    -------
    list
        The result of parsing
    """

    # WATSON Instructions
    INEW=['B','S']
    IINC=['u','h']
    ISHL=['b','a']
    IADD=['a','k']
    INEG=['A','r']
    ISHT=['e','A']
    ITOF=['i','z']
    ITOU=['\'','i']
    FINF=['q','m']
    FNAN=['t','b']
    FNEG=['p','u']
    SNEW=['?','$']
    SADD=['!','-']
    ONEW=['~','+']
    OADD=['M','g']
    ANEW=['@','v']
    AADD=['s','?']
    BNEW=['z','^']
    BNEG=['o','!']
    NNEW=['.','y']
    GDUP=['E','/']
    GPOP=['#','e']
    GSWP=['%',':']

    codeptr = 0
    stack = deque([])
    state = 0

    while codeptr < len(code):
        if code[codeptr] == INEW[state]:
            stack.append(0)

        elif code[codeptr] == IINC[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int:
                x = np.int64(x)
                stack.append((x+1).item())
            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == ISHL[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int:
                x = np.int64(x)
                stack.append((x<<1).item())
            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == IADD[state]:
            try:
                y = stack.pop()
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int and type(y) is int:
                y = np.int64(y)
                x = np.int64(x)
                stack.append((x+y).item())
            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == INEG[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int:
                x = np.int64(x)
                stack.append((-x).item())
            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == ISHT[state]:
            try:
                y = stack.pop()
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(y) is int and type(x) is int:
                y = np.int64(y)
                x = np.int64(x)
                stack.append((x << y).item())
            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == ITOF[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int:
                x = np.int64(x)
                stack.append(x.astype(np.float32).item())
            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == ITOU[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int:
                x = np.int64(x)
                stack.append(x.astype(np.uint64).item())

        elif code[codeptr] == FINF[state]:
            stack.append(float("inf"))

        elif code[codeptr] == FNAN[state]:
            stack.append(float("nan"))

        elif code[codeptr] == FNEG[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is float:
                stack.append(-x)

            else:
                raise WatsonVmError("Syntax Error")

        elif code[codeptr] == SNEW[state]:
            stack.append("")
            if state == 0:
                state = 1
            else:
                state = 0

        elif code[codeptr] == SADD[state]:
            try:
                x = stack.pop()
                s = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int and type(s) is str:
                s += chr(x)
                stack.append(s)

        elif code[codeptr] == ONEW[state]:
            stack.append({})

        elif code[codeptr] == OADD[state]:
            try:
                v = stack.pop()
                k = stack.pop
                o = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(k) is str and type(o) is dict:
                o[k] = v
                stack.append(o)

        elif code[codeptr] == ANEW[state]:
            stack.append([])

        elif code[codeptr] == AADD[state]:
            try:
                x = stack.pop()
                a = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is int and type(a) is list:
                a.append(x)
                stack.append(a)

        elif code[codeptr] == BNEW[state]:
            stack.append(False)

        elif code[codeptr] == BNEG[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            if type(x) is bool:
                stack.append(not x)

        elif code[codeptr] == NNEW[state]:
            stack.append(None)

        elif code[codeptr] == GDUP[state]:
            try:
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            stack.append(x)
            stack.append(x)

        elif code[codeptr] == GPOP[state]:
            try:
                stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

        elif code[codeptr] == GSWP[state]:
            try:
                y = stack.pop()
                x = stack.pop()
            except IndexError as exc:
                raise WatsonVmError("Syntax Error") from exc

            stack.append(y)
            stack.append(x)

        codeptr += 1
    return list(stack)
