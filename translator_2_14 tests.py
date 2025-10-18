from printer import Printer
from translator_2_14 import expr, nextToken, stream, printer
plus = '+'; minus = "-"; empty = "<EOS>"



def testStream(inStream):
    stream.clear()
    stream.extend(inStream)
    for c in inStream: printer.write(c)
    printer.write(" -> ")
    try:
        expr(nextToken())
        col = printer.column()
        col = 30-col
        printer.write(" "*col + "SUCCESS ")
    except SyntaxError as e:
        col = printer.column()
        col = 30-col
        printer.print(" " * col + f"FAILURE: Syntax Error: {e}", end="")
    finally:
        printer.print()   # newline


def testMe():
    print("------------ VALID INPUTS ------------")
 
    validExpression = ["9", "-", "5", "+", "2"]
    testStream(validExpression)

    minimalValidInput = ["7"]
    testStream(minimalValidInput)

    longValidExpr = ["1", "+", "2", "-", "3", "+", "4"]
    testStream(longValidExpr)


    print("\n----------- INVALID INPUTS ------------")

    badStream = ["a", "-", "5", "+", "2"]
    testStream(badStream)

    badStream = ["9", "b", "5", "+", "2"]
    testStream(badStream)

    badStream = []
    testStream(badStream)

    
    # Expression ending with operator (incomplete)
    incompleteExpr = ["5", "+"]
    testStream(incompleteExpr)
    
    # Multiple operators in sequence (invalid)
    doubleOperator = ["3", "+", "-", "2"]
    testStream(doubleOperator)
    
    # Only an operator (no digits)
    operatorOnly = ["+"]
    testStream(operatorOnly)

    trailingOperator = ["5", "+", "3", "-"]
    testStream(trailingOperator)    

if __name__ == "__main__": testMe()