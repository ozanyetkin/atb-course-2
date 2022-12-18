from collections import defaultdict, Counter

with open("./inputs/day_8.txt") as f:
    data = f.readlines()

def dict_generator():
    return {}

digits = defaultdict(dict_generator)
for i, d in enumerate(data):
    encoded, output = [x for x in d.split("|")]
    digits[i]["encoded"] = encoded.strip().split(" ")
    digits[i]["output"] = output.replace("\n", "").strip().split(" ")

all_decoded = []
digits = dict(digits)
for i in range(len(digits)):
    decode_digits = {}
    all_digits = ""
    digit_1 = set()
    digit_7 = set()
    digit_4 = set()
    for digit in digits[i]["encoded"]:
        all_digits += digit
        if len(digit) == 2:
            digit_1 = set(digit)
        if len(digit) == 3:
            digit_7 = set(digit)
        if len(digit) == 4:
            digit_4 = set(digit)

    digit_counts = dict(Counter(all_digits))
    digit_counts = sorted(digit_counts.items(), key=lambda pair: pair[1], reverse=True)

    # print(digit_counts)

    decode_digits["f"] = digit_counts[0][0]
    decode_digits["b"] = digit_counts[5][0]
    decode_digits["e"] = digit_counts[6][0]
    decode_digits["a"] = digit_7.difference(digit_1).pop()
    decode_digits["c"] = digit_counts[1][0] if decode_digits["a"] == digit_counts[2][0] else digit_counts[2][0]
    decode_digits["d"] = digit_counts[3][0] if digit_counts[3][0] in digit_4 else digit_counts[4][0]
    decode_digits["g"] = digit_counts[4][0] if digit_counts[3][0] in digit_4 else digit_counts[3][0]
    
    decoded_numbers = ""
    for digit in digits[i]["output"]:
        encoded_strings = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
        for i, encoded_string in enumerate(encoded_strings):
            temp = ""
            for x in encoded_string:
                temp += decode_digits[x]
            if set(digit) == set(temp):
                decoded_numbers += str(i)
    all_decoded.append(decoded_numbers)

total_count = 0
src = ["1", "4", "7", "8"]
for n in all_decoded:
    for x in n:
        for s in src:
            if s == x:
                total_count += 1

print(total_count)

print(sum([int(x) for x in all_decoded]))
