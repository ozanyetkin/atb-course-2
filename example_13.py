# Bir fonksiyon yazacagiz, bu fonksiyon 4 tane girdi alacak
# ilk girdi ilk sayiyi, ikinci girdi ikinci sayiyi tanimlayacak
# ucuncu girdi alt limiti, dorduncu girdi ust limiti belirleyecek
# verilen alt ve ust limit arasinda, 
# ilk ve ikinci sayinin ortak katlarini verecek

def okek(num_1, num_2, min_range, max_range):
    ortak_list = []
    for advocate in range(min_range, max_range):
        if advocate % num_1 == 0 and advocate % num_2 == 0:
            ortak_list.append(advocate)
    return ortak_list

print(okek(6, 10, 200, 300))
