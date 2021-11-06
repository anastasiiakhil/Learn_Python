morse_code = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
              "H": "....", "I": "..", "J": ".---", "K": "-.-",  "L": ".-..", "M": "--", "N": "-.",
              "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
              "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}


def encode_morze(text):
    text = text.upper()
    words = text.split(' ')
    str_new = ''
    for k in words:
        str_new = str_new + '____'
        for i in k:
            if i in morse_code:
                str_new = str_new + morse_code[i] + '__'
    str_new = str_new.replace('-', '^^^_')
    str_new = str_new.replace('.', '^_')
    return str_new[4:-3]

