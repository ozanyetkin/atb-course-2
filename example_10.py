# Kullanicidan tek bir sayi isteyecegiz, verdigi tek sayiya gore ucgen cizdirecegiz:

"""
Kullanici 3 girdiyse:
*
**
*
Kullanici 5 girdiyse:
*
**
***
**
*
"""
# Opsiyon 1: kullanicidan tek sayi alana kadar sormaya devam etmek
# Opsiyon 2: kullanicinin verdigi sayiyi en yakin tek sayiya cevirmek
# Bonus: sekli olusturan karakteri de (*), kullanicidan almak

"""
Ab
AbAb
AbAbAb
AbAb
Ab
"""
user_char = input("Lutfen bir karakter giriniz: ")
user_count = input("Lutfen tek bir sayi giriniz: ")

while user_count.isnumeric() == False:
    user_count = input("Lutfen tek bir sayi giriniz: ")

user_count = int(user_count)

"""
while user_count % 2 != 1:
    user_count = int(input("Lutfen tek bir sayi giriniz: "))
"""

if user_count % 2 == 0:
    user_count = user_count + 1

for i in range(user_count):
    if i <= user_count // 2:
        print(user_char * (i + 1))
    else:
        print(user_char * (user_count - i))