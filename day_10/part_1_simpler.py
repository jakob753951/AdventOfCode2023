with open('input.txt') as f:
    grid = f.read().split('\n')

type Position = tuple[int, int]

def get(position: Position) -> str:
	return grid[position[1]][position[0]]

def find_starting_position() -> Position:
	for i, row in enumerate(grid):
		if 'S' in row:
			return (row.index('S'), i)
	raise ValueError

def add(a: Position, b: Position) -> Position:
	return (a[0] + b[0], a[1] + b[1])

def points_to(position: Position) -> list[Position]:
	relative_positions = {
		'|': [(0, -1), (0, 1)],
		'-': [(-1, 0), (1, 0)],
		'J': [(-1, 0), (0, -1)],
		'L': [(1, 0), (0, -1)],
		'7': [(-1, 0), (0, 1)],
		'F': [(1, 0), (0, 1)],
	}
	return [add(position, rel_pos) for rel_pos in relative_positions[get(position)]]

def get_adjacent_pipe_locations(position: Position) -> list[Position]:
	relative_positions = {
		(-1, 0): ['-', 'L', 'F'],
		(1, 0): ['-', 'J', '7'],
		(0, -1): ['|', 'F', '7'],
		(0, 1): ['|', 'J', 'L']
	}
	positions = {add(position, relative): symbols for relative, symbols in relative_positions.items()}

	return [pos for pos, symbols in positions.items() if get(pos) in symbols]

def advance(current: Position, previous: Position) -> Position:
	return [position for position in points_to(current) if position != previous][0]

starting_position = find_starting_position()
current_pos, previous_pos = get_adjacent_pipe_locations(starting_position)[0], starting_position

i = 1
while current_pos != starting_position:
	i += 1
	current_pos, previous_pos = advance(current_pos, previous_pos), current_pos

print(i//2)
