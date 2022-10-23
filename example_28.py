# diabetes_data.txt dosyasini oku
# toplam hasta sayisi
# yasi 55'ten buyuk olanlarin ortalama vucut kutle endeksi (Body_mass_index)
# kac kisinin kandaki glikoz oraninin (glucose_concentration) 105'ten buyuk oldugu
# her bir kolon icin kac verinin eksik oldugunu bulacagiz
# yasi 20 ve 30 arasinda olan kisilerin minimum ve maksimum kan basinci ve serum insulin degerleri
# kullanicidan yas araligi alarak bu yas araliginda olan herkesin tum degerlerini gosterecegiz
from statistics import mean

# Veriyi dosyadan okumak icin dosya ismini input olarak alan ve her satiri bir liste olarak veren fonksiyon
def data_reader(file_name):
    with open(f'./inputs/{file_name}.txt') as file:
        lines = file.readlines()
    return lines

# data_reader fonksiyonunun okudugu ham veriyi isleyerek dogru veri turunde ayri elemanlar olusturan fonksiyon
def data_parser(raw_data, delimiter):
    parsed_data = []
    for data in raw_data:
        data = data.replace("\n", "").split(delimiter)
        converted = []
        for d in data:
            try:
                d = float(d)
            except ValueError:
                pass
            converted.append(d)
        parsed_data.append(converted)
    return parsed_data

# data_reader ve data_parser kullanarak veriyi okuyup kolon isimlerini ve verileri ayristiriyorum
diabetes_data = data_parser(data_reader("diabetes_data"), "\t")
diabetes_headers = diabetes_data[0]
diabetes_patients = diabetes_data[1:]

# Verilen datanin icerisinden hangi kolonu istiyorsam sadece onu ayiklayip bana veren fonksiyon
def feature_finder(feature):
    feature_matcher = {}
    for i, header in enumerate(diabetes_headers):
        feature_matcher[header] = i
    column_index = feature_matcher[feature]
    column_list = []
    for row in diabetes_patients:
        column_list.append(row[column_index])
    return column_list

# patient_ages = feature_finder("Age")

# Kullanicidan min ve max degerleri aldiktan sonra ilgili kolondaki veriyi kullanarak satirlari filtreleyen fonksiyon
def row_filter(feature_column, min_value, max_value=9999):
    filtered_id = []
    for i, data in enumerate(feature_column):
        if min_value < data < max_value:
            filtered_id.append(i)
    return filtered_id

# print(row_filter(patient_ages, 20, 30))
# feature_finder ve row_filter fonksiyonlarini birlestirerek aradigim hastanin aradigim ozelligini bulmami saglayan fonksiyon
def patient_finder(row_id, column):
    patient_column = feature_finder(column)
    patient_data = []
    for id in row_id:
        patient_data.append(patient_column[id])
    return patient_data

# Aradigim hastalarin id'lerinden o hastaya ait tum verileri almami sagliyor
def all_finder(row_id):
    patient_data = []
    for id in row_id:
        patient_data.append(diabetes_patients[id])
    return patient_data

# Listedeki NA degerlerini silen fonksiyon
def remove_na(the_list):
   return [value for value in the_list if value != "NA"]

# Listedeki NA degerlerini sayan fonksiyon
def count_na(the_list):
    count = 0
    for value in the_list:
        if value == "NA":
            count += 1
    return count

# print(patient_finder(row_filter(patient_ages, 20, 30), "blood_pressure"))

print(f"Toplam hasta sayisi: {len(diabetes_patients)}")

patient_ages = feature_finder("Age")
above_55 = row_filter(patient_ages, 55)
bmi_above_55 = patient_finder(above_55, "Body_mass_index")
print(f"Yasi 55'ten buyuk olanlarin ortalama vucut kutle endeksi: {mean(remove_na(bmi_above_55))}")

glucose_values = feature_finder("glucose_concentration")
above_105 = row_filter(glucose_values, 105)
print(f"{len(above_105)} kisinin kandaki glikoz orani (glucose_concentration) 105'ten buyuk")

na_ages = count_na(feature_finder("Age"))
print(f"Yas listesinde {na_ages} tane NA var")
na_bmi = count_na(feature_finder("Body_mass_index"))
print(f"Vucut kutle endeksi listesinde {na_bmi} tane NA var")

btw_20_30 = row_filter(patient_ages, 20, 30)
blood_pressures = patient_finder(btw_20_30, "blood_pressure")
serum_insulin = patient_finder(btw_20_30, "serum_insulin")
print(f"yasi 20 ve 30 arasinda olan kisilerin minimum kan basinci: {min(remove_na(blood_pressures))}")
print(f"yasi 20 ve 30 arasinda olan kisilerin maximum kan basinci: {max(remove_na(blood_pressures))}")
print(f"yasi 20 ve 30 arasinda olan kisilerin minimum serum insulin: {min(remove_na(serum_insulin))}")
print(f"yasi 20 ve 30 arasinda olan kisilerin maximum serum insulin: {max(remove_na(serum_insulin))}")

min_age = int(input("minimum yas giriniz: "))
max_age = int(input("maximum yas giriniz: "))

filtered_ids = row_filter(patient_ages, min_age, max_age)
for data in all_finder(filtered_ids):
    print(data)
