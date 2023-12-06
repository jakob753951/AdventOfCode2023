import re

with open('input.txt') as f:
    lines = f.read().split('\n')

for line in lines:
    matches = re.compile(r"\d+").findall(line)
    for number in matches:
        print(number)
