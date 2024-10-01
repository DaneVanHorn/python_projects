import random
import itertools

suits = ['Spade', 'Club', 'Heart', 'Diamond']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
cards = []
hand = []
table_cards = []
num_opps = 1
hands = []

for x in suits:
    for y in ranks:
        cards.append([y, x])

while True:
    user_hand = input("Enter the first card and suit in the following format: 3, Spade or King, Heart or Ace, Diamond: \n\n")
    if "," in user_hand:
        rank, suit = user_hand.split(',')
        rank = rank.strip()
        suit = suit.strip()
        if [rank, suit] in cards:
            hand.append([rank, suit])
            cards.remove([rank, suit])  # Remove the card from the deck
            break
        else: 
            print("\nCard not found in the deck. Please try again.\n")
    else: 
        print("\nInvalid input format. Please try again.\n")

while True:
    user_hand = input("Enter the second card and suit in the following format: 3, Spade or King, Heart or Ace, Diamond: \n\n")
    if "," in user_hand:
        rank, suit = user_hand.split(',')
        rank = rank.strip()
        suit = suit.strip()
        if [rank, suit] in cards:
            hand.append([rank, suit])
            cards.remove([rank, suit])  # Remove the card from the deck
            break
        else: 
            print("\nCard not found in the deck. Please try again.\n")
    else: 
        print("\nInvalid input format. Please try again.\n")

hands.append(hand)

#hand calculator
temp_cards = cards
odds_sum = 0.0

def straight_flush(arr1,arr2):
    arr1_highest_rank = -1
    arr2_highest_rank = -1
    for suit in suits:
        straight_count = 0
        for rank in ranks:
            if [rank, suit] in arr1:
                straight_count += 1
                if straight_count == 5:
                    arr1_highest_rank = ranks.index(rank)
                    break
            else:
                straight_count = 0
    for suit in suits:
        straight_count = 0
        for rank in ranks:
            if [rank, suit] in arr2:
                straight_count += 1
                if straight_count == 5:
                    arr2_highest_rank = ranks.index(rank)
                    break
            else:
                straight_count = 0
    if arr1_highest_rank > arr2_highest_rank:
        return 1
    elif arr1_highest_rank < arr2_highest_rank:
        return -1
    else:
        return 0
    
def fourofakind(arr1, arr2):
    arr1_rank = None
    arr2_rank = None
    for rank in ranks:
        if [rank, 'Spade'] in arr1 and [rank, 'Club'] in arr1 and [rank, 'Heart'] in arr1 and [rank, 'Diamond'] in arr1:
            arr1_rank = rank
    for rank in ranks:
        if [rank, 'Spade'] in arr2 and [rank, 'Club'] in arr2 and [rank, 'Heart'] in arr2 and [rank, 'Diamond'] in arr2:
            arr2_rank = rank
    if arr1_rank is not None and arr2_rank is not None:
        return 1 if ranks.index(arr1_rank) > ranks.index(arr2_rank) else -1 if ranks.index(arr1_rank) < ranks.index(arr2_rank) else 0
    elif arr1_rank is not None:
        return 1
    elif arr2_rank is not None:
        return -1
    else:
        return 0

def fullhouse(arr1, arr2):
    arr1_three = 0
    arr1_two = 0
    arr2_three = 0
    arr2_two = 0
    return_val = 0
    arr1_three_rank = None

    for rank in ranks:
        arr1_count = sum(1 for x in arr1 if x[0] == rank)
        if arr1_count >= 3:
            arr1_three = True
            arr1_three_rank = rank
        elif arr1_count == 2:
            arr1_two = True
        if arr1_three and arr1_two:
            return_val = 1

    for rank in ranks:
        arr2_count = sum(1 for x in arr2 if x[0] == rank)
        if arr2_count >= 3:
            arr2_three = True
            arr2_three_rank = rank
        elif arr2_count == 2:
            arr2_two = True
        if arr2_three and arr2_two:
            if (return_val == 1):
                if ranks.index(arr1_three_rank) < ranks.index(arr2_three_rank):
                    return_val = -1 

    return return_val

def flush (arr1, arr2):
    for x in suits:
        arr1_count = 0
        arr2_count = 0
        for y in arr1:
            if (y[1] == x):
                arr1_count += 1
        for y in arr2:
            if (y[1] == x):
                arr2_count += 1
    if arr1_count == 5:
        return 1
    if arr2_count == 5:
        return -1

def straight(arr):
    rank_integers = {rank: index for index, rank in enumerate(ranks)}
    arr.sort(key=lambda x: rank_integers[x[0]])
    for i in range(len(arr) - 1):
        if rank_integers[arr[i][0]] + 1 != rank_integers[arr[i + 1][0]]:
            return False
    return True

def straight(arr1, arr2):
    is_arr1_straight = straight(arr1)
    is_arr2_straight = straight(arr2)
    if is_arr1_straight and not is_arr2_straight:
        return 1
    elif not is_arr1_straight and is_arr2_straight:
        return -1
    elif is_arr1_straight and is_arr2_straight:
        arr1_highest_rank = arr1[-1][0]
        arr2_highest_rank = arr2[-1][0]
        return 1 if ranks.index(arr1_highest_rank) > ranks.index(arr2_highest_rank) else -1 if ranks.index(arr1_highest_rank) < ranks.index(arr2_highest_rank) else 0
    else:
        return 0 

def trips (arr1, arr2):
    arr1_three = 0
    arr2_three = 0
    return_val = 0
    arr1_three_rank = None

    for rank in ranks:
        arr1_count = sum(1 for x in arr1 if x[0] == rank)
        if arr1_count >= 3:
            arr1_three = True
            arr1_three_rank = rank
        if arr1_three:
            return_val = 1
    for rank in ranks:
        arr2_count = sum(1 for x in arr2 if x[0] == rank)
        if arr2_count >= 3:
            arr2_three = True
            arr2_three_rank = rank
        if arr2_three:
            if (return_val == 1):
                if ranks.index(arr1_three_rank) < ranks.index(arr2_three_rank):
                    return_val = -1 
                if ranks.index(arr1_three_rank) == ranks.index(arr2_three_rank):
                    return_val = high(arr1,arr2)
    return return_val

def two(arr1, arr2):
    arr1_high = None
    arr1_two = 0
    arr2_high = None
    arr2_two = 0
    return_val = 0

    for rank in ranks:
        arr1_count = sum(1 for x in arr1 if x[0] == rank)
        if arr1_count == 2:
            arr1_high = rank
            arr1_two += 1
        if arr1_two == 2:
            return_val = 1

    for rank in ranks:
        arr2_count = sum(1 for x in arr2 if x[0] == rank)
        if arr2_count == 2:
            arr2_high = rank
            arr2_two += 1
        if arr2_two == 2:
            if (return_val == 1):
                if ranks.index(arr1_high) < ranks.index(arr2_high):
                    return_val = -1 
                if ranks.index(arr1_high) == ranks.index(arr2_high):
                    return_val = 0

    return return_val

def pair(arr1, arr2):
    arr1_high = None
    arr1_two = 0
    arr2_high = None
    arr2_two = 0
    return_val = 0

    for rank in ranks:
        arr1_count = sum(1 for x in arr1 if x[0] == rank)
        if arr1_count == 2:
            arr1_high = rank
            arr1_two += 1
        if arr1_two == 1:
            return_val = 1

    for rank in ranks:
        arr2_count = sum(1 for x in arr2 if x[0] == rank)
        if arr2_count == 2:
            arr2_high = rank
            arr2_two += 1
        if arr2_two == 1:
            if (return_val == 1):
                if ranks.index(arr1_high) < ranks.index(arr2_high):
                    return_val = -1 
                if ranks.index(arr1_high) == ranks.index(arr2_high):
                    return_val = 0

    return return_val

def high(arr1, arr2):
    all_cards = arr1 + arr2
    all_cards.sort(key=lambda x: ranks.index(x[0]), reverse=True)
    arr1_highest_cards = all_cards[:2]
    arr2_highest_cards = all_cards[2:4]
    for card1, card2 in zip(arr1_highest_cards, arr2_highest_cards):
        if ranks.index(card1[0]) < ranks.index(card2[0]):
            return -1
        elif ranks.index(card1[0]) > ranks.index(card2[0]):
            return 1  
    return 0

def compare_hand(arr1, arr2):
    straight_flush_result = straight_flush(arr1, arr2)
    if straight_flush_result != 0:
        return straight_flush_result
    four_of_a_kind_result = fourofakind(arr1, arr2)
    if four_of_a_kind_result != 0:
        return four_of_a_kind_result
    full_house_result = fullhouse(arr1, arr2)
    if full_house_result != 0:
        return full_house_result
    flush_result = flush(arr1, arr2)
    if flush_result != 0:
        return flush_result
    straight_result = straight(arr1, arr2)
    if straight_result != 0:
        return straight_result
    trips_result = trips(arr1, arr2)
    if trips_result != 0:
        return trips_result
    two_pair_result = two(arr1, arr2)
    if two_pair_result != 0:
        return two_pair_result
    pair_result = pair(arr1, arr2)
    if pair_result != 0:
        return pair_result
    high_card_result = high(arr1, arr2)
    return high_card_result



all_hands = itertools.combinations(temp_cards, 2*num_opps)

count = 0
wins = 0
new_temp = temp_cards

for x_tuple in all_hands:
    new_temp = temp_cards
    x = list(x_tuple)  # Convert the tuple to a list
    for i in x:
        try:
            new_temp.remove(i)  # Attempt to remove the element from new_temp
        except ValueError:
            pass
    all_rivers = itertools.combinations(new_temp, 5)
    for river in all_rivers:
        river_list = list(river)  # Convert the river tuple to a list
        count += 1
        result = compare_hand(hand + river_list, x + river_list)
        if result == 1:
            wins += 1

print(float(wins)/float(count))
