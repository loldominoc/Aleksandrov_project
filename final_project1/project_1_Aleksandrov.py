from random import randrange

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(map(str, row)) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


def enter_move(board):
    valid = False
    while not valid:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                valid = True
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def make_list_of_free_fields(board):
    return [(row_idx, col_idx) for row_idx, row in enumerate(board) for col_idx, value in enumerate(row) if value not in ['X', 'O']]


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = 'X'


def main():
    board = [[1 + 3 * i + j for j in range(3)] for i in range(3)]
    board[1][1] = 'X'
    while True:
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        elif victory_for(board, 'O'):
            print("You win!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        if len(make_list_of_free_fields(board)) % 2 == 0:
            enter_move(board)
        else:
            draw_move(board)


if __name__ == "__main__":
    main()
