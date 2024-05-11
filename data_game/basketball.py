import numpy as np

rng = np.random.default_rng(12345)
bps = [20, 25, 50, 60, 65, 70, 70]
N = 10**5

paths = set()
outcomes = dict()
for x in range(N):
    path = ""

    made = 0
    missed = 0
    for bp in bps:
        if made == 5 or missed == 3:
            break

        num = rng.integers(1, 101)
        if num > bp:
            made += 1
            path += "S"
        else:
            missed += 1
            path += "F"
    
    if path not in paths:
        paths.add(path)
        outcomes[path] = 1
    else:
        outcomes[path] += 1


sum = 0
with open("basketball.txt", "a") as file:
    for path, total in outcomes.items():
        sum += total/N
        file.write(f"{path}: {total/N}\n")

print(sum)
