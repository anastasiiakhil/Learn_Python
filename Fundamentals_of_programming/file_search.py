def file_search(folder, filename):
    result = str(folder[0]) + '/'
    for i in folder:
        if isinstance(i, str) & (i == filename):
            result = result + str(i)
            return result
        else:
            if isinstance(i, list):
                rec = file_search(i, filename)
                result = result + str(rec)
    if filename in result:
        return result.replace("False", "")
    else:
        return False
