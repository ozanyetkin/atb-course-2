# diabetes_data.txt dosyasini oku
# toplam hasta sayisi
# yasi 55'ten buyuk olanlarin ortalama vucut kutle endeksi (Body_mass_index)
# kac kisinin kandaki glikoz oraninin (glucose_concentration) 105'ten buyuk oldugu
# her bir kolon icin kac verinin eksik oldugunu bulacagiz
# yasi 20 ve 30 arasinda olan kisilerin minimum ve maksimum kan basinci ve serum insulin degerleri
# kullanicidan yas araligi alarak bu yas araliginda olan herkesin tum degerlerini gosterecegiz

def data_reader(file_name):
    with open(f'./inputs/{file_name}.txt') as file:
        lines = file.readlines()
    return lines

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

print(data_parser(data_reader("diabetes_data"), "\t"))
