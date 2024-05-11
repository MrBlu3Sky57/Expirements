import numpy as np
import random

num_allowed = 10657
num_answers = 2135

allowed = np.array([])
answers = np.array([])

with open("answers.txt", "r") as file:
    answers = np.array(file.readlines())

with open("allowed.txt", "r") as file:
    allowed = np.array(file.readlines())

index = random.randint(0, num_answers - 1)

answer = answers[index]

info = dict()

for x in range(6):
    ratings = np.empty(shape=num_allowed, dtype=int)


def check_word(allowed, guess):
    return None