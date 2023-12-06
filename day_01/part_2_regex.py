import re

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def translate(s: str, d: dict[str, str]):
    for original, replacement in d.items():
        s = s.replace(original, replacement)
    return s


def get_calibration_value(line: str) -> int:
    pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    matches: list[str] = re.findall(pattern, line)
    return int(translate(matches[0], numbers) + translate(matches[-1], numbers))


calibration_values = [get_calibration_value(line) for line in lines]
print(sum(calibration_values))
