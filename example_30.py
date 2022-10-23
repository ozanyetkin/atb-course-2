# atom_file.txt dosyasini okuyacagiz
# her bir atom ciftinin aralarindaki uzakligi hesaplayacagiz
# bu atom ciftleri arasindaki mesafe 4.0'ten buyukse False degilse True bilgisi verecegiz
from example_28 import data_reader, data_parser

atom_data = data_parser(data_reader("atom_file"), "\t")
atom_headers = atom_data[0]
atom_locations = atom_data[1:]
