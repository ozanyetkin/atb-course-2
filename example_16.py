def bumping_cars(v1, v2, dist):
    relative_v = abs(v1 - v2) * 1000 / 3600
    if relative_v == 0:
        return None
    else:
        total_second = dist / relative_v
        return total_second

# print(bumping_cars(80, 60, 10000))
    
def time_formatter(input_seconds):
    if input_seconds == None:
        print("Sonsuz")
    else:
        minutes = input_seconds // 60
        seconds = input_seconds % 60
        hours = minutes // 60
        minutes = minutes % 60
        print(f"Iki arac {hours} saat, {minutes} dakika, {seconds:.1f} saniye sonra ayni noktaya gelir")

v1 = int(input("Lutfen daha hizli olan ve geride olan aracin hizini giriniz, v1 (km/sa): "))
v2 = int(input("Lutfen daha yavas olan ve onde olan aracin hizini giriniz, v2 (km/sa): "))
distance = int(input("Lutfen iki arac arasindaki mesafeyi giriniz, d (m): "))

time_formatter(bumping_cars(60, 15, 50000))
time_formatter(bumping_cars(6444440, 144444444, 604444000))
time_formatter(bumping_cars(v1, v2, distance))