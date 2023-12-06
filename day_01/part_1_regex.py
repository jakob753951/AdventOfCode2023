import re

with open("input.txt") as f:
    lines = f.read().strip().split("\n")


def get_calibration_value(line: str) -> int:
    matches = re.findall('\\d', line)
    return int(matches[0] + matches[-1])


calibration_values = [get_calibration_value(line) for line in lines]
print(sum(calibration_values))
