def funcname(string):
    for i in range(len(string)):
        if string[i] in string[i + 1:]:
            print("duplicates found")
            return "duplicates found"
    print("all unique")
    return "all unique"
funcname("hpkdweélxo")
