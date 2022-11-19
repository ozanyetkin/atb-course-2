import numpy as np

def data_reader(file_name):
    with open(f'./inputs/{file_name}.txt') as file:
        lines = file.readlines()

    parsed_data = []
    for data in lines:
        data = data.replace("\n", "")
        parsed_data.append(data)
    return parsed_data

bingo_data = data_reader("day_4")

drawn_numbers = [int(data) for data in bingo_data[0].split(",")]

bingo_rows = []
for card_data in bingo_data[1:]:
    if card_data != "":
        row = []
        for data in card_data.split(" "):
            try:
                row.append(int(data))
            except ValueError:
                pass
        bingo_rows.append(row)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

bingo_cards = [np.array(card) for card in list(chunks(bingo_rows, 5))]
def bingo_winner():
    for drawn in drawn_numbers:
        for bingo_card in bingo_cards:
            bingo_card[bingo_card == drawn] = 100
            
            for i in range(bingo_card.shape[0]):
                if np.all(bingo_card[i]==bingo_card[i][0]):
                    return drawn * np.sum(bingo_card[bingo_card != 100])

            bingo_transpose = bingo_card.T
            for i in range(bingo_transpose.shape[0]):
                if np.all(bingo_transpose[i] == bingo_transpose[i][0]):
                    return drawn * np.sum(bingo_card[bingo_card != 100])
        
print(bingo_winner())
