def minimum(matrix):
    
    if not matrix or not matrix[0]:
        return [None, None]
    
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            return [None, None]
        
    min_row_sum = float('inf')
    min_row_index = -1
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i

    min_col_sum = float('inf')
    min_col_index = -1
    for j in range(len(matrix[0])):
        col_sum = sum(matrix[i][j] for i in range(len(matrix)))
        if col_sum < min_col_sum:
            min_col_sum = col_sum
            min_col_index = j

    return [min_row_index, min_col_index]

print(minimum([
    [7, 2, 7, 2, 8],
    [2, 9, 4, 1, 7],
    [3, 8, 6, 2, 4],
    [2, 5, 2, 9, 1],
    [6, 6, 5, 4, 5]
]))

print(minimum([
    [-7, -2, -7, -2, -8],
    [-2, -9, -4, -1, -7],
    [-3, -8, -6, -2, -4],
    [-2, -5, -2, -9, -1],
    [-6, -6, -5, -4, -5]
]))
print(minimum([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]))
print(minimum([
    ['a', 'b', 0],
    [0, 1, 0],
    ['c', 0, 0]
]))