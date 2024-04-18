import random


def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    placed_mines = 0
    while placed_mines < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if board[row][col] != '*':
            board[row][col] = '*'
            placed_mines += 1

    return board


def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == '*':
                count += 1
    return count



def reveal_square(board, revealed, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or revealed[row][col] == True:
        return
    revealed[row][col] = True

    if board[row][col] == ' ':
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                reveal_square(board, revealed, i, j)


def print_board(revealed):
    for row in revealed:
        print(" | ".join(['*' if val else ' ' for val in row]))
        print("-" * 24)


def main():
    rows = 6
    cols = 6
    num_mines = 6
    board = create_board(rows, cols, num_mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]



    game_over = False

    while not game_over:
        print_board(revealed)
        row = int(input("请输入要揭开的行号："))
        col = int(input("请输入要揭开的列号："))

        if board[row][col] == '*':
            print("很遗憾，你踩到了地雷！")
            revealed[row][col] = True
        else:
            reveal_square(board, revealed, row, col)



        all_revealed = all(all(revealed[i][j] or board[i][j] == '*' for j in range(cols)) for i in range(rows))
        if all_revealed:
            print("恭喜你，你成功扫雷！")
            game_over = True



if __name__ == "__main__":
    main()

