numbers_list = [12, 8, 4, 9]

def average(num_lst):
    total = 0
    for num in num_lst:
        total += num
    return total / len(num_lst)

avg_1 = average([3, 64, 23, 18])
avg_2 = average(numbers_list)

print(avg_1)
print(avg_2)

def find_min_max(lst):
    lst.sort()
    """
    a = lst[0]
    lst.reverse()
    b = lst[0]
    return a, b
    """
    return lst[0], lst[-1] # lst[len(lst) - 1]

list_min, list_max = find_min_max(numbers_list)
print(list_min)
print(list_max)
