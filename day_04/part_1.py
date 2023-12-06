with open('input.txt') as f:
    lines = f.read().split('\n')

winnings = []
for line in lines:
    line = line.split(': ')[1]
    winning_numbers, our_numbers = line.split(' | ')

    winning_numbers = list(map(int, winning_numbers.split()))
    our_numbers = list(map(int, our_numbers.split()))
    winning_number_count = len(
        [number for number in our_numbers if number in winning_numbers])
    winnings.append(2 ** (winning_number_count-1)
                    if winning_number_count > 0 else 0)


print(sum(winnings))
