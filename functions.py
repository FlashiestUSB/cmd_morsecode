ALPHA = {
    "A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.", "G": "__.", "H": "....", "I": "..",
    "J": ".___", "K": "_._", "L": "._..", "M": "__", "N": "_.", "O": "___", "P": ".__.", "Q": "__._", "R": "._.",
    "S": "...", "T": "_", "U": ".._", "V": "..._", "W": ".__", "X": "_.._", "Y": "_.__", "Z": "__..", "1": ".____",
    "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...", "8": "___..", "9": "____.",
    "0": "_____", "?": "..__..", "!": "_._.__", ".": "._._._", ",": "__..__", ";": "_._._.", ":": "___...",
    "+": "._._.", "-": "_...._", "/": "_.._.", "=": "_..._", "'": ".----."
}


def encode_message(message):
    morse_list = []
    for letter in message:
        if letter == " ":
            morse_list.append("   ")
        else:
            coded = ALPHA[letter]
            morse_list.append(coded)
    # print(morse_list)
    output = ""
    for letter in morse_list:
        output += letter
        output += " "

    print(output)


def decode_message(message):
    output = message
    o_lists = output.split("   ")
    # print(o_lists)
    new = ""
    for item in o_lists:
        new += item
    # print(new)
    new2 = new.split("  ")
    # print(new2)
    convert = []
    for item in new2:
        # print(item)
        for letter in item.split(" "):
            # print(letter)
            convert.append(letter)
        convert.append(" ")
    # print(convert)
    output2 = []
    for letter in convert:
        if letter == " ":
            output2.append(" ")
        elif letter == "":
            pass
        else:
            output2.append([list(ALPHA.values()).index(letter)])
    # print(output2)
    now = ""
    for item in output2:
        if item == " ":
            now += " "
        else:
            now += list(ALPHA.keys())[item[0]]
    print(now.title())
