import re

key = 'aaaaabbbbbabbbaabbababbaaababaabaaaa'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

word = input('')
text_repl = word.replace(" ", "")


def transformation(text):
    res = []
    for i in text:
        if i.isupper():
            res.append('b')
        else:
            res.append('a')
    return res


def finding(i):
    for k in range(len(key)):
        lit = key[k:k+5]
        if i == lit:
            code = alphabet[k]
            return code


text_transf = transformation(text_repl)
new_res = "".join(text_transf)
text_ab = re.findall('.....', new_res)

final = []
for i in text_ab:
    new = finding(i)
    final.append(new)
print("".join(final))
