# Bir kisiden sirkette kac yil calistigi bilgisini aliyoruz
# Kisinin mevcut maasini soruyoruz
# Bu kisinin deneyimi 0 - 3 yil arasiysa % 5 zam
# Bu kisinin deneyimi 3 - 5 yil arasiysa % 10 zam
# Bu kisinin deneyimi 5 - 10 yil arasiysa % 15 zam
# Bu kisinin deneyimi 10+ yil ise % 20 zam
# Kisiye yeni maasini soyluyoruz

experience = float(input("Lutfen sirkette kac yildir calistiginizi giriniz: "))
salary = float(input("Lutfen sirkette aldiginiz mevcut maasi giriniz: "))

if salary <= 0 or experience <= 0:
    print("Girdiginiz bilgiler gecersizdir")
else:
    if 0 < experience < 3:
        print(f"Yeni maasiniz {salary * 1.05} hayirli olsun.")
    elif 3 <= experience < 5:
        print("Yeni maasiniz " + str(salary * 1.10) + " hayirli olsun.")
    elif 5 <= experience < 10:
        print("Yeni maasiniz " + str(salary * 1.15) + " hayirli olsun.")
    else:
        print("Yeni maasiniz " + str(salary * 1.20) + " hayirli olsun.")