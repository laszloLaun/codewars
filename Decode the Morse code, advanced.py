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
        ".": ".-.-.-",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }
    decode = []
    inverseMORSE_CODE = dict((v, k) for (k, v) in MORSE_CODE.items())

    print(morseCode)
    morseCode = str(morseCode).split(sep=" ")
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
    return decode


def decodeBits(bits):
    BIT_CODE = {000000: "   ",
                000: " ",
                1: ".",
                111: "-"
                }
    ones = str(bits).split(sep="0")
    zeros = str(bits).split(sep="1")
    ones = list(filter(lambda x: len(x) > 0, ones))
    zeros = list(filter(lambda x: len(x) > 0, zeros))
    print(ones)
    print(zeros)
    if len(ones) != 0 and len(zeros) != 0:
        if len(min(ones)) < len(min(zeros)):
            shortest = len(min(ones))
        else:
            shortest = len(min(zeros))
    elif len(ones) == 0 and len(zeros) == 0:
        return ""
    elif len(ones) == 0:
        shortest = len(min(zeros))
    elif len(zeros) == 0:
        shortest = len(min(ones))
    print(shortest)
    bits = str(bits).replace(shortest * "000000",
                             "   ").replace(shortest * "000",
                                            " ").replace(shortest * "111",
                                                         "-").replace(shortest * "1",
                                                                      ".").replace(shortest * "0",
                                                                                   "").replace("0", "")
    print(bits)
    return decodeMorse(bits)

# decodeBits(1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011)
decodeBits("01110")
