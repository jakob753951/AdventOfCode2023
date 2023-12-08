directions = [1 if direction == 'R' else 0 for direction in open('input.txt').read().split('\n\n')[0]]

nodes = {line.split(' = ')[0]: tuple(line.split(' = ')[1].strip('()').split(', ')) for line in open('input.txt').read().split('\n\n')[1].split('\n')}

current_node_names = [name for name in nodes.keys() if name.endswith('A')]

index = 0
while any([not name.endswith('Z') for name in current_node_names]):
    current_node_names = [nodes[name][directions[index % len(directions)]] for name in current_node_names]
    index += 1

print(index)
