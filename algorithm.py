import random

# Создание поля
field = []
for i in range(10):

    if i == 0:
        field.append(["#", "#", "#", "#", ".", "#", "#", "#", "#", "#"])
    if i == 1:
        field.append(["#", "#", "#", "#", ".", "#", "#", "#", "#", "#"])
    if i == 2:
        field.append(["#", ".", ".", ".", ".", ".", ".", ".", "#", "#"])
    if i == 3:
        field.append(["#", ".", "#", "#", ".", "#", "#", ".", "#", "#"])
    if i == 4:
        field.append(["#", ".", ".", ".", ".", "#", "#", ".", "#", "#"])
    if i == 5:
        field.append(["#", "#", "#", ".", "#", "#", ".", ".", ".", "#"])
    if i == 6:
        field.append(["#", "#", "#", ".", ".", ".", ".", "#", "#", "#"])
    if i == 7:
        field.append(["#", "#", "#", "#", ".", "#", ".", "#", "#", "#"])
    if i == 8:
        field.append(["#", "#", ".", ".", ".", "#", ".", ".", ".", "#"])
    if i == 9:
        field.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

for n in range(2):
    block_row = random.randint(2, 8)
    block_col = random.randint(2, 8)
    if field[block_row][block_col] == ".":
        field[block_row][block_col] = "&"


# Расположение квадратика на поле
player_row = 1
player_col = 4
field[1][4] = "X"

# Расположение выхода на поле
exit_row = 0
exit_col = 4
field[0][4] = "O"

# Вывод поля на экран
for row in field:
    print(" ".join(row))
print('\n')


def traverse_maze(field):
    # стартовая позиция игрока
    player_row = 1
    player_col = 4

    red = "\033[31m"
    reset = "\033[0m"

    # помечаем стартовую позицию как пройденную
    field[player_row][player_col] = "{}V{}".format(red, reset)

    # инициализируем стек для отслеживания посещенных ячеек
    stack = [(player_row, player_col)]

    # продолжаем до тех пор, пока не будут посещены все ячейки
    while stack:
        # находим следующую ячейку для посещения
        current_row, current_col = stack.pop()

        # проверка, является ли текущая ячейка выходом
        if current_row == 0 and current_col == 4:
            print("Вы вышли из форта!")
            break

        # проверка соседних ячеек и добавление их в стек, если они не являются препятствиями или уже посещены
        if current_row > 0 and field[current_row - 1][current_col] != "#" and field[current_row - 1][current_col] != "&"\
                and field[current_row - 1][current_col] != "{}V{}".format(red, reset):
            stack.append((current_row - 1, current_col))
            field[current_row - 1][current_col] = "{}V{}".format(red, reset)
            for row in field:
                print(" ".join(row))
            print('\n')
        if current_row < 9 and field[current_row + 1][current_col] != "#" and field[current_row + 1][current_col] != "&"\
                and field[current_row + 1][current_col] != "{}V{}".format(red, reset):
            stack.append((current_row + 1, current_col))
            field[current_row + 1][current_col] = "{}V{}".format(red, reset)
            for row in field:
                print(" ".join(row))
            print('\n')
        if current_col > 0 and field[current_row][current_col - 1] != "#" and field[current_row][current_col - 1] != "&"\
                and field[current_row][current_col - 1] != "{}V{}".format(red, reset):
            stack.append((current_row, current_col - 1))
            field[current_row][current_col - 1] = "{}V{}".format(red, reset)
            for row in field:
                print(" ".join(row))
            print('\n')
        if current_col < 9 and field[current_row][current_col + 1] != "#" and field[current_row][current_col + 1] != "&"\
                and field[current_row][current_col + 1] != "{}V{}".format(red, reset):
            stack.append((current_row, current_col + 1))
            field[current_row][current_col + 1] = "{}V{}".format(red, reset)
            for row in field:
                print(" ".join(row))
            print('\n')

    # вывод финального пройденного лабиринта
    for row in field:
        print(" ".join(row))
    print('\n')


# вызов функции решения лабиринта
traverse_maze(field)
