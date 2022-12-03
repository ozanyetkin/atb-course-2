import numpy as np
import matplotlib.pyplot as plt

from day_1 import data_reader

lines_data = {}
for i, data in enumerate(data_reader("day_5")):
    start, end = data.split(" -> ")
    start_x, start_y = start.split(",")
    end_x, end_y = end.split(",")
    lines_data[i] = {
        "start": {"x": int(start_x), "y": int(start_y)},
        "end": {"x": int(end_x), "y": int(end_y)},
    }

orthagonal_lines = {}
diagonal_lines = {}
for i in range(len(lines_data)):
    if (
        lines_data[i]["start"]["x"] == lines_data[i]["end"]["x"]
        or lines_data[i]["start"]["y"] == lines_data[i]["end"]["y"]
    ):
        orthagonal_lines[i] = lines_data[i]
    else:
        diagonal_lines[i] = lines_data[i]

lines_map = np.zeros((1000, 1000), dtype=int)
for ortho_line in orthagonal_lines.values():
    if ortho_line["start"]["x"] > ortho_line["end"]["x"]:
        for i in range(ortho_line["end"]["x"], ortho_line["start"]["x"] + 1):
            lines_map[ortho_line["start"]["y"]][i] += 1
    elif ortho_line["end"]["x"] > ortho_line["start"]["x"]:
        for i in range(ortho_line["start"]["x"], ortho_line["end"]["x"] + 1):
            lines_map[ortho_line["start"]["y"]][i] += 1
    elif ortho_line["start"]["y"] > ortho_line["end"]["y"]:
        for i in range(ortho_line["end"]["y"], ortho_line["start"]["y"] + 1):
            lines_map[i][ortho_line["start"]["x"]] += 1
    elif ortho_line["end"]["y"] > ortho_line["start"]["y"]:
        for i in range(ortho_line["start"]["y"], ortho_line["end"]["y"] + 1):
            lines_map[i][ortho_line["start"]["x"]] += 1
    else:
        print("Something shitty happened")

print(np.count_nonzero(lines_map > 1))

fig, ax = plt.subplots()
ax.imshow(lines_map)

plt.savefig("./outputs/day5_part1.png")

for diagonal_line in diagonal_lines.values():
    if (
        diagonal_line["start"]["x"] < diagonal_line["end"]["x"]
        and diagonal_line["start"]["y"] < diagonal_line["end"]["y"]
    ):
        for j, i in zip(
            range(
                diagonal_line["start"]["x"],
                diagonal_line["end"]["x"] + 1,
            ),
            range(
                diagonal_line["start"]["y"],
                diagonal_line["end"]["y"] + 1,
            ),
        ):
            lines_map[i][j] += 1
    elif (
        diagonal_line["start"]["x"] > diagonal_line["end"]["x"]
        and diagonal_line["start"]["y"] < diagonal_line["end"]["y"]
    ):
        for j, i in zip(
            range(diagonal_line["start"]["x"], diagonal_line["end"]["x"] - 1, -1),
            range(
                diagonal_line["start"]["y"],
                diagonal_line["end"]["y"] + 1,
            ),
        ):
            lines_map[i][j] += 1
    elif (
        diagonal_line["start"]["x"] > diagonal_line["end"]["x"]
        and diagonal_line["start"]["y"] > diagonal_line["end"]["y"]
    ):
        for j, i in zip(
            range(diagonal_line["start"]["x"], diagonal_line["end"]["x"] - 1, -1),
            range(diagonal_line["start"]["y"], diagonal_line["end"]["y"] - 1, -1),
        ):
            lines_map[i][j] += 1
    elif (
        diagonal_line["start"]["x"] < diagonal_line["end"]["x"]
        and diagonal_line["start"]["y"] > diagonal_line["end"]["y"]
    ):
        for j, i in zip(
            range(
                diagonal_line["start"]["x"],
                diagonal_line["end"]["x"] + 1,
            ),
            range(diagonal_line["start"]["y"], diagonal_line["end"]["y"] - 1, -1),
        ):
            lines_map[i][j] += 1
    else:
        print("Something fucked up")

print(np.count_nonzero(lines_map > 1))

fig, ax = plt.subplots()
ax.imshow(lines_map)

plt.savefig("./outputs/day5_part2.png")
