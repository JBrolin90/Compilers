integer = "integer"; char = "char"; num = "num"
pointer = "^"
id = "id"
array="array"; LSqBracket="["; RSqBracket = "]"; dotdot=".."; of="of"
simple = [integer, char, num]



def IsSimple(token):
    return token in simple

def ProduceSimpleType(token):
    if not IsSimple(token): raise SyntaxError
    if token == num:
        token = MatchDotDot(NextToken())
        return MatchNum(token)
    return NextToken()

def ProducePointer(token):
    if token != pointer: raise SyntaxError
    if NextToken() != id: raise SyntaxError
    return NextToken()


def MatchArray(token): return match(token, array)
def MatchLSqBracket(token): return match(token, LSqBracket)
def MatchRSqBracket(token): return match(token, RSqBracket)
def MatchNum(token): return match(token, num)
def MatchOf(token): return match(token, of)
def MatchDotDot(token): return match(token, dotdot)
    

def ProduceArrayType(token):
    sequence = [MatchArray, MatchLSqBracket, ProduceSimpleType, MatchLSqBracket, MatchOf, ProduceSimpleType]
    for matchExpected in sequence:
        token = matchExpected(token)
    return token
    
def match(token, matchee):
    if token == matchee: return NextToken()
    raise SyntaxError


stream = [array, LSqBracket, num, dotdot, num, RSqBracket, of, integer ]

def NextToken():
    token = stream[0]
    stream = stream[1:]
    return token


def ProduceType(token):
    if IsSimple(token):
        token = ProduceSimpleType(token)
    elif token == pointer:
        token = ProducePointer(token)
    elif token == array:
        token = ProducePointer(token)
    else:
        raise SyntaxError
    return token


def main():
    ProduceType(NextToken())
    
