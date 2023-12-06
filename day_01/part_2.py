def get_first(line: str, reverse=False) -> int:
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    r = reversed(range(len(line))) if reverse else range(len(line))
    for i in r:
        if line[i].isdigit():
            return int(line[i])
        for number, int_value in numbers.items():
            if line[i:].find(number) == 0:
                return int_value
    raise ValueError


with open("input.txt") as f:
    lines = f.read().split("\n")

calibration_values = [
    get_first(line) * 10 + get_first(line, reverse=True) for line in lines
]

print(sum(calibration_values))
