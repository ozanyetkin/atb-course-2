# verilen iki stringin birbirinin anagrami olup olmadigini soyleyecek
# "race", "care"
# "anagram", "nag a ram"
# "Debit Card", "Bad Credit"
# "New York Times", "Monkeys Write"

def anagram_checker(first_str, second_str):
    first_str = first_str.replace(" ", "").lower()
    second_str = second_str.replace(" ", "").lower()
    if set(first_str) == set(second_str):
        return True
    else:
        return False


def anagram_checker(first_str, second_str):
    first_str = first_str.replace(" ", "").lower()
    second_str = second_str.replace(" ", "").lower()
    if len(first_str) == len(second_str):
        for s in first_str:
            if s in second_str:
                second_str = second_str.replace(s, "", 1)
            else:
                return False
        if second_str == "":
            return True
    else:
        return False

"""
def anagram_checker(first_str, second_str):
    first_str, second_str = first_str.replace(" ", "").lower(), second_str.replace(" ", "").lower()
    return True if set(first_str) == set(second_str) else False
"""

print(anagram_checker("race", "care"))
print(anagram_checker("anagram", "nag a ram"))
print(anagram_checker("Debit Card", "Bad Credit"))
print(anagram_checker("New York Times", "Monkeys Write"))

print(anagram_checker("amnsgjdbiu", "adasljd"))
print(anagram_checker("amhsbd", ",a.mnvshd "))