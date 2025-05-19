def solve_n_queen(n):
    result = []

    def is_safe(row, col, queen):
        for r in range(row):
            c = queen[r]  # column where the queen was placed in previous row

            if c == col or abs(c - col) == abs(r - row):  # same column or same diagonal
                return False
        return True
    
    def backtrack(row, queen):
        if row == n:
            result.append(queen[:])  # store a copy of the current solution
            return
        
        for col in range(n):  # try every column in the current row
            if is_safe(row, col, queen):
                queen.append(col)  # place the queen
                backtrack(row + 1, queen)  # move to the next row
                queen.pop()  # backtrack: remove the queen

    backtrack(0, [])
    return result

def print_boards(solution, n):
    for sol in solution:
        for col in sol:
            row = ['.'] * n
            row[col] = 'Q'  # place the queen at the saved position
            print(''.join(row))
        print()

n = 4
solutions = solve_n_queen(n)
print(f'Number of solutions for N={n}: {len(solutions)}')
print_boards(solutions, n)
