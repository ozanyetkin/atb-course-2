# d metre uzaklikta iki arac var, bunlar v1 ve v2 hizla ayni yonde ilerliyor
# hizi buyuk olan arac yavas olani kac saat, kac dakika kac, saniye sonra yakalar
# 10000 metre mesafede, 80 km/sa ile giden 60 km/sa ile gideni 30 dakikada
# 50000 metre mesafede, 60 km/sa ile giden 15 km/sa ile gideni 1:6:40

v1 = int(input("Lutfen daha hizli olan ve geride olan aracin hizini giriniz, v1 (km/sa): "))
v2 = int(input("Lutfen daha yavas olan ve onde olan aracin hizini giriniz, v2 (km/sa): "))
distance = int(input("Lutfen iki arac arasindaki mesafeyi giriniz, d (m): "))

# Saat biriminden sure hesaplama formulu
t = (distance / 1000) / (v1 - v2)
t_second = t * 60 * 60

def time_formatter(input_seconds):
    minutes = input_seconds // 60
    seconds = input_seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    print(f"Iki arac {hours} saat, {minutes} dakika, {seconds:.1f} saniye sonra ayni noktaya gelir")

time_formatter(t_second)