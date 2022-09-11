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

letter_counts = [["F", 0], ["D", 0], ["C", 0], ["B", 0], ["A", 0]]
for student in student_list:
    if student[-1] <= max_F:
        student.append("F")
        letter_counts[0][1] += 1
    elif max_F < student[-1] < min_C:
        student.append("D")
        letter_counts[1][1] += 1
    elif min_C <= student[-1] < min_B:
        student.append("C")
        letter_counts[2][1] += 1
    elif min_B <= student[-1] < min_A:
        student.append("B")
        letter_counts[3][1] += 1
    else:
        student.append("A")
        letter_counts[4][1] += 1

# Lambda fonksiyonu icin dokumantasyondan kopya cektik
# https://docs.python.org/3/howto/sorting.html
student_list.sort(key=lambda student: student[-2])

print(student_list)
letters_list = []
for student in student_list:
    # round fonksiyonu dogrudan yuvarlar, asagi yuvarlamak icin floor(), yukari icin ceil()
    bar_count = round(student[2] / 10)
    print(student[0] + "\t" + student[1] + "\t" + (bar_count * "#"))
    letters_list.append(student[-1])

for letter, count in letter_counts:
    print(letter + "\t" + count * "*")