import string


def play_pass(s, n):
    print(s, n)
    s = list(s)
    ascii_uppercase = string.ascii_uppercase
    str_digits = string.digits
    unicode_limit = len(ascii_uppercase)
    count = 0
    for char in s:
        if char in ascii_uppercase:
            if (ascii_uppercase).index(char) + n >= unicode_limit:
                s[count] = ascii_uppercase[n - (unicode_limit - (ascii_uppercase).index(char))]
            else:
                s[count] = ascii_uppercase[(ascii_uppercase).index(char) + n]

        elif char in str_digits:
            s[count] = str(9 - int(char))
        count += 1
    count = 1
    for char in s:
        if char in ascii_uppercase:
            if count % 2 == 0:
                s[count - 1] = s[count - 1].lower()
        count += 1
    s = s[::-1]
    s = "".join(s)
    print(s)
    return s


play_pass("TO BE HONEST WITH YOU I DON'T USE THIS TEXT TOOL TOO OFTEN BUT HEY... MAYBE YOUR NEEDS ARE DIFFERENT.", 5)
