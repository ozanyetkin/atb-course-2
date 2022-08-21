a = 5
b = 3

animal = "2 + 2 = 4"

a_number = 25

"""
if a > b:
    print("a sayisi b'den buyuktur")
"""
"""
if a > b:
    print("a sayisi b'den buyuktur")
else:
    print("a sayisi b'den kucuk veya b'ye esittir")

if animal == "dog":
    print("Bu hayvan bir kopektir")
else:
    print("Bu esitlik dogru degildir")
"""

if 0 < a_number < 100:
    print("Bu sayi sifir ile 100 arasindadir")
else:
    print("Bu sayi 0 ile 100 arasinda degildir")

"""
if 0 < a_number and a_number < 100:
    print("Bu sayi sifir ile 100 arasindadir")
else:
    print("Bu sayi 0 ile 100 arasinda degildir")
"""
"""
if 0 < a_number:
    if a_number < 100:
        print("Bu sayi sifir ile 100 arasindadir")
    else:
        print("Bu sayi sifir ile 100 arasinda degildir")
else:
    print("Bu sayi sifir ile 100 arasinda degildir")
"""

# Bir sayi 0'dan kucukse negatiftir, 0 ile 100 arasindaysa 0 - 100
# arasindadir, 100'den buyukse bu sayi 100'den buyuktur

if 0 < a_number < 100:
    print("Bu sayi sifir ile 100 arasindadir")
else:
    if a_number <= 0:
        print("Bu sayi sifirdan kucuktur veya 0'dir")
    else:
        print("Bu sayi 100'den buyuktur veya esittir")

if 0 < a_number < 100:
    print("Bu sayi sifir ile 100 arasindadir")
elif a_number < 0:
    print("Bu sayi sifirdan kucuktur")
elif a_number == 0:
    print("Bu sayi sifira esittir")
elif a_number == 100:
    print("Bu sayi 100'e esittir")
else:
    print("Bu sayi 100'den buyuktur")


a_number = float(input("Bir sayi giriniz: "))

if 0 < a_number < 100:
    print("Bu sayi sifir ile 100 arasindadir")
elif a_number < 0:
    print("Bu sayi sifirdan kucuktur")
elif a_number > 100:
    print("Bu sayi 100'den buyuktur")
else:
    print("Bu sayi araligin limit degerindedir")

if 0 <= a_number and a_number <= 100:
    print("Bu sayi sifir ile 100 arasindadir veya esittir")
if a_number < 0:
    print("Bu sayi sifirdan kucuktur")
if 100 < a_number:
    print("Bu sayi 100'den buyuktur")
