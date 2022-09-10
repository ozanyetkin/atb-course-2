# Kullanici sayi girmeden entera basana kadar verdigi
# tum sayilarin ortalamasi

total_number = 0
user_number = "a"
number_count = 0
while user_number != "":
    user_number = input("Lutfen sayi giriniz, bitirmek icin entera basiniz: ")
    if user_number != "":
        user_number = int(user_number)
        total_number += user_number
        number_count += 1

print(f"Girdiginiz sayilarin ortalamasi: {total_number / number_count}")