# day 4
# i refuse to do this without numpy
import numpy as np


draws = np.loadtxt('day4-input.txt', delimiter=',', max_rows=1, dtype=int)
cards = np.loadtxt('day4-input.txt', skiprows=2, dtype=int).reshape(100, 5, 5)

# print(draws)
# print(cards[:, :, 0])

cards_marked = cards.copy()

for draw in draws:
    cards_marked[cards_marked == draw] = -1

    # check for bingos
    colsums = cards_marked.sum(axis=1)
    rowsums = cards_marked.sum(axis=2)
    if (colsums == -5).any():
        winning_number = draw
        winning_card = np.nonzero(colsums == -5)[0][0]
        print(winning_number, winning_card, cards[winning_card, :, :])
        print(cards_marked[winning_card, :, :])
        break
    if (rowsums == -5).any():
        winning_number = draw
        winning_card = np.nonzero(rowsums == -5)[0][0]
        print(winning_number, winning_card, cards[winning_card, :, :])
        print(cards_marked[winning_card, :, :])
        break

card_sum = cards_marked[winning_card, :, :].copy()
card_sum[card_sum == -1] = 0
print(card_sum)
print(np.sum(card_sum), winning_number, np.sum(card_sum) * winning_number)

# part 2
cards_marked = cards.copy()
card_won = np.full(100, False)

for draw in draws:
    cards_marked[cards_marked == draw] = -1

    # check for bingos
    colsums = cards_marked.sum(axis=1)
    rowsums = cards_marked.sum(axis=2)
    if (colsums == -5).any():
        winning_number = draw
        winning_cards = np.nonzero(colsums == -5)[0]
        card_won[winning_cards] = True
    if (rowsums == -5).any():
        winning_number = draw
        winning_cards = np.nonzero(rowsums == -5)[0]
        card_won[winning_cards] = True

    if sum(card_won) == 99:
        print(winning_number)
        losing_card = np.nonzero(1 - card_won)[0][0]
        print(losing_card)
        break

card_sum = cards[losing_card, :, :].copy()
for draw in draws:
    card_sum[card_sum == draw] = 0

    # check for bingos
    colsums = card_sum.sum(axis=0)
    rowsums = card_sum.sum(axis=1)
    if (colsums == 0).any():
        winning_number = draw
        winning_cards = np.nonzero(colsums == 0)[0]
        break
    if (rowsums == 0).any():
        winning_number = draw
        winning_cards = np.nonzero(rowsums == 0)[0]
        break
card_sum[card_sum == -1] = 0
print(card_sum)
print(np.sum(card_sum), winning_number, np.sum(card_sum) * winning_number)
