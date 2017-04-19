import string
import random


def interpret(code):
    digits = string.digits
    code = code.split("\n")
    print(code)
    x = 0
    y = 0
    stack = []
    print(code[x][y])
    output = []
    direction = ""
    string_mode = False
    while code[x][y] != "@":
        if string_mode is True and code[x][y] != '"':             # string mode
            stack.append(ord(code[x][y]))
        elif code[x][y] == ",":                             # empties ascii values from stack and converts ascii values
            output = list(map(lambda x: chr(x), stack))     # to integer before gives the values to output
            stack = []
        elif code[x][y] in digits:          # 0123456789
            stack.append(int(code[x][y]))
        elif code[x][y] == ">":             # directions
            direction = "right"
        elif code[x][y] == "<":
            direction = "left"
        elif code[x][y] == "v":
            direction = "down"
        elif code[x][y] == "^":
            direction = "up"
        elif code[x][y] == "?":             # random directions
            direction = random.choice("right", "left", "up", "down")
        elif code[x][y] in "+-*/%'":        # aritmethics
            a = stack.pop()                 #
            b = stack.pop()                 #
            if code[x][y] == "+":
                stack.append(a + b)
            elif code[x][y] == "-":
                stack.append(b - a)
            elif code[x][y] == "*":
                stack.append(a * b)
            elif code[x][y] == "/":
                if a == 0:
                    stack.append(0)
                else:
                    stack.append(int(b / a))
            elif code[x][y] == "'":
                if b > a:
                    stack.append(1)
                else:
                    stack.append(0)
        elif code[x][y] in "!_|":
            a = stack.pop()
            if code[x][y] == "!":             # logical NOT
                if a == 0:
                    stack.append(1)
                else:
                    stack.append(0)
            elif code[x][y] == "_":  # conditional movement
                if a == 0:
                    y += 1
                    direction = "right"
                else:
                    y -= 1
                    direction = "left"
                continue
            elif code[x][y] == "|":
                if a == 0:
                    x += 1
                    direction = "down"
                else:
                    x -= 1
                    direction = "up"
                output.append(chr(a))
                continue
        elif code[x][y] == ":":
            if len(stack) == 0:
                stack.append(0)
            else:
                stack[len(stack) - 1] *= 2
        elif code[x][y] == '"':                     # enter string mode
            if string_mode is False:
                string_mode = True
            else:
                string_mode = False
        elif code[x][y] == ".":                     # empty numeric stack to output
            output = stack
            stack = []
        if direction == "right" and code[x][y] != "@":        # movement
            y += 1                                            #
        elif direction == "left" and code[x][y] != "@":       #
            y -= 1
        elif direction == "up" and code[x][y] != "@":
            x -= 1
        elif direction == "down" and code[x][y] != "@":
            x += 1

    # end of program
    if output[0] == "\n":
        output.append("H")
    output.reverse()
    output = list(map(lambda x: str(x), output))
    output = "".join(output)
    print(output)
    return output

interpret('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^')
# interpret('>987v>.v\nv456<  :\n>321 ^ _@')
