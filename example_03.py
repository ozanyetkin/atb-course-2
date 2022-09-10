# Kullanicidan bir sayi alacagiz
# Bu sayi tam sayi degilse, ya kullaniciya bilgi verip islem yapmayacagiz,
# Ya da kullanicinin verdigi sayiyi tam sayiya yuvarlayip bilgi verecegiz
# Bu sayinin tek mi yoksa cift mi oldugunu kullaniciya bildirecegiz

user_input = float(input("Bir sayi giriniz: "))

if user_input % 1 == 0:
    if user_input % 2 == 0:
        print(f"{user_input} cift bir sayidir")
    else:
        print(f"{user_input} tek bir sayidir")
else:
    print("Girdiginiz sayi tam sayi degildir")
    if input("Sayinizi yuvarlamak ister misiniz? (y/n): ") == "y":
        user_input = round(user_input)
        if user_input % 2 == 0:
            print(f"{user_input} cift bir sayidir")
        else:
            print(f"{user_input} tek bir sayidir")
