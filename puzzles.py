def general_check(sudoku): 
    return rows_check(sudoku) and columns_check(sudoku) and boxes_check(sudoku)
        
def rows_check(sudoku): 
    for i in range(sudoku.size):
        row_set = set()
        for j in range(sudoku.size):
            num = sudoku.board[i][j]
            if num in row_set: 
                return False 
            if num != 0: 
                row_set.add(num)
    return True

def columns_check(sudoku): 
    for i in range(sudoku.size):
        col_set = set()
        for j in range(sudoku.size):
            num = sudoku.board[j][i]
            if num in col_set: 
                return False                 
            if num != 0: 
                col_set.add(num)
    return True

def boxes_check(sudoku): 
    starting_pos = []
    n = int(sudoku.size ** .5)
    for i in range(0, sudoku.size-1, n): 
        for j in range(0, sudoku.size-1, n): 
            starting_pos.append((i, j))
    for r, c in starting_pos: 
        box_set = set()
        for i in range(r, r+n): 
            for j in range(c, c+n): 
                num = sudoku.board[i][j]
                if num != 0:
                    if num in box_set: 
                        return False
                    box_set.add(num)
    return True


easy =  [[0, 5, 3, 0, 0, 0, 7, 9, 0],
         [0, 0, 9, 7, 8, 2, 6, 0, 0],
         [0, 0, 0, 5, 0, 3, 0, 0, 0],
         [0, 0, 0, 4, 0, 6, 0, 0, 0],
         [0, 4, 0, 0, 0, 0, 0, 6, 0],
         [8, 0, 5, 1, 0, 9, 3, 0, 2],
         [0, 0, 8, 9, 3, 1, 4, 0, 0],
         [9, 0, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 4, 0, 0, 0, 8, 0, 0]]

medium = [[0, 0, 0, 0, 0, 0, 0, 9, 0],
          [0, 5, 0, 0, 0, 0, 2, 0, 1],
          [0, 0, 0, 0, 0, 7, 6, 0, 0],
          [0, 0, 0, 0, 4, 1, 5, 0, 0],
          [0, 0, 0, 6, 0, 0, 0, 0, 9],
          [0, 0, 6, 2, 0, 0, 4, 0, 7],
          [0, 7, 3, 1, 0, 6, 0, 0, 5],
          [9, 0, 0, 0, 0, 0, 0, 0, 2],
          [0, 4, 0, 0, 7, 9, 3, 8, 0]]

hard = [[2, 0, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [8, 0, 0, 0, 9, 0, 7, 2, 0],
        [7, 0, 1, 5, 2, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [4, 0, 6, 9, 1, 0, 0, 0, 3],
        [1, 0, 0, 0, 8, 0, 4, 6, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [9, 0, 7, 4, 0, 0, 0, 0, 0]]

very_hard = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 3, 6, 0, 0, 0, 0, 0],
             [0, 7, 0, 0, 9, 0, 2, 0, 0],
             [0, 5, 0, 0, 0, 7, 0, 0, 0],
             [0, 0, 0, 0, 4, 5, 7, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 3, 0],
             [0, 0, 1, 0, 0, 0, 0, 6, 8],
             [0, 0, 8, 5, 0, 0, 0, 1, 0],
             [0, 9, 0, 0, 0, 0, 4, 0, 0]]

most_difficult = [[0, 6, 1, 0, 0, 7, 0, 0, 3],
                  [0, 9, 2, 0, 0, 3, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 8, 5, 3, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 5, 0, 4],
                  [5, 0, 0, 0, 0, 8, 0, 0, 0],
                  [0, 4, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 6, 0, 8, 0, 0],
                  [6, 0, 0, 0, 0, 0, 0, 0, 0]]

sixteen_by_sixteen = [[0 for i in range(16)] for _ in range(16)]