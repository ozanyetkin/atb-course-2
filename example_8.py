# Bir sayi aliyorum (kullanicidan veya bir variable olarak)
# bu sayinin asal sayi olup olmadigini kullaniciya soyluyorum

test_number = int(input("Lutfen pozitif bir tam sayi giriniz: "))
is_prime = True

if test_number == 1:
    is_prime = False

for i in range(2, test_number):
    if (test_number / i) % 1 == 0:
        is_prime = False

if is_prime == True:
    print(f"{test_number} bir asal sayidir")
else:
    print(f"{test_number} bir asal sayi degildir")
