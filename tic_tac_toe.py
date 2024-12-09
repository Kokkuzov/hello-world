board = [' ' for _ in range(9)]

def print_board():
    print("-------------")
    for i in range(3):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print("-------------")

def check_winner():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in win_combinations:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return board[line[0]]
    return 'Draw' if ' ' not in board else None

def is_valid_move(move):
    return 0 <= move < 9 and board[move] == ' '

def play_game():
    current_player = 'X'
    while True:
        print_board()
        try:
            move = int(input(f"Игрок {current_player}, введите позицию (1-9): ")) - 1
            if move < 0 or move > 8:
                print(f"Неверная позиция! Игрок {current_player}, введите позицию (1-9): ")
                continue
            if not is_valid_move(move):
                print("Позиция занята. Попробуйте снова.")
                continue
            board[move] = current_player
            winner = check_winner()
            if winner:
                print_board()
                if winner == 'Draw':
                    print("Ничья!")
                else:
                    print(f"Игрок {winner} победил!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Пожалуйста, введите целое число от 1 до 9.")
play_game()