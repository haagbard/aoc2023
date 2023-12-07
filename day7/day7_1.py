import pandas as pd

file = 'aoc2023/day7/input.txt'

results = {}

rankings_five_of_a_kind = []
rankings_four_of_a_kind = []
rankings_full_house = []
rankings_three_of_a_kind = []
rankings_two_pairs = []
rankings_one_pair = []
rankings_high_card = []

hands_bids = {}

card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def five_of_a_kind(hand):
    hand_as_list = list(hand)
    count = pd.Series(hand_as_list).value_counts(sort=True)
    if count.iloc[0] == 5:
        return True
    else:
        return False

def four_of_a_kind(hand):
    hand_as_list = list(hand)
    count = pd.Series(hand_as_list).value_counts(sort=True)
    if count.iloc[0] == 4:
        return True
    else:
        return False

def full_house(hand):
    hand_as_list = list(hand)
    count = pd.Series(hand_as_list).value_counts(sort=True)
    if count.iloc[0] == 3 and count.iloc[1] == 2:
        return True
    else:
        return False

def three_of_a_kind(hand):
    hand_as_list = list(hand)
    count = pd.Series(hand_as_list).value_counts(sort=True)
    if count.iloc[0] == 3:
        return True
    else:
        return False

def two_pairs(hand):
    hand_as_list = list(hand)
    count = pd.Series(hand_as_list).value_counts(sort=True)
    if count.iloc[0] == 2 and count.iloc[1] == 2:
        return True
    else:
        return False
    
def one_pair(hand):
    hand_as_list = list(hand)
    count = pd.Series(hand_as_list).value_counts(sort=True)
    if count.iloc[0] == 2 and count.iloc[1] == 1:
        return True
    else:
        return False
    
def compare_card(card_one, card_two):
    if card_one == card_two:
        return 0
    elif card_values.index(card_one) < card_values.index(card_two):
        # Worth less
        return 1
    else:
        # Worth more
        return -1

def calculate_score(hand):
    index = 0
    if five_of_a_kind(hand):
        for crnt_card in rankings_five_of_a_kind:
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_five_of_a_kind.insert(index, hand)
    elif four_of_a_kind(hand):
        for crnt_card in rankings_four_of_a_kind:
            if hand == 'AAAAQ' and crnt_card == 'AA8AA':
                print('break')
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_four_of_a_kind.insert(index, hand)
    elif full_house(hand):
        for crnt_card in rankings_full_house:
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_full_house.insert(index, hand)
    elif three_of_a_kind(hand):
        for crnt_card in rankings_three_of_a_kind:
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_three_of_a_kind.insert(index, hand)
    elif two_pairs(hand):
        for crnt_card in rankings_two_pairs:
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_two_pairs.insert(index, hand)
    elif one_pair(hand):
        for crnt_card in rankings_one_pair:
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_one_pair.insert(index, hand)
    else:
        for crnt_card in rankings_high_card:
            for i in range(0, len(crnt_card)):
                res = compare_card(hand[i], crnt_card[i])
                if res == 1:
                    index += 1
                    break
                elif res == -1:
                    break
        rankings_high_card.insert(index, hand)

with open(file, 'r') as file:
    lines = file.read().splitlines()

for line in lines:
    hand_bid = line.split(' ')
    hands_bids[hand_bid[0]] = hand_bid[1]

for hand in hands_bids:
    calculate_score(hand)

rankings = []
rankings.extend(rankings_five_of_a_kind)
rankings.extend(rankings_four_of_a_kind)
rankings.extend(rankings_full_house)
rankings.extend(rankings_three_of_a_kind)
rankings.extend(rankings_two_pairs)
rankings.extend(rankings_one_pair)
rankings.extend(rankings_high_card)

rankings.reverse()

for index, hand in enumerate(rankings):
    standing = index + 1
    bid = int(hands_bids[hand])
    results[hand] = bid * standing

sum = 0

for res in results:
    sum += results[res]

print(sum)