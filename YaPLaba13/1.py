def read(f):
    with (open(f, 'rb') as file):
        binary_data = file.read()
        unpacked_numbers = [int.from_bytes(binary_data[i:i + 4], byteorder='little', signed=True)
                            for i in range(0, len(binary_data), 4)]
    return unpacked_numbers


numbers = []
n = int(input('\nВведите количество элементов в файле: '))
print()
for i in range(n):
    numbers.append(int(input('Введите новый элемент в файл: ')))
print()

with open('input_1.bin', 'wb') as file:
    for i in numbers:
        binary_data = i.to_bytes(4, byteorder='little', signed=True)
        file.write(binary_data)

unpack = read('input_1.bin')
print(unpack)

with open('output_1.bin', 'wb') as file:
    for i in range(len(unpack) - 1, -1, -1):
        number = unpack[i]
        binary_data = number.to_bytes(4, byteorder='little', signed=True)
        file.write(binary_data)

print()
print(read('output_1.bin'))
