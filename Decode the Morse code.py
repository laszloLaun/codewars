def decodeMorse(morseCode):
    MORSE_CODE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "/",
        "SOS": "...---...",
        "!": "-.-.--",
        ".": ".-.-.-"
    }
    decode = []
    inverseMORSE_CODE = dict((v, k) for (k, v) in MORSE_CODE.items())

    morseCode.replace("   ", "*")
    print(morseCode)
    morseCode = morseCode.split(sep=" ")
    print(morseCode)
    space_count = 0
    for letter in morseCode:
        if letter != "":
            decode.append(inverseMORSE_CODE[letter])
            space_count = 0
        elif space_count == 0:
            decode.append(" ")
            space_count += 1
    if decode[0] == " ":
        del decode[0]
    if decode[len(decode) - 1] == " ":
        del decode[len(decode) - 1]
    print(decode)
    decode = "".join(decode)
    print(decode)

decodeMorse(' . ')
