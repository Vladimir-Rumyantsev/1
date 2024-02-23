import struct


def read(f):
    with (open(f, 'rb') as file):
        packed_data = file.read()
        N = len(packed_data) // 4   # Можно определить количество байтов в списке (каждое число 4 байта)
        unpacked_data = struct.unpack('f' * N, packed_data)
    return unpacked_data


numbers = []
n = int(input('\nВведите количество элементов в файле: '))
print()
for i in range(n):
    numbers.append(float(input('Введите новый элемент в файл: ')))
print()


with open('input_2.bin', 'wb') as file:
    for i in numbers:
        file.write(struct.pack('f', i))


unpack = read('input_2.bin')
print(unpack)


with open('output_2.bin', 'wb') as file:
    output = float(0)
    for i in unpack:
        output += i
    output /= len(unpack)

    file.write(struct.pack('f', output))


print()
output = round(float(str(read('output_2.bin'))[1:-2]), n*3)
print(output)
