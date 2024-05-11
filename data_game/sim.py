import random
from matplotlib import pyplot as plt

# Data structures that simulate spinners
TYPES = ["Placement", "Post", "Shot", "Goalie"]
PLACEMENT = ["Middle"] * 6 + ["Left"] * 6 + ["Right"] * 6 + ["Post"] + ["Out"]
POST = ["In", "Out"]
SHOT = ["Normal"] * 12 + ["Power"] * 4 + ["Chip"] * 3 + ["Finesse"]
GOALIE = ["Middle", "Right", "Left"]

# Returns multiplier on standard winning for the round
def round():
    placement = random.choice(PLACEMENT)
    
    if placement == "Out":
        return 0

    if placement == "Post":
        post = random.choice(POST)

        if post == "In":
            return 2
        else:
            return 0
    
    else:
        goalie = random.choice(GOALIE)
        shot = random.choice(SHOT)
        if goalie == placement and shot != "Finesse":
            return 0
        else:
            if shot == "Finesse" or shot == "Normal":
                return 1
            elif shot == "Power":
                return 2
            else:
                return 3


# Play a game with a standard win and the number of rounds, standard is (2, 3)
def play(std_win=2, num_rounds=3):
    winnings = 0

    for _ in range(num_rounds):
        winnings += round() * std_win
    
    return winnings


def get_expected(num_trials=10**6, buy_in=6):
    if num_trials == 0:
        return 0
    expected = 0

    for _ in range(num_trials):
        result = play()
        expected += result
    expected = expected / num_trials

    return expected 

data = [(5.93 - get_expected(x)) ** 2 for x in range(0, 10**3)] # Error of expected value
data = data[100:]
plt.axhline(y=0, color="r", linestyle="-")
plt.plot(data)
plt.xlabel("Number of Games played")
plt.ylabel("Error of E(x)")

plt.show()



