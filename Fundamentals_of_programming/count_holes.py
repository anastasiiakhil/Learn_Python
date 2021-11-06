def count_holes(n):
    if isinstance(n, str) | isinstance(n, int):
        n = list(str(int(n)))
        d = {0: 1, 4: 1, 6: 1, 8: 2, 9: 1}
        val = []
        if '-' in n:
            n_clear = n.remove('-')
        else:
            n_clear = n
        for i in n_clear:
            int_i = int(i)
            if int_i in d:
                val.append(d[int_i])
        return sum(val)
    else:
        return ('ERROR')
