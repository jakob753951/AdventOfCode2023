winnings = []
for line in open('input.txt').read().split('\n'):
    winnings.append(__import__('math').floor(2 ** ((lambda a,b: len(a.intersection(b))-1)(*map(lambda x: set(map(int, x.split())), line[len('Card 100: '):].split(' | ')))-1)))

print(sum(winnings))
