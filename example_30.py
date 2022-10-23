# atom_file.txt dosyasini okuyacagiz
# her bir atom ciftinin aralarindaki uzakligi hesaplayacagiz
# bu atom ciftleri arasindaki mesafe 4.0'ten buyukse False degilse True bilgisi verecegiz
from math import sqrt
from example_28 import data_reader, data_parser

atom_data = data_parser(data_reader("atom_file"), "\t")

atoms = {}
for i in range(1, len(atom_data)):
    atoms[i] = {
        "x": atom_data[i][1],
        "y": atom_data[i][2],
        "z": atom_data[i][3]
    }

def euclidean_distance(atom_i, atom_j):
    return sqrt(
        (atoms[atom_i]["x"] - atoms[atom_j]["x"]) ** 2 +
        (atoms[atom_i]["y"] - atoms[atom_j]["y"]) ** 2 +
        (atoms[atom_i]["z"] - atoms[atom_j]["z"]) ** 2
    )

for i in range(1, len(atom_data)):
    for j in range(i + 1, len(atom_data)):
        dist = euclidean_distance(i, j)
        if dist <= 4:
            print(i, j, round(dist, 2), True)
        else:
            print(i, j, round(dist, 2), False)
