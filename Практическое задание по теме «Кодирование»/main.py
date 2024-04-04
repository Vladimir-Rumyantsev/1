alphabet = {' ': [0], 'А': [0], 'Б': [0], 'В': [0], 'Г': [0], 'Д': [0], 'Е': [0], 'Ж': [0], 'З': [0], 'И': [0],
            'Й': [0], 'К': [0], 'Л': [0], 'М': [0], 'Н': [0], 'О': [0], 'П': [0], 'Р': [0], 'С': [0], 'Т': [0],
            'У': [0], 'Ф': [0], 'Х': [0], 'Ц': [0], 'Ч': [0], 'Ш': [0], 'Щ': [0], 'Ъ': [0], 'Ы': [0], 'Ь': [0],
            'Э': [0], 'Ю': [0], 'Я': [0]}


class Node:
    def __init__(self, data=None, quantity=None):
        self.data = data
        self.quantity = quantity
        self.result = ''


def read_talks() -> str:
    with open('text.txt', 'r', encoding="utf-8") as file:
        arr = file.readlines()

    result = ''

    for i in arr:
        result = f'{result} {i[:-1]}'

    return result[1:]


def combining_probabilities(n):
    if n == 4:
        while len(database[0]) % 3 != 1:
            database[0].append(Node(['None'], 0))

    while len(database[-1]) >= n:
        database.append([])
        r = []

        for i in range(len(database[-2]) - n):
            database[-1].append(database[-2][i])

        for i in range(len(database[-2]) - n, len(database[-2])):
            r.append(database[-2][i])

        data = []
        quantity = 0
        for i in range(len(r)):
            for j in r[i].data:
                data.append(j)
            quantity += r[i].quantity
        database[-1].append(Node(data, quantity))

        database[-1] = sorted(database[-1], key=lambda x: -x.quantity)

    if n == 2 and is_prefix:
        for i in range(len(database) - 1, 0, -1):
            for j in database[i]:
                if database[i - 1][-1].data[0] in j.data:
                    database[i - 1][-1].result = f'{j.result}1'
                    database[i - 1][-2].result = f'{j.result}0'
    elif n == 2 and not is_prefix:
        for i in range(len(database) - 1, 0, -1):
            for j in database[i]:
                if database[i - 1][-1].data[0] in j.data:
                    database[i - 1][-1].result = f'1{j.result}'
                    database[i - 1][-2].result = f'0{j.result}'
    elif n == 4 and is_prefix:
        for i in range(len(database) - 1, 0, -1):
            for j in database[i]:
                if database[i - 1][-1].data[0] in j.data:
                    database[i - 1][-1].result = f'{j.result}3'
                    database[i - 1][-2].result = f'{j.result}2'
                    database[i - 1][-3].result = f'{j.result}1'
                    database[i - 1][-4].result = f'{j.result}0'
    elif n == 4 and not is_prefix:
        for i in range(len(database) - 1, 0, -1):
            for j in database[i]:
                if database[i - 1][-1].data[0] in j.data:
                    database[i - 1][-1].result = f'3{j.result}'
                    database[i - 1][-2].result = f'2{j.result}'
                    database[i - 1][-3].result = f'1{j.result}'
                    database[i - 1][-4].result = f'0{j.result}'


line = read_talks()
total = len(line)

len_alphabet = input('Введите количество символов в алфавите (2 или 4): ')
is_prefix = input('\nПрефиксное дерево или суффиксное?\nЕсли префиксное — введите "1"'
                  '\nЕсли суффиксное — введите "2"\nВаш ввод: ')

if len_alphabet == "4":
    len_alphabet = 4
else:
    len_alphabet = 2

if is_prefix == "2":
    is_prefix = False
else:
    is_prefix = True

for i in line:

    if i in [' ', '\n']:
        alphabet[' '][0] += 1
    else:
        alphabet[i.upper()][0] += 1

print('\n')

database = [[]]
for i in alphabet:
    database[0].append(Node([i], alphabet[i][0]))
database[0] = sorted(database[0], key=lambda x: -x.quantity)

for i in database[0]:
    print(f'{i.data}: {i.quantity}')

print('\n')

combining_probabilities(len_alphabet)

for i in database[0]:
    alphabet[i.data[0]].append(i.result)

for i in alphabet:
    print(f"'{i}': {alphabet[i]}")
