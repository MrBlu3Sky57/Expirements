import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

DECK_SIZE = 6 # CONST
SUITS = ["Clubs", "Diamonds"] # Const
counter = 0

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def get_name(self):
        if self.value in range(2, 11):
            return str(self.value)
        elif self.value == 11:
            return "Jack"
        elif self.value == 12:
            return "Queen"
        elif self.value == 13:
            return "King"
        else:
            return "Ace"


def setup(deck_size=52, suits=["Clubs", "Diamonds",  "Hearts", "Spades"]):
    temp_deck = []

    for suit in suits:
        for value in range(2, (deck_size // len(suits) + 2) ):
            card = Card(value, suit)
            temp_deck.append(card)
                
    deck = np.array(temp_deck)

    hand1 = deck[:(deck_size//2)]
    np.random.shuffle(hand1)
    _ = [print(x.value, end=" ") for x in hand1]
    print("\n")

    hand2 = deck[(deck_size//2):]
    np.random.shuffle(hand2)
    _ = [print(x.value, end=" ") for x in hand2]

    return (hand1, hand2)


def war(hand1, hand2, pile, counter=1):
    card1 = 0
    card2 = 0
    
    if len(hand1) == 0 or len(hand2) == 0:
        return [hand1, hand2, counter]
    elif len(hand1) == 1 and len(hand2) == 1:
        hand1 = np.array([])
        hand2 = np.array([])
        return[hand1, hand2, counter]
    if len(hand1) < 6:
        card1 = hand1[-1].value
        pile = np.append(pile, hand1[:(len(hand1) - 1)])
        hand1 = np.delete(hand1, range(0, len(hand1) - 1))
    else:
        card1 = hand1[4].value
        pile = np.append(pile, hand1[0:4])
        hand1 = np.delete(hand1, range(0, 4))
    
    if len(hand2) < 6:
        card2 = hand2[-1].value
        pile = np.append(pile, hand2[:(len(hand2) - 1)])
        hand2 = np.delete(hand2, range(0, len(hand2) - 1))
    else:
        card2 = hand2[4].value
        pile = np.append(pile, hand2[0:4])
        hand2 = np.delete(hand2, range(0, 4))
    
    if card1 > card2:
        hand1 = np.append(hand1, pile)
        hand1 = np.append(hand1, hand2[0])
        hand2 = np.delete(hand2, 0)
        return (hand1, hand2, counter)
    elif card2 > card1:
        hand2 = np.append(hand2, pile)
        hand2 = np.append(hand2, hand1[0])
        hand1 = np.delete(hand1, 0)
        return (hand1, hand2, counter)
    else:
        return war(hand1, hand2, pile, counter + 1)
    

def play_round(hand1, hand2):
    war_counter = 0

    if len(hand1) == 0 or len(hand2) == 0:
        return [war_counter]

    if hand1[0].value > hand2[0].value:
        hand1 = np.append(hand1, hand1[0])
        hand1 = np.delete(hand1, 0)
        hand1 = np.append(hand1, hand2[0])
        hand2 = np.delete(hand2, 0)
    elif hand2[0].value > hand1[0].value:
        hand2 = np.append(hand2, hand2[0])
        hand2 = np.delete(hand2, 0)
        hand2 = np.append(hand2, hand1[0])
        hand1 = np.delete(hand1, 0)
    else:
        hands = war(hand1, hand2, np.array([], dtype=Card))
        war_counter += hands[-1]

        hand1 = hands[0]
        hand2 = hands[1]
    
    return (hand1, hand2, war_counter)


def play(deck_size=52, suits=["Clubs", "Diamonds",  "Hearts", "Spades"]):
    hand1, hand2 = setup(deck_size, suits)
    game_len = 0
    war_count = 0
    len_hand1 = []
    len_hand2 = []
    triple_war_count = 0
    round_len = 0

    while True:
        hands = play_round(hand1, hand2)
        war_count += hands[-1]

        if war_count > 1:
            game_len += (war_count - 1)

            if hands[-1] == 3:
                triple_war_count += 1

        if len(hands) == 1:
            break

        game_len += 1
        round_len += 1

        hand1 = hands[0]
        len_hand1.append(np.shape(hand1)[0])

        hand2 = hands[1]
        len_hand2.append(np.shape(hand2)[0])

    return [game_len, (len_hand1, len_hand2), (len(hand1), len(hand2)), war_count, triple_war_count, round_len]


def play_100(n, deck_size=52, suits=["Clubs", "Diamonds",  "Hearts", "Spades"]):
    tie_counter = 0
    for x in range(n):
        game_len, hands, len_hands, war_count, twc, round_len = play(deck_size, suits)

        if len_hands[0] == len_hands[1]:
            tie_counter += 1
    return tie_counter / n

N = 1

with open('war_data.txt', 'a') as file:
    for x in range(N):
        game_len, hands, len_hands, war_count, twc, round_len = play(DECK_SIZE, SUITS)

        if game_len == 0:
            war_prob = 0
            prob_twc = 0
        else:
            war_prob = war_count / game_len
            prob_twc = twc / game_len
        
        winner = 0

        if len_hands[0] == 0 and len_hands[1] != 0:
            winner = 2
        elif len_hands[1] == 0 and len_hands[0] != 0:
            winner = 1


        
        file.write(f"{war_prob} {game_len} {winner} {prob_twc}\n")

# m = 52
# n = 10
# tie_tracker = []
# len_tracker = []
# while (m > 0):
#     if m > 26:
#         tie_tracker.append(play_100(n, m) * 100)
#         len_tracker.append(m)
#     else:
#         tie_tracker.append(play_100(n, m, SUITS) * 100)
#         len_tracker.append(m)
#     print(counter)
#     counter += 1
#     m -= 2

# def func(x, a, b, c, d):
#      return a * x**3 + b * x**2 + c * x + d
# _ = [print(len_tracker[i], tie_tracker[i]) for i in range(0, len(tie_tracker))]

# ties = np.array(tie_tracker)
# len = np.array(len_tracker)
# plt.plot(len, ties, ".", label="The probability of Ties in relation to deck size")
# plt.xlabel("Number of Cards in Deck")
# plt.ylabel("Probability of a Tie")

# # optimizedParameters, pcov = opt.curve_fit(func, len, ties)
# # plt.plot(len, func(ties, *optimizedParameters), label="fit")

# plt.show()

# xMin, xMax, yMin, yMax = 0, 50, 0, 100
# xtickFrequency = 5
# ytickFrequency = 5

# fig, ax = plt.subplots(figsize=(10, 10))
# ax.plot(len, ties)

# ax.spines['bottom'].set_position('zero')
# ax.spines['left'].set_position('zero')

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# ax.set_xlabel('Number of Cards in Deck', size=20, labelpad=10 , x=0.5)
# ax.set_ylabel('Percentage Probability of a Tie', size=20, labelpad=-24, y=1.03, rotation=0,)

# x_ticks = np.arange(xMin, xMax+1, xtickFrequency)
# y_ticks = np.arange(yMin, yMax+1, ytickFrequency)
# ax.set_xticks(x_ticks[x_ticks != 0])
# ax.set_yticks(y_ticks[y_ticks != 0])

# ax.set_xticks(np.arange(xMin, xMax+1, 5), minor=True)
# ax.set_yticks(np.arange(yMin, yMax+1, 5), minor=True)

# ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# arrow_fmt = dict(markersize=4, color='black', clip_on=False)
# ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
# ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

# plt.show()