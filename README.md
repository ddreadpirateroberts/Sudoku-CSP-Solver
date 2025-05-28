# Sudoku-CSP-Solver

An intelligent Sudoku solver implementing Constraint Satisfaction Problem (CSP) techniques with advanced heuristics and constraint propagation.

## Algorithm Performance

- **Forward Checking**: Automatically eliminates conflicts in neighboring cells
- **Early Pruning**: Arc consistency detects dead ends quickly

## File Structure

```
├── sudoku.py          # Main CSP solver implementation
├── puzzles.py         # Validation functions and test puzzles
└── README.md          # This file
```

## Example Usage

```python
# Create a Sudoku CSP instance
board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 6, 0, 0, 0, 0, 0],
         # ... rest of puzzle
         ]

sudoku = SudokuCSP(board)

# Solve using CSP techniques  
solution = recursive_backtraking(sudoku)

# Validate solution
from puzzles import general_check
print(f"Valid solution: {general_check(solution)}")
```

## Technical Details

### CSP Components
- **Variables**: Grid cells (i, j)
- **Domains**: Possible values [1-9] for each cell
- **Constraints**: Row, column, and 3×3 box uniqueness

### Key Methods
- `is_consistent()`: Validates assignments against Sudoku rules
- `inference()`: Applies arc consistency for constraint propagation  
- `minimum_remaining_value()`: MRV heuristic for variable selection
- `recursive_backtraking()`: Main solving algorithm
