# Verilen .txt dosyasini okuyarak ogrencilerin bilgilerini veri yapisina donusturecegiz
# Bu verilerin icinden notlari kullanarak sinif ortalamasini hesaplayacagiz
# Sinif ortalamasinin 100'den cikarilmasiyla elde edilen sayiyi not baremlemek icin kullanacagiz
# Sinif ortalamasina gore belirlenen harf notu sinirlarini ogrenciye bildirip, harf notunun ne oldugunu soyleyecegiz

with open('./inputs/grades.txt') as f:
    lines = f.readlines()

# "\n" == "Enter" (alt satira gec)
# "\t" == "Tab" (iceri gir)
# "\b" == "Backspace" (sil)
# print(lines)
student_list = []
for line in lines:
    student_info = line.replace("\n", "").split(",")
    # print(student_info)
    info_list = []
    for info in student_info:
        info = info.strip()
        if info.isnumeric():
            info = int(info)
        # print(type(info))
        info_list.append(info)
    student_list.append(info_list)

print(student_list)