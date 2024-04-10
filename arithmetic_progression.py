import random
import sys


number_of_numbers_to_play = 2018   # Натуральное число (количество чисел в игре)
n_low = 2
n_medium = 10


class Player:
    def __init__(self):
        self.myNodes = []

    def add_node(self, value):
        self.myNodes.append(value)
        database.append(value)


class Petya(Player):
    def __init__(self):
        super().__init__()


class Vasya(Player):
    def __init__(self):
        super().__init__()


def choosing_a_number_by_computer(diff=3):
    if diff == 1:
        rand = random.randint(1, n_low)
        if rand == 1:
            high_difficulty = False
        else:
            high_difficulty = True
    elif diff == 2:
        rand = random.randint(1, n_medium)
        if rand == 1:
            high_difficulty = False
        else:
            high_difficulty = True
    else:
        high_difficulty = True

    numbers_list = list(range(1, number_of_numbers_to_play + 1))
    random.shuffle(numbers_list)

    if not computer.myNodes:
        for i in numbers_list:
            if not (i in database):
                computer.add_node(i)
                return i

    elif len(computer.myNodes) == 1:
        if high_difficulty and len(player.myNodes) >= 2:
            dangerous_number = (player.myNodes[-1] - player.myNodes[-2]) + player.myNodes[-1]
            if (not (dangerous_number in database)) and (1 <= dangerous_number <= number_of_numbers_to_play):
                computer.add_node(dangerous_number)
                return dangerous_number

        for i in numbers_list:
            the_future_number = ((i - computer.myNodes[-1]) + i)

            if ((not (i in database)) and (not (the_future_number in database)) and
                    (1 <= the_future_number <= number_of_numbers_to_play)):
                computer.add_node(i)
                return i

        for i in numbers_list:
            if not (i in database):
                computer.add_node(i)
                return i

    elif len(computer.myNodes) >= 2:
        suitable_number = (computer.myNodes[-1] - computer.myNodes[-2]) + computer.myNodes[-1]
        if (not (suitable_number in database)) and (1 <= suitable_number <= number_of_numbers_to_play):
            computer.add_node(suitable_number)
            return suitable_number

        if high_difficulty and len(player.myNodes) >= 2:
            dangerous_number = (player.myNodes[-1] - player.myNodes[-2]) + player.myNodes[-1]
            if (not (dangerous_number in database)) and (1 <= dangerous_number <= number_of_numbers_to_play):
                computer.add_node(dangerous_number)
                return dangerous_number

        for i in numbers_list:
            the_future_number = ((i - computer.myNodes[-1]) + i)

            if ((not (i in database)) and (not (the_future_number in database)) and
                    (1 <= the_future_number <= number_of_numbers_to_play)):
                computer.add_node(i)
                return i

        for i in numbers_list:
            if not (i in database):
                computer.add_node(i)
                return i

    return None


def choosing_a_number_by_computer_2(diff=3):
    if diff == 1:
        rand = random.randint(1, n_low)
        if rand == 1:
            high_difficulty = False
        else:
            high_difficulty = True
    elif diff == 2:
        rand = random.randint(1, n_medium)
        if rand == 1:
            high_difficulty = False
        else:
            high_difficulty = True
    else:
        high_difficulty = True

    numbers_list = list(range(1, number_of_numbers_to_play + 1))
    random.shuffle(numbers_list)

    if not player.myNodes:
        for i in numbers_list:
            if not (i in database):
                player.add_node(i)
                return i

    elif len(player.myNodes) == 1:
        if high_difficulty and len(computer.myNodes) >= 2:
            dangerous_number = (computer.myNodes[-1] - computer.myNodes[-2]) + computer.myNodes[-1]
            if (not (dangerous_number in database)) and (1 <= dangerous_number <= number_of_numbers_to_play):
                player.add_node(dangerous_number)
                return dangerous_number

        for i in numbers_list:
            the_future_number = ((i - player.myNodes[-1]) + i)

            if ((not (i in database)) and (not (the_future_number in database)) and
                    (1 <= the_future_number <= number_of_numbers_to_play)):
                player.add_node(i)
                return i

        for i in numbers_list:
            if not (i in database):
                player.add_node(i)
                return i

    elif len(player.myNodes) >= 2:
        suitable_number = (player.myNodes[-1] - player.myNodes[-2]) + player.myNodes[-1]
        if (not (suitable_number in database)) and (1 <= suitable_number <= number_of_numbers_to_play):
            player.add_node(suitable_number)
            return suitable_number

        if high_difficulty and len(computer.myNodes) >= 2:
            dangerous_number = (computer.myNodes[-1] - computer.myNodes[-2]) + computer.myNodes[-1]
            if (not (dangerous_number in database)) and (1 <= dangerous_number <= number_of_numbers_to_play):
                player.add_node(dangerous_number)
                return dangerous_number

        for i in numbers_list:
            the_future_number = ((i - player.myNodes[-1]) + i)

            if ((not (i in database)) and (not (the_future_number in database)) and
                    (1 <= the_future_number <= number_of_numbers_to_play)):
                player.add_node(i)
                return i

        for i in numbers_list:
            if not (i in database):
                player.add_node(i)
                return i

    return None


if __name__ == '__main__':

    database = []

    x = input(f'\nИгра в арифметическую прогрессию!\n\nПетя и Вася по очереди выписывают на доску натуральные числа, '
              f'не превосходящие {number_of_numbers_to_play} (выписывать уже имеющееся число запрещено); начинает Петя.'
              f'\nЕсли после хода игрока на доске оказываются три числа, образующих арифметическую прогрессию, '
              f'этот игрок выигрывает.\n\nВыберете игрока (Петя или Вася).\n1. Петя\n2. Вася\nВедите число (1 или 2): ')
    difficulty = input('\nВыберите сложность игры.\n1. Лёгкая\n2. Средняя\n3. Сложная\nВведите число (1 или 3): ')

    if x == '2':
        player = Vasya()
        computer = Petya()
    else:
        player = Petya()
        computer = Vasya()

    if difficulty == '1':
        difficulty = 1
    elif difficulty == '2':
        difficulty = 2
    else:
        difficulty = 3

    if isinstance(computer, Petya):
        print(f'\n\nХод компьютера 2: {choosing_a_number_by_computer(difficulty)}')

    while True:

        if len(database) >= number_of_numbers_to_play:
            print('\nПобеда компьютера 2 через окончание доступных компьютеру 1 ходов!')
            print(f'\n{player.myNodes}\n{computer.myNodes}\n\n{sorted(player.myNodes)}\n{sorted(computer.myNodes)}')
            sys.exit()

        print(f'\n\nХод компьютера 1: {choosing_a_number_by_computer_2(difficulty)}')

        if (len(player.myNodes) >= 3 and
                (player.myNodes[-1] - player.myNodes[-2]) == (player.myNodes[-2] - player.myNodes[-3])):
            print('\nПобеда компьютера 1!')
            print(f'\n{player.myNodes}\n{computer.myNodes}\n\n{sorted(player.myNodes)}\n{sorted(computer.myNodes)}')
            sys.exit()

        if len(database) >= number_of_numbers_to_play:
            print('\nПобеда компьютера 1 через окончание доступных компьютеру 2 ходов!')
            print(f'\n{player.myNodes}\n{computer.myNodes}\n\n{sorted(player.myNodes)}\n{sorted(computer.myNodes)}')
            sys.exit()

        print(f'Ход компьютера 2: {choosing_a_number_by_computer(difficulty)}')

        if (len(computer.myNodes) >= 3 and
                (computer.myNodes[-1] - computer.myNodes[-2]) == (computer.myNodes[-2] - computer.myNodes[-3])):
            print('\nПобеда компьютера 2!')
            print(f'\n{player.myNodes}\n{computer.myNodes}\n\n{sorted(player.myNodes)}\n{sorted(computer.myNodes)}')
            sys.exit()

        while len(player.myNodes) >= 4:
            player.myNodes.pop(0)

        while len(computer.myNodes) >= 4:
            computer.myNodes.pop(0)
