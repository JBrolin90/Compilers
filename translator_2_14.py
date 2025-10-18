from printer import Printer
plus = '+'; minus = "-"; empty = "<EOS>"



# create a module-level printer instance
printer = Printer(echo=True)


def expr(token):
    return rest(term(token))

def rest(token):
    if token == '+': out = plus
    elif token == '-': out = minus
    elif token == empty: return empty
    else:
        printer.write(token)
        message =  f"Expected valid operator but found '{token}'"
        raise SyntaxError(message)
        
    token = term(nextToken())
    printer.write(out)
    token = rest(token)
    return token    
                
def term(token):
    printer.write(token)
    if token.isdigit(): return nextToken()
    raise SyntaxError(f"Expected digit [0-9] but found '{token}'")

def nextToken():
    global stream
    if len(stream) < 1: return empty
    return stream.pop(0) 


stream = []

