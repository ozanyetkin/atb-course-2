with open("./inputs/day_10.txt") as f:
    data = f.readlines()

data = [d.replace("\n", "") for d in data]

mates = {")": "(", "]": "[", "}": "{", ">": "<"}


def syntax_resolver(input_str):
    previous_char = ""
    open_count = 0
    for i, char in enumerate(input_str):
        try:
            if mates[char] != previous_char:
                return char
            else:
                input_str = input_str[0 : i - 1] + input_str[i + 1 :]
                previous_char = char
                return syntax_resolver(input_str)
        except KeyError:
            open_count += 1
            previous_char = char
        if open_count == len(input_str):
            return input_str


error_points = {")": 3, "]": 57, "}": 1197, ">": 25137}

incomplete_points = {"(": 1, "[": 2, "{": 3, "<": 4}

part1_points = 0
part2_points = 0
part2_list = []
for d in data:
    resolved_syntax = syntax_resolver(d)
    if len(str(resolved_syntax)) == 1:
        part1_points += error_points[str(resolved_syntax)]
    else:
        for x in str(resolved_syntax)[::-1]:
            part2_points *= 5
            part2_points += incomplete_points[x]
    part2_list.append(part2_points)
    part2_points = 0


print(part1_points)
part2 = list(filter(lambda x: (x != 0), part2_list))
part2.sort()
print(part2[len(part2) // 2])
