import sys

text = sys.argv[1:]
text_1 = text[::-1]
text_2 = ' '.join(text_1)
print(text_2)
