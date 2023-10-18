from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    ROWS = len(input_board)
    COLS = len(input_board[0])

    if x >= ROWS or y >= COLS: return print('invalid coordinates')

    # Implement dfs for flood fill algo
    def dfs(x, y):
        # If out of range or done exchange, return right away
        if x < 0 or x >= ROWS or y < 0 or y >= COLS or input_board[x][y] != old:
            return
        # Change one item each time
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
        
        # Goes top, down, left, right
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    # If the starting point is not new ones yet, start calling our dfs function
    if input_board[x][y]!= new:
        dfs(x, y)

    return input_board

# Test cases
# modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
# modified_board = flood_fill(input_board=board, old=".", new="~", x=-5, y=200)
modified_board = flood_fill(input_board=board, old=".", new="~", x=0, y=0)

for a in modified_board:
    print(a)

# Time complexity: O(n*m), Space Complexity: O(n*m)
# n: length of rows, m: length of columns

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....