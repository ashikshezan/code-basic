def decrypt(encrypted_text):
    et = list(encrypted_text)
    first_char = et[0]
    et.remove(first_char)

    print(et)


def encrypt(text):
    encrypted_text = ""
    text = list(text)
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = list(i for i in range(10))
    symbol = '''.,:;-?! '()$%&"'''
    region = list(char) + list(char.lower()) + num + list(symbol)

    region_dict = {key: value for key, value in zip(
        region, {i for i in range(len(region))})}

    if text == "":
        return text
    for i in text:
        if i not in region:
            raise Exception

    # -----step 1------
    for i in range(len(text)):
        if i % 2 != 0:
            text[i] = text[i].swapcase()

    first = text[0]

    for i in range(len(text)-1):
        # if i == 0:
        #     continue

        char1 = text[i]
        try:
            char2 = text[i+1]
        except IndexError:
            pass

        diff = region_dict[char1] - region_dict[char2]

        if diff < 0:
            diff += 77
        # print(diff)
        try:
            text[i] = region[diff]
        except:
            pass
    text.pop()
    mirror = 76 - region_dict[first]
    text.append(region[mirror])

    for i in text:
        encrypted_text += str(i)

    return encrypted_text


print(encrypt("ABCDEFGHIJKLMNO"))
