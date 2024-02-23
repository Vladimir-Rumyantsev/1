import struct


def read(f):
    with (open(f, 'rb') as file):
        packed_data = file.read()
        unpacked_numbers = [int.from_bytes(packed_data[i:i + 4], byteorder='little', signed=True)
                            for i in range(0, len(packed_data), 4)]
    return unpacked_numbers



numbers = []
n = int(input('\nВведите количество элементов в файле: '))
print()
for i in range(n):
    numbers.append(int(input('Введите новый элемент в файл: ')))


with open('input_3.bin', 'wb') as file:
    for i in numbers:
        file.write(i.to_bytes(4, byteorder='little', signed=True))


unpack_start = read('input_3.bin')
print(f'\n{unpack_start}')

unpack = []
for i in range(len(unpack_start)):
    unpack.append(unpack_start[i])
    if (i % 2) != 0:
        unpack.append(unpack_start[i])


with open('output_3.bin', 'wb') as file:
    for i in unpack:
        file.write(i.to_bytes(4, byteorder='little', signed=True))

x = read('output_3.bin')
print(f'\n{x}')
