# Verilen bir kelimenin tum olasi anagramlarini verecek bir fonksiyon
# "123" => ["123", "132", "213", "312", "321", "231"]
# "abcdef" => ["abcdef", "acbdef", ...]

def anagram_generator(input_str):
    if len(input_str) == 1:
        return input_str
    else:
        anagrams = set()
        for letter in input_str:
            for anagram in anagram_generator(input_str.replace(letter, "", 1)):
                anagrams.add(letter + anagram)
        return anagrams

print(anagram_generator("123"))
print(anagram_generator("abcdef"))
print(anagram_generator("a1as46a"))
print(anagram_generator("aaaa"))