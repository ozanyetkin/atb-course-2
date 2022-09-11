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
# student_list her ogrencinin bilgilerini tek listede tutacak
student_list = []
for line in lines:
    student_info = line.replace("\n", "").split(",")
    # print(student_info)
    # info_list her bir ogrencinin tum bilgilerini icerecek
    info_list = []
    for info in student_info:
        info = info.strip()
        if info.isnumeric():
            info = int(info)
        # print(type(info))
        info_list.append(info)
    student_list.append(info_list)

print(student_list)

total_grades = 0
max_grade = 0
min_grade = 100
for student in student_list:
    total_grades += student[-1]
    if student[-1] > max_grade:
        max_grade = student[-1]
    if student[-1] < min_grade:
        min_grade = student[-1]

average_grade = total_grades / len(student_list)
min_A = average_grade + (max_grade - min_grade) / 2
max_F = average_grade - (max_grade - min_grade) / 2
min_B = min_A - (min_A - max_F) / 3
min_C = max_F + (min_A - max_F) / 3

for student in student_list:
    if student[-1] <= max_F:
        student.append("F")
    elif max_F < student[-1] < min_C:
        student.append("D")
    elif min_C <= student[-1] < min_B:
        student.append("C")
    elif min_B <= student[-1] < min_A:
        student.append("B")
    else:
        student.append("A")

print(student_list)