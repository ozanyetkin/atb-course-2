# Bir string icerisinde art arda en cok tekrar eden 
# karakterin tekrar sayisini verecek bir fonksiyon
# "abbaacccaabc" => 3
# "aabaacca" => 2

def consecutive_repeat_1(input_str):
    previous_str = ""
    repetition_counts = []
    for current_str in input_str:
        if current_str == previous_str:
            str_count += 1
        else:
            str_count = 1
        repetition_counts.append(str_count)
        previous_str = current_str
    return max(repetition_counts)

def consecutive_repeat_2(input_str):
    previous_str = ""
    max_repetition = 0
    for current_str in input_str:
        if current_str == previous_str:
            str_count += 1
        else:
            str_count = 1

        if str_count > max_repetition:
            max_repetition = str_count

        previous_str = current_str
    return max_repetition
