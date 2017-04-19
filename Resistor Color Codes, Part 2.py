def convert_to_float(ohms_string):
    if ohms_string[len(ohms_string) - 1] == "k":
        return float(ohms_string[:-1]) * 1000

    elif ohms_string[len(ohms_string) - 1] == "M":
        return float(ohms_string[:-1]) * 1000000
    return float(ohms_string)


def encode_resistor_colors(ohms_string):
    code = {0: "black", 1: "brown", 2: "red", 3: "orange", 4: "yellow",
            5: "green", 6: "blue", 7: "violet", 8: "gray", 9: "white"}
    ohms_string = ohms_string.split(" ")[0]
    ohms_string = convert_to_float(ohms_string)
    result = []
    result.append(code[int(str(ohms_string)[0])])
    result.append(code[int(str(ohms_string)[1])])
    if ohms_string < 100:
        result.append("black")
    elif ohms_string >= 100 and ohms_string < 1000:
        result.append("brown")
    elif ohms_string >= 1000 and ohms_string < 10000:
        result.append("red")
    elif ohms_string >= 10000 and ohms_string < 100000:
        result.append("orange")
    elif ohms_string >= 100000 and ohms_string < 1000000:
        result.append("yellow")
    elif ohms_string >= 1000000 and ohms_string < 10000000:
        result.append("green")
    elif ohms_string >= 10000000 and ohms_string < 100000000:
        result.append("blue")
    elif ohms_string >= 100000000 and ohms_string < 1000000000:
        result.append("violet")
    elif ohms_string >= 1000000000 and ohms_string < 10000000000:
        result.append("grey")
    elif ohms_string >= 10000000000 and ohms_string < 100000000000:
        result.append("white")
    result.append("gold")
    result = " ".join(result)
    print(ohms_string)
    print(result)
    return result

encode_resistor_colors("62M ohms")
