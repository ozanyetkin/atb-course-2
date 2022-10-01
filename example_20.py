# Bir string icerisinde art arda en cok tekrar eden 
# karakterin tekrar sayisini ve hangi karakter oldugunu
# verecek bir fonksiyon
# "abbaacccaabc" => (3, "c")
# "aabaacca" => (2, "a")
"""
def consecutive_repeat(input_str):
    previous_str = ""
    max_repetition = 0
    max_str = ""
    for current_str in input_str:
        if current_str == previous_str:
            str_count += 1
        else:
            str_count = 1

        if str_count > max_repetition:
            max_repetition = str_count
            max_str = current_str

        previous_str = current_str
    return (max_repetition, max_str)
"""
"""
def consecutive_repeat(input_str):
    previous_str = ""
    repetition_counts = []
    for current_str in input_str:
        if current_str == previous_str:
            str_count += 1
        else:
            str_count = 1
        repetition_counts.append(str_count)
        previous_str = current_str
    max_index = repetition_counts.index(max(repetition_counts))
    return (max(repetition_counts), input_str[max_index])
"""

def consecutive_repeat(input_str):
    previous_str = ""
    repetition_counts = []
    repetitive_strs = []
    for current_str in input_str:
        if current_str == previous_str:
            str_count += 1
            str_slice += current_str
        else:
            str_count = 1
            str_slice = current_str
        repetition_counts.append(str_count)
        repetitive_strs.append(str_slice)
        previous_str = current_str
        max_index = repetition_counts.index(max(repetition_counts))
    return (max(repetition_counts), repetitive_strs[max_index][0])

print(consecutive_repeat("abbaacccaabc"))