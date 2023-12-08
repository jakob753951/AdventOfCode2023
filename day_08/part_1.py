with open('input.txt') as f:
    segments = f.read().split('\n\n')

directions, nodes_string = segments

directions = [1 if direction == 'R' else 0 for direction in directions]

nodes = {}
for line in nodes_string.split('\n'):
    name, connections = line.split(' = ')
    left, right = connections.strip('()').split(', ')
    nodes[name] = (left, right)

current_node_name = 'AAA'

index = 0
while current_node_name != 'ZZZ':
    current_node_name = nodes[current_node_name][directions[index % len(directions)]]
    index += 1

print(index)
directions = [1 if direction == 'R' else 0 for direction in open('input.txt').read().split('\n\n')[0]]

nodes = {line.split(' = ')[0]: tuple(line.split(' = ')[1].strip('()').split(', ')) for line in open('input.txt').read().split('\n\n')[1].split('\n')}