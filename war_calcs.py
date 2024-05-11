import numpy as np
from scipy.stats import gaussian_kde
import statistics
from matplotlib import pyplot as plt

war_probs = []
game_lens = []
prob_wins_1 = 0
prob_wins_2 = 0
prob_ties = 0
with open("war_data.txt", "r") as file:
    lines = file.readlines()
    wins_1 = 0
    wins_2 = 0
    ties = 0
    twc = 0
    wc = 0

    for line in lines:
        data1, data2, data3, data4 = map(float, line.split())
        war_probs.append(round(data1, 3))
        game_lens.append(round(data2, 3))
        twc += data4
        wc += data1

        if data3 == 1:
            wins_1 += 1
        elif data3 == 2:
            wins_2 += 1
        else:
            ties += 1
    prob_wins_1 = round(wins_1 / len(lines), 5)
    prob_wins_2 = round(wins_2 / len(lines), 5)
    prob_ties = ties / len(lines)
    twc = twc / len(lines)
    wc = round(wc / len(lines), 5)



def create_pdf(data_set):
    kde = gaussian_kde(data_set)
    x = np.linspace(0, max(data_set), 1000)

    mean = round(statistics.mean(data_set), 3)
    sd = round(statistics.stdev(data_set), 3)
    print(f"Mean: {mean}\nStd Dev: {sd}\n")

    plt.plot(x, kde(x), label="PDF")
    plt.show()


print(f"P(Player 1 Winning) = {prob_wins_1}")
print(f"P(Player 2 Winning) = {prob_wins_2}")
print(f"P(Tie) = {prob_ties}")
print(f"P(A War) = {wc}")
print(f"P(3 Wars In A Row) = {twc}\n")
create_pdf(war_probs)
create_pdf(game_lens)

    