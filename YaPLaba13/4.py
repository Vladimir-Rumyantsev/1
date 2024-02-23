def read(f):
    with (open(f, 'rb') as file):
        packed_data = file.read()
        unpacked_numbers = [int.from_bytes(packed_data[i:i + 4], byteorder='little', signed=True)
                            for i in range(0, len(packed_data), 4)]
    return unpacked_numbers


numbers = list(map(int, input('Введите через пробел данные для файла-архива: ').split()))

with open('input_4.bin', 'wb') as file:
    for i in numbers:
        file.write(i.to_bytes(4, byteorder='little', signed=True))

unpack_start = read('input_4.bin')
print(f'\n{unpack_start}')

unpack = []
x = 0
try:
    while unpack_start:
        if x == 0:
            x = unpack_start[0]
            unpack_start.pop(0)
        else:
            A = []
            for i in range(x):
                A.append(unpack_start[0])
                unpack_start.pop(0)
            x = 0
            unpack.append(A)

    S1 = []
    S2 = []
    for i in unpack:
        S1.append(i[0])
        S2.append(i[-1])

    with open('S1.bin', 'wb') as file:
        for i in S1:
            file.write(i.to_bytes(4, byteorder='little', signed=True))
    with open('S2.bin', 'wb') as file:
        for i in S2:
            file.write(i.to_bytes(4, byteorder='little', signed=True))

    x = read('S1.bin')
    print(f'\n{x}')
    x = read('S2.bin')
    print(f'\n{x}')

except:
    print('Ошибка при вводе данных!')
