def clean_list(list_to_clean):
    s = []
    for i in range(len(list_to_clean)):
        if list_to_clean[i] in s and type(list_to_clean[i]) == type(s[s.index(list_to_clean[i])]):
            continue
        else:
            s.append(list_to_clean[i])
    return s
