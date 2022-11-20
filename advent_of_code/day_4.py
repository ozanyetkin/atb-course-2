import numpy as np


def data_reader(file_name):
    with open(f"./inputs/{file_name}.txt") as file:
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
        yield lst[i : i + n]


bingo_cards = [np.array(card) for card in list(chunks(bingo_rows, 5))]


def bingo_winner():
    for drawn in drawn_numbers:
        for bingo_card in bingo_cards:
            bingo_card[bingo_card == drawn] = 100

            for i in range(bingo_card.shape[0]):
                if np.all(bingo_card[i] == bingo_card[i][0]):
                    return drawn * np.sum(bingo_card[bingo_card != 100])

            bingo_transpose = bingo_card.T
            for i in range(bingo_transpose.shape[0]):
                if np.all(bingo_transpose[i] == bingo_transpose[i][0]):
                    return drawn * np.sum(bingo_card[bingo_card != 100])


print(bingo_winner())


def remove_array(L, arr):
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind], arr):
        ind += 1
    if ind != size:
        L.pop(ind)
    else:
        # raise ValueError('array not found in list.')
        pass


def checker(bingo_card):
    bingo_transpose = bingo_card.T
    for i in range(bingo_card.shape[0]):
        if np.all(bingo_card[i] == bingo_card[i][0]) or np.all(bingo_transpose[i] == bingo_transpose[i][0]):
            return bingo_card
        else:
            return None


def bingo_loser(bingo_cards):
    winners = []
    winner_ids = []
    for drawn in drawn_numbers:
        candidate_cards = []
        for index, bingo_card in enumerate(bingo_cards):
            bingo_card[bingo_card == drawn] = 100
            if checker(bingo_card) is not None:
                if index not in winner_ids:
                    winner_ids.append(index)
                    winners.append((index, drawn * np.sum(bingo_card[bingo_card != 100])))
            else:
                candidate_cards.append(bingo_card)
        bingo_cards = candidate_cards
    return winners

bingo_cards = [np.array(card) for card in list(chunks(bingo_rows, 5))]

# print(bingo_loser(bingo_cards))

class Board:
    def __init__(self):
        self.board = np.zeros((5,5), dtype=int)
        self.marked = np.zeros((5,5))

    def read_from_lines(self, lines):
        for i in range(5):
            line_entries = [int(entry) for entry in lines[i].split(' ') if entry != '']
            self.board[i] = line_entries
    
    def check_called_number(self, called_number):
        if called_number in self.board:
            indices = np.where(self.board == called_number)
            self.marked[indices[0], indices[1]] = 1

    def check_win(self):
        return self.marked.all(axis=0).any() or self.marked.all(axis=1).any()

    def calculate_score(self, called_number):
        return (self.board * (self.marked==0)).sum() * called_number

with open("./inputs/day_4.txt", 'r') as f:
    lines = [entry.strip() for entry in f.readlines()]

called_numbers = [int(entry) for entry in lines[0].split(',')]

number_of_boards = (len(lines)-1)//6
boards = dict()
for i in range(number_of_boards):
    boards[i] = Board()
    boards[i].read_from_lines(lines[(2 + i*6):(2+5+(i+1)*6)])

def find_last_winner(called_numbers, boards):
    winners = []
    winner_call = 0
    for called_number in called_numbers:
        for i in range(len(boards)):
            if i not in winners:
                boards[i].check_called_number(called_number)
                if boards[i].check_win():
                    winners.append(i)
                    # print(f"Board {i+1} won!")
                    winner_call = called_number
    return winners[-1], winner_call

winner_index, called_number = find_last_winner(called_numbers, boards)    
print(boards[winner_index].calculate_score(called_number))
