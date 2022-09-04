# Kullanici sayi girmeden entera basana kadar verdigi
# tum sayilarin ortalamasi

total_number = 0
user_number = 0
number_count = 0
while user_number != -1:
    total_number += user_number
    user_number = int(input("Lutfen sayi giriniz, bitirmek icin -1 yaziniz: "))
    if user_number != -1:
        number_count += 1
        
print(f"Girdiginiz sayilarin ortalamasi: {total_number / number_count}")