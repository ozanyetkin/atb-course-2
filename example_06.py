# Kullanicidan 5 tane sayi alacagiz, sonra kullaniciya bu sayilarin
# ortalamasini soyleyecegiz

user_numbers = []
for i in range(5):
    user_input = int(input("Bir sayi giriniz: "))
    user_numbers.append(user_input)

print(f"Girdiginiz sayilar sunlardir: {user_numbers}")
average_value = sum(user_numbers) / len(user_numbers)
print(f"Girdiginiz sayilarin ortalamasi: {average_value}")
