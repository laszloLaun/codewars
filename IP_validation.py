def is_valid_IP(strng):
    print(strng)
    if type(strng) != str or strng == "":
        print(False)
        return False
    true_range = str(list(range(0, 256)))
    strng = strng.split(sep=".")
    if len(strng) != 4:
        print(False)
        return False
    for part in strng:
        if part not in true_range:
            print(False)
            return False
    print(True)
    return True

is_valid_IP("237.186.160.65")
