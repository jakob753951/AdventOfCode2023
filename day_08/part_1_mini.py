directions = [1 if direction == 'R' else 0 for direction in open('input.txt').read().split('\n\n')[0]]

nodes = {line.split(' = ')[0]: tuple(line.split(' = ')[1].strip('()').split(', ')) for line in open('input.txt').read().split('\n\n')[1].split('\n')}

current_node_name = 'AAA'

index = 0
while current_node_name != 'ZZZ':
    current_node_name = nodes[current_node_name][directions[index % len(directions)]]
    index += 1

print(index)