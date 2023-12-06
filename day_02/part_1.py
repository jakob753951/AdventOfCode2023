with open("2023_day_02.txt") as f:
    lines = f.read().strip().split("\n")

games = {}
for game in lines:
    number, draws_str = game[5:].split(': ')
    number = int(number)

    draws = []
    for draw in draws_str.split('; '):
        colors = {}
        for pair in draw.split(', '):
            colors[pair.split(' ')[1]] = int(pair.split(' ')[0])
        draws.append(colors)

    games[number] = draws


def is_possible(game: list[dict[str, int]]) -> bool:
    maximum_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    for draw in game:
        for color, amount in draw.items():
            if maximum_cubes[color] < amount:
                return False
    return True


possible_game_numbers = [
    number for
    number, game in
    games.items()
    if is_possible(game)
]
print(sum(possible_game_numbers))
