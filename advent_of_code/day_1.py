def data_reader(file_name):
    with open(f'./inputs/{file_name}.txt') as file:
        lines = file.readlines()

    parsed_data = []
    for data in lines:
        data = data.replace("\n", "")
        try:
            data = float(data)
        except ValueError:
                pass
        parsed_data.append(data)
    return parsed_data

sonar_data = data_reader("day_1")

increase_count = 0
i = 1
for depth in sonar_data:
    try:
        if depth < sonar_data[i]:
            increase_count += 1
        i += 1
    except IndexError:
        pass

print(increase_count)

increase_count = 0
for i in range(len(sonar_data)):
    try:
        if sum(sonar_data[i:i+3]) < sum(sonar_data[i+1:i+4]):
            increase_count += 1
    except IndexError:
        pass

print(increase_count)
