from collections import deque
import numpy as np

class WatsonVmError(Exception):
    pass

def parse(code):
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
            x = stack.pop()
            if type(x) is int:
                x = np.int64(x)
                stack.append((x+1).item())
            else:
                raise WatsonVmError()
            
        elif code[codeptr] == ISHL[state]:
            x = stack.pop()
            if type(x) is int:
                x = np.int64(x)
                stack.append((x<<1).item())
            else:
                raise WatsonVmError()
            
        elif code[codeptr] == IADD[state]:
            y = stack.pop()
            x = stack.pop()
            if type(x) is int and type(y) is int:
                y = np.int64(y)
                x = np.int64(x)
                stack.append((x+y).item())
            else:
                raise WatsonVmError()
            
        elif code[codeptr] == INEG[state]:
            x = stack.pop()
            if type(x) is int:
                x = np.int64(x)
                stack.append((-x).item())
            else:
                raise WatsonVmError()
            
        elif code[codeptr] == ISHT[state]:
            y = stack.pop()
            x = stack.pop()
            if type(y) is int and type(x) is int:
                y = np.int64(y)
                x = np.int64(x)
                stack.append((x << y).item())
            else:
                raise WatsonVmError()
        
        elif code[codeptr] == ITOF[state]:
            x = stack.pop()
            if type(x) is int:
                x = np.int64(x)
                stack.append(x.astype(np.float32).item())
            else:
                raise WatsonVmError()
            
        elif code[codeptr] == ITOU[state]:
            x = stack.pop()
            if type(x) is int:
                x = np.int64(x)
                stack.append(x.astype(np.uint64).item())

        elif code[codeptr] == FINF[state]:
            stack.append(float("inf"))

        elif code[codeptr] == FNAN[state]:
            stack.append(float("nan"))

        elif code[codeptr] == FNEG[state]:
            x = stack.pop()
            if type(x) is float:
                stack.append(-x)

            else:
                raise WatsonVmError()

        elif code[codeptr] == SNEW[state]:
            stack.append("")
            if state == 0:
                state = 1
            else:
                state = 0

        elif code[codeptr] == SADD[state]:
            x = stack.pop()
            s = stack.pop()
            if type(x) is int and type(s) is str:
                s += chr(x)
                stack.append(s)

        elif code[codeptr] == ONEW[state]:
            stack.append({})

        elif code[codeptr] == OADD[state]:
            v = stack.pop()
            k = stack.pop
            o = stack.pop()
            if type(k) is str and type(o) is dict:
                o[k] = v
                stack.append(o)

        elif code[codeptr] == ANEW[state]:
            stack.append([])

        elif code[codeptr] == AADD[state]:
            x = stack.pop()
            a = stack.pop()
            if type(x) is int and type(a) is list:
                a.append(x)
                stack.append(a)

        elif code[codeptr] == BNEW[state]:
            stack.append(False)

        elif code[codeptr] == BNEG[state]:
            x = stack.pop()
            if type(x) is bool:
                stack.append(not x)

        elif code[codeptr] == NNEW[state]:
            stack.append(None)

        elif code[codeptr] == GDUP[state]:
            x = stack.pop()
            stack.append(x)
            stack.append(x)

        elif code[codeptr] == GPOP[state]:
            stack.pop()

        elif code[codeptr] == GSWP[state]:
            if len(stack) >= 2:
                y = stack.pop()
                x = stack.pop()
                stack.append(y)
                stack.append(x)
            else:
                raise WatsonVmError()
            
    return list(stack)
