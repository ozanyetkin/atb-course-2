# Kullanicinin istedigi sayiya kadar olan tum tek sayilar ve
# cift sayilar ayri bir listede sirali olacak sekilde store edilecek

user_input = input("Lutfen bir sayi giriniz: ")

while user_input.isnumeric() == False:
    user_input = input("Girdiginiz gecerli bir sayi degildir, lutfen tekrar giriniz: ")

# even_numbers => cift sayilar icin, odd_numbers => tek
even_numbers = []
odd_numbers = []
for i in range(int(user_input) + 1):
    if i % 2 == 0:
        # Burada sayinin cift oldugundan eminim
        even_numbers.append(i)
    else:
        # Burada sayinin tek oldugundan eminim
        odd_numbers.append(i)

print(even_numbers)
print(odd_numbers)

# Burada sayi sayma metodu yerine ikiser ikiser artirarak tek ve cift sayilari bulduk
even_numbers = []
odd_numbers = []

even_number = 0
while even_number <= int(user_input):
    even_numbers.append(even_number)
    even_number += 2

odd_number = 1
while odd_number <= int(user_input):
    odd_numbers.append(odd_number)
    odd_number += 2

print(even_numbers)
print(odd_numbers)