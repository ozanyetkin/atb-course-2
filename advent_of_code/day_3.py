def data_reader(file_name):
    with open(f'./inputs/{file_name}.txt') as file:
        lines = file.readlines()

    parsed_data = []
    for data in lines:
        data = data.replace("\n", "")
        parsed_data.append(data)
    return parsed_data

binary_data = data_reader("day_3")

bit_totals = {}
for i in range(len(binary_data[0])):
    bit_totals[i] = 0

for binary in binary_data:
    for i, bit in enumerate(binary):
        bit_totals[i] += int(bit)

gamma = ""
epsilon = ""
for value in bit_totals.values():
    if value > len(binary_data) // 2:
        gamma += "1"
        epsilon += "0"
    elif value < len(binary_data) // 2:
        gamma += "0"
        epsilon += "1"

def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(binary[::-1]):
        decimal += (2 ** i) * int(bit)
    return decimal

print(binary_to_decimal(gamma) * binary_to_decimal(epsilon))

def most_common(position, binary_list):
    count_0 = 0
    count_1 = 0
    for binary in binary_list:
        if binary[position] == "0":
            count_0 += 1
        elif binary[position] == "1":
            count_1 += 1
    if count_0 > count_1:
        return 0
    elif count_0 == count_1:
        return -1
    elif count_0 < count_1:
        return 1

def life_support(support_type, position=0, binary_list=binary_data):
    if len(binary_list) == 1:
        return binary_list.pop()
    common = most_common(position, binary_list)
    if common == -1:
        finder = int(support_type)
    else:
        if support_type == True:
            finder = common
        else:
            finder = 0 if common == 1 else 1
    binary_updated = []
    for binary in binary_list:
        if int(binary[position]) == finder:
            binary_updated.append(binary)
    binary_list = binary_updated
    position += 1
    return life_support(support_type, position, binary_list)

print(binary_to_decimal(life_support(True)) * binary_to_decimal(life_support(False)))
