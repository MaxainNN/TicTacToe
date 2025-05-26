from colorama import Fore,Back, Style

def draw_board(board: list[list[str]]) -> None:
    """Draws the Tic-Tac-Toe board with colored symbols and separators."""
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == " ":
                if y < len(board) - 1:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ", end='')
                else:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ")
            elif board[x][y] == "X":
                if y < len(board) - 1:
                    print(Fore.RED + 'X' + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.RED + 'X' + Style.RESET_ALL, "| ")
            elif board[x][y] == "0":
                if y < len(board) - 1:
                    print(Fore.BLUE + '0' + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.BLUE + '0' + Style.RESET_ALL, "| ")
        print("---------")


def ask_move(player: str, board: list[list[str]]) -> tuple[int, int]:
    """Asks the player for coordinates and validates the input.
        Returns valid (x, y) coordinates of an empty cell."""
    while True:
        try:
            x, y = (
                input(f"{player}, Enter x и y coordinates (e.g. 0 0): ")
                .strip()
                .split()
            )
            x, y = int(x), int(y)
            if (0 <= x < len(board)) and (0 <= y < len(board)) and (board[y][x] == " "):
                return x, y
            else:
                print(f"Cell {x} {y} is occupied or out of range. Try again.")
        except ValueError:
            print("Incorrect input. Enter two integers, separated by space.")


def make_move(player: str, board: list[list[str]], x: int, y: int) -> None:
    """Places the player's symbol ('X' or '0') at the specified coordinates."""
    board[y][x] = player


def ask_and_make_move(player: str, board: list[list[str]]) -> None:
    """Combines asking for and executing a move in one operation."""
    x, y = ask_move(player, board)
    make_move(player, board, x, y)


def check_win(player: str, board: list[list[str]]) -> bool:
    """Checks if the specified player has a winning combination.
    Returns True if the player has won."""
    for i in range(len(board)):
        if board[i] == [player, player, player]:
            return True

        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def tic_tac_toe(board: int) -> None:
    """Main game loop that manages turns, wins, and game restarts.
       Initializes a fresh board of the specified size (typically 3)."""
    while True:
        board = [[" " for i in range(board)] for j in range(board)]
        player = "X"

        while True:
            draw_board(board)
            ask_and_make_move(player, board)

            if check_win(player, board):
                print(f"{player} won!")
                break

            if all(cell != " " for row in board for cell in row):
                print("Draw!")
                break

            player = "0" if player == "X" else "X"

        restart = input("Want play one more time? (y/n)")
        if restart.lower() != "y":
            break


# Run main func to run game
tic_tac_toe(3)