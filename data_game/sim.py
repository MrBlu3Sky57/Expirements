import random
from matplotlib import pyplot as plt

TYPES = ["Placement", "Post", "Shot", "Goalie"]
PLACEMENT = ["Middle"] * 6 + ["Left"] * 6 + ["Right"] * 6 + ["Post"] + ["Out"]
POST = ["In", "Out"]
SHOT = ["Normal"] * 12 + ["Power"] * 4 + ["Chip"] * 3 + ["Finesse"]
GOALIE = ["Middle", "Right", "Left"]

data = {"Placement": {"Middle": 0, "Left": 0, "Right": 0, "Post":0, "Out": 0}, "Post": {"In": 0, "Out": 0}, "Shot": {"Normal": 0, "Power": 0, "Chip": 0, "Finesse": 0}, "Goalie": {"Middle": 0, "Left": 0, "Right": 0}}
stat_data = {"Placement": {"Middle": 0, "Left": 0, "Right": 0, "Post":0, "Out": 0}, "Post": {"In": 0, "Out": 0}, "Shot": {"Normal": 0, "Power": 0, "Chip": 0, "Finesse": 0}, "Goalie": {"Middle": 0, "Left": 0, "Right": 0}}
player_profits = []

outcomes = set()
outcome_probs = dict()

# Returns multiplier on standard winning for the round
def round():
    placement = random.choice(PLACEMENT)
    data["Placement"][placement] += 1
    
    if placement == "Out":
        return 0

    if placement == "Post":
        post = random.choice(POST)
        data["Post"][post] += 1

        if post == "In":
            return 2
        else:
            return 0
    
    else:
        goalie = random.choice(GOALIE)
        data["Goalie"][goalie] += 1

        shot = random.choice(SHOT)
        data["Shot"][shot] += 1

        if goalie == placement and shot != "Finesse":
            return 0
        else:
            if shot == "Finesse" or shot == "Normal":
                return 1
            elif shot == "Power":
                return 2
            else:
                return 3


def play(std_win=2, num_rounds=3):
    winnings = 0

    for _ in range(num_rounds):
        winnings += round() * std_win
    
    return winnings


def get_stats(num_trials=10**6, buy_in=6):
    if num_trials == 0:
        return 0
    expected = 0
    profit = 0

    for _ in range(num_trials):
        result = play()
        expected += result
        profit += buy_in - result
        player_profits.append(result - buy_in)
    expected = expected / num_trials

    for k1 in data.keys():
        for k2 in data[k1].keys():
            stat_data[k1][k2] = data[k1][k2] / (num_trials * 3) 

    return expected 

data = [(5.93 - get_stats(x)) ** 2 for x in range(0, 10**3)] # Error of expected value
data = data[100:]
plt.axhline(y=0, color="r", linestyle="-")
plt.plot(data)
plt.xlabel("Number of Games played")
plt.ylabel("Error of E(x)")

plt.show()



