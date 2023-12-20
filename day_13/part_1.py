with open('input.txt') as f:
	patterns = f.read().split('\n\n')

# def find_mirroring_index(grid: list[str]) -> int | None:
# 	a = list(zip(*grid))
# 	for i in range(1, len(a)):
# 		thing = [(a, b) for a, b in zip(a[:i], reversed(a[i:])) if a != b]
# 		if len(thing) == 0:
# 			return i
def find_mirroring_index(grid: list[str]) -> int | None:
	a = list(zip(*grid))
	for i in range(1, len(a)):
		matches = [a == b for a, b in zip(reversed(a[:i]), a[i:])]
		if all(matches):
			return i

def get_value(pattern: str) -> int:
	rows = pattern.split('\n')
	columns = [''.join(chars) for chars in zip(*rows)]

	row_mirror = find_mirroring_index(rows)
	col_mirror = find_mirroring_index(columns)

	if col_mirror: return col_mirror * 100
	if row_mirror: return row_mirror

	raise ValueError

print(sum(get_value(pattern) for pattern in patterns))