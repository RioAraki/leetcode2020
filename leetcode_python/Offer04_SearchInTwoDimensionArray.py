def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
    if len(matrix) == 0 or len(matrix[0]) == 0: return False
    width = len(matrix[0])-1
    height = 0

    while 0 <= width and width < len(matrix[0]) and 0 <= height and height < len(matrix):
        if matrix[height][width] == target:
            return True
        elif matrix[height][width] > target:
            width -= 1
        else:
            height += 1

    return False
