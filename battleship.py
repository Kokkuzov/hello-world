import random

class Ship:
    def __init__(self, positions):
        self.positions = positions  # Список координат клеток корабля
        self.hits = set()  # Координаты подбитых частей корабля

    def is_sunk(self):
        """Проверяет, потоплен ли корабль."""
        return len(self.hits) == len(self.positions)

    def hit(self, position):
        """Регистрирует попадание в корабль."""
        if position in self.positions:
            self.hits.add(position)
            return True
        return False


class Board:
    def __init__(self, size=6):
        self.size = size
        self.ships = []
        self.board = [["O"] * size for _ in range(size)]
        self.attempts = set()  # Учет сделанных ходов

    def place_ship(self, length):
        """Размещает корабль на доске с учетом расстояния в одну клетку."""
        while True:
            vertical = random.choice([True, False])
            if vertical:
                start_row = random.randint(0, self.size - length)
                start_col = random.randint(0, self.size - 1)
                positions = [(start_row + i, start_col) for i in range(length)]
            else:
                start_row = random.randint(0, self.size - 1)
                start_col = random.randint(0, self.size - length)
                positions = [(start_row, start_col + i) for i in range(length)]

            # Проверка на расстояние в одну клетку от других кораблей
            if all(self.is_position_valid(pos) for pos in positions):
                ship = Ship(positions)
                self.ships.append(ship)
                for pos in positions:
                    self.board[pos[0]][pos[1]] = "■"
                break

    def is_position_valid(self, position):
        """Проверяет, можно ли разместить корабль в данной позиции."""
        row, col = position
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        # Проверка соседних клеток
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                r, c = row + dr, col + dc
                if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == "■":
                    return False
        return True

    def shoot(self, row, col):
        """Регистрирует выстрел по доске и возвращает результат."""
        if (row, col) in self.attempts:
            raise ValueError("Вы уже стреляли в эту клетку!")
        self.attempts.add((row, col))

        for ship in self.ships:
            if ship.hit((row, col)):
                self.board[row][col] = "X"
                if ship.is_sunk():
                    print("Корабль потоплен!")
                return True
        self.board[row][col] = "T"
        return False

    def all_ships_sunk(self):
        """Проверяет, потоплены ли все корабли на доске."""
        return all(ship.is_sunk() for ship in self.ships)

    def display(self, hide_ships=False):
        """Отображает доску в консоли."""
        print("   | " + " | ".join(str(i+1) for i in range(self.size)) + " |")
        print("  " + "-" * (self.size * 4 + 1))
        for i, row in enumerate(self.board):
            row_display = [
                "O" if hide_ships and cell == "■" else cell for cell in row
            ]
            print(f"{i + 1} | " + " | ".join(row_display) + " |")


class BattleshipGame:
    def __init__(self):
        self.size = 6
        self.player_board = Board(size=self.size)
        self.computer_board = Board(size=self.size)
        self.setup_boards()

    def setup_boards(self):
        """Устанавливает корабли на доски игрока и компьютера."""
        for length, count in [(3, 1), (2, 2), (1, 4)]:
            for _ in range(count):
                self.player_board.place_ship(length)
                self.computer_board.place_ship(length)

    def player_turn(self):
        """Ход игрока."""
        while True:
            try:
                row = int(input("Введите номер строки (1-6): ")) - 1
                col = int(input("Введите номер столбца (1-6): ")) - 1
                if self.computer_board.shoot(row, col):
                    print("Попадание!")
                else:
                    print("Мимо!")
                break
            except ValueError:
                print("Неправильный ввод или вы уже стреляли сюда. Попробуйте снова.")

    def computer_turn(self):
        """Ход компьютера (стреляет случайно по доске игрока)."""
        while True:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            try:
                if self.player_board.shoot(row, col):
                    print(f"Компьютер попал в ({row + 1}, {col + 1})!")
                else:
                    print(f"Компьютер промахнулся в ({row + 1}, {col + 1}).")
                break
            except ValueError:
                continue

    def play(self):
        """Основной игровой цикл."""
        print("Добро пожаловать в Морской бой!")
        while True:
            print("\nВаша доска:")
            self.player_board.display()
            print("\nДоска компьютера:")
            self.computer_board.display(hide_ships=True)

            self.player_turn()
            if self.computer_board.all_ships_sunk():
                print("Поздравляем, вы выиграли!")
                break

            self.computer_turn()
            if self.player_board.all_ships_sunk():
                print("Компьютер выиграл!")
                break


# Запуск игры
if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
