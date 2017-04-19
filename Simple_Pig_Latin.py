import string


def pig_it(text):
    text = text.split(sep=" ")
    print(text)
    pigged_text = []
    for word in text:
        if word in string.punctuation:
            pigged_text.append(word)
        else:
            pigged_text.append(word[1:] + word[0:1] + "ay")
    pigged_text = " ".join(pigged_text)
    print(pigged_text)
    return pigged_text


pig_it('Quis custodiet ipsos custodes ?')
