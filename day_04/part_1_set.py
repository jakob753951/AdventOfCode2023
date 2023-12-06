import math

with open('input.txt') as f:
    lines = f.read().split('\n')

winnings = []
for line in lines:
    line = line.split(': ')[1]
    winning_numbers, our_numbers = line.split(' | ')

    winning_numbers = set(map(int, winning_numbers.split()))
    our_numbers = set(map(int, our_numbers.split()))
    winning_number_count = len(our_numbers.intersection(winning_numbers))
    winnings.append(math.floor(2 ** (winning_number_count-1)))

print(sum(winnings))
