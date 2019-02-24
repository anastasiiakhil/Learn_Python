import sys


text = sys.argv[1].lower()
text_1 = text.replace(" ", "")
text_2 = text_1[::-1]

if text_1 == text_2:
    print('YES')
else:
    print('NO')
