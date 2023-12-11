from itertools import pairwise

with open('input.txt') as f:
    lines = f.read().split('\n')

lines = [list(map(int, line.split(' '))) for line in lines]

def predict_previous(values: list[int]) -> int:
    if all(value == 0 for value in values):
        return 0
    diffs = [b - a for a, b in pairwise(values)]

    return values[0] - predict_previous(diffs)


results = [predict_previous(line) for line in lines]


print(sum(results))
