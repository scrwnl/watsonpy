from collections import deque


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

    class SyntaxError(Exception):
        pass

    while codeptr < len(code):
        if code[codeptr] == INEW[state]:
            stack.append(0)

        elif code[codeptr] == IINC[state]:
            x = stack.pop()
            if type(x) is int:
                stack.append(x+1)
            else:
                raise SyntaxError()
            
        elif code[codeptr] == ISHL[state]:
            x = stack.pop()
            if type(x) is int:
                stack.append(x<<1)
            else:
                raise SyntaxError()
            
        elif code[codeptr] == IADD[state]:
            x = stack.pop()
            y = stack.pop()
            if type(x) is int and type(y) is int:
                stack.append(x+y)
            else:
                raise SyntaxError()
            
        elif code[codeptr] == INEG[state]:
            x = stack.pop()
            if type(x) is int:
                stack.append(-x)
            else:
                raise SyntaxError()
            
        elif code[codeptr] == ISHT[state]:
            x = stack.pop()

