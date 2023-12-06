from functools import reduce

with open("2023_day_02.txt") as f:
    lines = f.read().strip().split("\n")

games = {}
for game in lines:
    number, draws = game[5:].split(": ")
    number = int(number)

    draws = [
        {pair.split(" ")[1]: int(pair.split(" ")[0])
         for pair in draw.split(", ")}
        for draw in draws.split("; ")
    ]

    games[number] = draws


def power(game: list[dict[str, int]]) -> int:
    minimum_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for draw in game:
        for color, amount in draw.items():
            if minimum_cubes[color] < amount:
                minimum_cubes[color] = amount
    min_cubes = list(minimum_cubes.values())
    power = reduce(lambda acc, x: acc * x, min_cubes)
    return power


powers = [power(game) for game in games.values()]

print(sum(powers))
