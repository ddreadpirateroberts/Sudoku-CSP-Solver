from copy import deepcopy
from puzzles import *

Var = tuple[int, int]

class SudokuCSP: 
    def __init__(self, board: list, n: int = 9):
        self._feasibility_check(n)
        self.size = n 
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.dom = {(i, j): [k for k in range(1, n+1)] 
                    for i in range(n) for j in range(n)}
        self._load_board(board)
       
    def _feasibility_check(self, n: int):
        if n**.5 != int(n**.5):
            raise Exception("n is not fitting")
                 
    def _load_board(self, board: list): 
        for i, row in enumerate(board): 
            for j, val in enumerate(row): 
                if val != 0: 
                    self.set_var((i, j), val)
                    if not inference(self, (i, j)): 
                        raise Exception("invalid puzzle")
                    
    def is_complete(self):
        for i in range(self.size): 
            for j in range(self.size): 
                if self.board[i][j] == 0: 
                    return False
        return True
    
    def is_consistent(self, var: Var, val: int):
        for i in range(self.size):
            if self.board[i][var[1]] == val or self.board[var[0]][i] == val: 
                return False
        for el in self.get_box(var):
            if self.board[el[0]][el[1]] == val: 
                return False
        return True 
    
    def set_var(self, var: Var, val: int): 
        self.board[var[0]][var[1]] = val
        self.dom[var] = [val] 
        
    def get_box(self, var: Var): 
        n = int(self.size ** .5)
        sr, sc = var[0]//n*n, var[1]//n*n
        box = []
        for i in range(sr, sr+n): 
            for j in range(sc, sc+n):
                box.append((i, j))
        return box
    
    def get_neighbors(self, var: Var) -> list[Var]:
        neighbors = set()
        row, col = var 
        for i in range(self.size): 
            if i != col:
                neighbors.add((row, i))
            if i != row:
                neighbors.add((i,col))  
        for el in self.get_box(var): 
            if el != var: 
                neighbors.add(el)      
        return list(neighbors)
    
    def __str__(self):
        return '\n'.join(str(row) for row in self.board)
        
        
def get_arcs(sudoku: SudokuCSP, var: Var) -> list[tuple[Var, Var]]: 
    arcs = []
    for neighbor in sudoku.get_neighbors(var): 
        arcs.append((neighbor,var))
    return arcs 

def revise(sudoku: SudokuCSP, tail: Var, head: Var) -> bool:
    revised = False 
    if len(sudoku.dom[head]) == 1 and sudoku.dom[head][0] in sudoku.dom[tail]:
        sudoku.dom[tail].remove(sudoku.dom[head][0])
        revised = True
    return revised

def inference(sudoku: SudokuCSP, var: Var) -> bool:   
    "arc consistancy"   
    queue = get_arcs(sudoku, var)
    while queue: 
        tail, head = queue.pop(0)
        if revise(sudoku, tail, head): 
            if len(sudoku.dom[tail]) == 0: 
                return False
            for neighbor in sudoku.get_neighbors(tail): 
                queue.append((neighbor, tail))     
    return True

def minimum_remaining_value(sudoku: SudokuCSP, unassigned_vars: list) -> Var: 
    return min(unassigned_vars, key=lambda var: len(sudoku.dom[var]))

mrv = minimum_remaining_value
def select_unassigned_var(sudoku: SudokuCSP, heuristic=mrv) -> Var: 
    unassigned_vars = [(i, j) for i in range(sudoku.size) 
                       for j in range(sudoku.size) if sudoku.board[i][j] == 0]
    return heuristic(sudoku, unassigned_vars) 

def order_domain_values(sudoku: SudokuCSP, var: Var): 
    return sudoku.dom[var]
    
def recursive_backtraking(sudoku: SudokuCSP): 
    if sudoku.is_complete():
        return sudoku
    var = select_unassigned_var(sudoku)
    for value in order_domain_values(sudoku, var): 
        if sudoku.is_consistent(var, value): 
            org_dom = deepcopy(sudoku.dom)
            sudoku.set_var(var, value)
            infers = inference(sudoku, var) # adding inferences to csp
            if infers: 
                result = recursive_backtraking(sudoku)
                if result: 
                    return result
            sudoku.set_var(var, 0)
            sudoku.dom = org_dom # removing inferences from csp
    return False 
            
    
board = very_hard
sudoku = SudokuCSP(board)

print(recursive_backtraking(sudoku))
print(general_check(sudoku))
