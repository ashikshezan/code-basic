def decrypt_one(encrypted_text, n):
    encrypted_text = list(encrypted_text)
    ln = len(encrypted_text)
    for i in range(n):
        c = ln//2
        for i in range(ln):
            if i % 2 == 0:
                encrypted_text.insert(i, encrypted_text[c])
                del encrypted_text[c+1]
                c += 1
    else:
        return "".join(encrypted_text)


def encrypt_one(text, n):
    for i in range(n):
        second_char = text[1::2]
        others = text[::2]
        text = second_char+others
    else:
        return text


def decrypt(encrypted_text):
    pass
    # decoded_text = ""
    # for i, j in enumerate(encrypted_text):


def encrypt(text):
    text = list(text)
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = list(i for i in range(10))
    symbol = '''.,:;-?! '()$%&"'''
    region = list(char) + list(char.lower()) + num + list(symbol)

    region_dict = {key: value for key, value in zip(
        region, {i for i, j in enumerate(region)})}

    if text == "":
        return text
    for i in text:
        if i not in region:
            raise Exception

    # -----step 1------
    for i, j in enumerate(text):
        if i % 2 != 0:
            text[i] = text[i].swapcase()
    first = text[0]

    for i, _ in enumerate(text):
        if i == len(text)-1:
            continue
        char1 = text[i]
        char2 = text[i+1]
        diff = region_dict[char1] - region_dict[char2]
        if diff < 0:
            diff += 77
        text[i] = region[diff]

    text.pop()
    mirror = 76 - region_dict[first]
    text.insert(0, region[mirror])

    return "".join(map(str, text))
