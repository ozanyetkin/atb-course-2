a_list = ["asdasd", 5, 7.2, True]
another_list = ["string", 5, 3.2, False, [1, 2, 3], [[1, 2], [2, 3], [3, 4]]]

student_list = [["Meryem", "Tosun", "03156357323", "meryemtosun@gmail.com"], ["Ozan", "Yetkin", "05713238742", "ozan.yetkin@metu.edu.tr"], ["Tosun", "Pasa", "1231231213", "tosun@yesilcam.com"]]
another_student_list = [["Meryem", "Ozan", "Tosun"], ["Tosun", "Yetkin", "Pasa"], ["123235", "234346457", "123123135"], ["asd@qwe.com", "zxc@lkj.com", "xzc@oiu.com"]]

for student in student_list:
    if student[0] == "Tosun" or student[1] == "Tosun":
        print(student)

print(another_student_list[0])

for another_student in another_student_list[0]:
    print(another_student)

# Lutfen evde denemeyiniz
"""
for student_info in another_student_list:
    for i, info in enumerate(student_info):
        if info == "Tosun":
            tosun_index = i
    print(student_info[tosun_index])
"""
