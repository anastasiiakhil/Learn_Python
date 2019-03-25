def counter(a, b):
    s = []
    if type(a) == type(b) == int:
        if a >= 0:
            if b >= 0:
                a = list(str(a))
                b = list(str(b))
                for i in b:
                    if i in a:
                        s.append(i)
                return len(set(s))
