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

# Get the expected value across a certain number of trials, with a set buy-in, standard is 6
def get_expected(num_trials, buy_in=6):
    if num_trials == 0:
        return 0
    expected = 0

    for _ in range(num_trials):
        result = play()
        expected += result
    expected = expected / num_trials

    return expected 

# Get the error in the expected of a range of trial numbers
def get_error(range_end, range_start= 0, theoretical_expected=5.93):
    return [(theoretical_expected - get_expected(x)) ** 2 for x in range(range_start, range_end)]

# Plot data
plt.axhline(y=0, color="r", linestyle="-")
plt.plot(get_error(40))
plt.xlabel("Number of Games played")
plt.ylabel("Error of E(x)")

plt.show()



