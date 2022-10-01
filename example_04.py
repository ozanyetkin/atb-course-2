# Kullanicidan bir sayi girdisi alacagiz, bu sayi saniye olarak verilmis
# kabul edilecek, Ay, Gun, Saat, Dakika, Saniye
# "Girdiginiz 6759873 saniye 145 Gün 22 Saat 35 Dakika 23 Saniyedir"

input_seconds = int(input("Lütfen saniye bilgisi giriniz: "))

minutes = input_seconds // 60
seconds = input_seconds % 60

hours = minutes // 60
minutes = minutes % 60

days = hours // 24
hours = hours % 24

print(f"Girdiginiz {input_seconds} Saniye: {days} Gün {hours} Saat {minutes} Dakika {seconds} Saniyedir")
# print("Girdiginiz " + str(input_seconds) + " Saniye: " + str(days) + " Gun")
