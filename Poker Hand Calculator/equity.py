from collections import Counter 

straightflush = []
numflush = -1

def convert(a):
    b = int(a/4 + 1)
    suit = a%4
    if (suit == 0):
        return b + "D" 
    if (suit == 1):
        return b + "H" 
    if (suit == 2):
        return b + "S" 
    if (suit == 3):
        return str(b) + "C" 

def flush(hand, suit, table):
    count = 0
    high = 0
    if (hand[0] % 4 == suit):
        count += 1
        high = hand[0]
    if (hand[1] % 4 == suit):
        count += 1
        high = hand[1]
    if table + count >= 5:
        return high
    return 0

def straight(all):
    unique_arr = sorted(set(all))  
    if len(unique_arr) < 5:
        return False
    for i in range(len(unique_arr) - 1, 3, -1): 
        if (unique_arr[i]/4 - unique_arr[i-4]/4) == 4:
            return unique_arr[i]
    return 0     

def quads(hand, number): 
    number -= 1 
    if int(hand[0]/ 4) == number:
        if int(hand[1] / 4) == number:
            return number + 1
    return 0

def strfl(hand):
    if hand[4] - 4 == hand[3]:
        if hand[3] - 4 == hand[2]:
            if hand[2] - 4 == hand[1]:
                if hand[1] - 4 == hand[0]:
                    return hand[4]
    return 0

def twopair(arr):
    arr = [int(x / 4 + 1) for x in arr]
    count = Counter(arr)
    pairs = [num for num, cnt in count.items() if cnt == 2]
    pairs.sort(reverse=True)
    if len(pairs) >= 2:
        return pairs[:2]
    else:
        return 0 

def fullhouse(arr):
    arr = [int(x / 4 + 1) for x in arr]
    count = Counter(arr)
    triples = [num for num, cnt in count.items() if cnt >= 3]
    doubles = [num for num, cnt in count.items() if cnt >= 2]
    
    if triples and doubles:
        triples.sort(reverse=True)
        doubles.sort(reverse=True)
        if triples[0] == doubles[0] and len(triples) > 1:
            return triples[1], doubles[0]
        return triples[0], doubles[0]
    return None

def trips(arr):
    arr = [int(x / 4 + 1) for x in arr]
    count = Counter(arr)
    triples = [num for num, cnt in count.items() if cnt >= 3]
    
    if triples:
        triples.sort(reverse=True)
        
        return triples[0]
    return 0

def pair(arr):
    arr = [int(x / 4 + 1) for x in arr]
    count = Counter(arr)
    pair = [num for num, cnt in count.items() if cnt >= 2]
    
    if pair:
        pair.sort(reverse=True)
        
        return pair[0]
    return None

#def handcheck(hand, table, nuts):
def STR(arr):
    if (not pair(arr)):
        arr = [int(x / 4 + 1) for x in arr]
        #print(arr)
        if arr[2] - arr[1] < 4 and arr[2] - arr[0] < 5:
 
            return arr[2]
    return 0


def nutscalc(table):
    nuts = [0, 0]
    strfl = -1
    suit = -1
    suits = [x % 4 for x in table]
    #print(suits)
    count = Counter(suits)
    for num, cnt in count.items():
        if cnt >= 3:
            suit = num
            numflush = cnt
   
    if not suit == -1:
        suited = [x for x in table if x % 4 == suit]
        count = 0
        for x in range (len(suited) - 2):
            if not STR(suited[x:x+3]) == 0:
                straightflush.append(suited[x:x+3])
                count += 1
                nuts = 4, count
                print("straight flush")
                strfl = 1


    if strfl == -1:  
        arr = [int(x / 4 + 1) for x in table]
        count = Counter(arr)
        pair = [num for num, cnt in count.items() if cnt >= 2]
        if pair:
            nuts = [3, pair]
            print("quads")
                    
        elif suit > 0:
            nuts = 2, suit
            print("flush")
        elif STR(table):
            nuts = 1, 0
            print("straight")
        else: 
            print("trips")
    return nuts
# hand should always be sorted !!!!!
"""
print(strfl([1,5,9,13,17])) 
print(quads([5, 6], 2)) 
print(fullhouse([1,2,3,4,5,18,19,49]))     
print(flush([47, 51], 3, 3))
print(straight([0, 1, 5, 9, 13, 17, 21]))
print(trips([1,2,3]))
print(twopair([1,2,5,6,8,20,21]))
print(pair([1,2]))
"""

print() 
print() 




def checkhand(table, own, nuts, pairs, suit, straight, trips):
    all = table + own
    all.sort()

    hand = 0

    if nuts == 4:
        for x in straightflush: 
            new = x+own
            new.sort()
            hand = strfl(new)
    if nuts >= 3: 
        if hand == 0:
            for x in pairs:              
                hand = quads(own, x) + 1
                if not hand == -1:
                    break
        if hand == 0:
            hand = fullhouse(all)
    if nuts >= 2 and not suit == -1:
        if hand == 0: 
            hand = flush(own, suit, numflush)
    if nuts >= 1 and not straight == -1:
        if hand == 0: 
            hand = straight(all)
    else: 
        if hand == 0: 
            hand = twopair(all)
        if hand == 0: 
            hand = pair(all)
    return hand

all_hands = []

sf_hands = []
q_hands = []
fh_hands = []
fl_hands = []
st_hands = []
tr_hands = []
tp_hands = []
p_hands = []
hc_hands = []

table = [13, 17, 18, 23, 41]
hand = [21, 51]
combo = table + hand
print(combo)
combo.sort()

nuts = nutscalc(table)

count = 0

for i in range(0, 52):
    if i in combo:
        continue 
    for j in range(i, 52):
        if j in combo or j == i:
            continue
        else:
            count+=1
            all_hands.append([i,j])

print()
print()
def game():
    pairs = -1
    trips = -1
    quads = -1
    max_suit = -1

    arr = [int(x / 4 + 1) for x in table]
    count = Counter(arr)
    print(count)
    pairs = [num for num, cnt in count.items() if cnt == 2]
    for num, cnt in count.items():
        if cnt == 3:
            trips = num
            break  # Exit loop after finding the first triplet

    # Determine quads (if any)
    for num, cnt in count.items():
        if cnt == 4:
            quads = num
            break  # Exit loop after finding the first quadruplet

    print(pairs)
    print(trips)
    print(quads)
    

    suits = [x % 4 for x in table]
    print(suits)
    count = Counter(suits)
    for num, cnt in count.items():
        if cnt >= 3:
            max_suit = cnt
    if nuts[0] == 4:
        for x in straightflush:
            if x[2] - x[0] == 8:
                bool = not (x[2] + 4) in combo
                if (x[0] - 4) not in combo:
                    if bool: 
                        sf_hands.append(all_hands.remove([x[0]-4,x[2]+4]))
                    if x[0] > 12 and (x[0] - 8) not in combo:
                        if (x[0] - 8) not in combo:
                            sf_hands.append(all_hands.remove([x[0]-8,x[0]-4]))
                if bool and x[2] + 8 not in combo:
                    sf_hands.append(all_hands.remove([x[2]+4,x[2]+8]))
            elif x[2] - x[0] == 12:
                middle = x[0] + (x[2] - x[1])
                if x[2] + 4 not in combo: 
                    sf_hands.append(all_hands.remove([middle, x[2]+4])) 
                if x[0] - 4 not in combo: 
                    sf_hands.append(all_hands.remove([x[0] - 4, middle]))
            else:
                set = [x[2]- 12, x[2]-8, x[2]-4]
                set.remove(x[1])
                if set[0] not in combo and set[1] not in combo:
                    sf_hands.append(set)
    if nuts[0] >= 3:
        #quads
        for x in pairs:
            array = ([(x - 1)* 4 + y for y in range(0, 4)])
            #print(array)
            new_arr = [item for item in array if item not in combo]
            #print(new_arr)
            if len(new_arr) == 2:
                q_hands.append(new_arr)

        if trips != -1:
            array = ([(trips - 1) * 4 + y for y in range(0, 4)])
            print(array)
            new_arr = [item for item in array if item not in combo]
            print(new_arr)
            card = new_arr[0]
            for x in range (0, card):
                if x not in combo:
                    if [x, card] in all_hands:
                        all_hands.remove([x, card])
                        q_hands.append([x, card])
            for x in range (card, 52):
                if x not in combo:
                    if [card, x] in all_hands:
                        all_hands.remove([card, x])
                        q_hands.append([card, x])
            print(0)
        #full house
        for x in pairs:
            #matches a pair
            
            print(0)
            #random trips
        if trips != 

game()

#print(all_hands)
print(sf_hands)
print(q_hands)
print(fh_hands)
print()
print()
