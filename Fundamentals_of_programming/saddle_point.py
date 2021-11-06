def saddle_point(matrix):
    col_max = []
    row_min = []
    count_row_min = []
    count_col_max = []
    result = []
    for i in range(len(matrix)):
        row_min = min(matrix[i])
        count_row_min = matrix[i].count(row_min)
        if count_row_min == 1:
            index = matrix[i].index(row_min)
            col_max = max([row[index] for row in matrix])
            count_col_max = [row[index] for row in matrix].count(col_max)
            if count_col_max == 1:
                if row_min == col_max:
                    result = [i, index]
    if result == []:
        return False
    else:
        return tuple(result)
