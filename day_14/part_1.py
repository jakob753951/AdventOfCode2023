with open('input.txt') as f:
    lines = f.read().split('\n')
columns = [''.join(chars) for chars in zip(*lines)]
columns = [column.split('#') for column in columns]
columns = [[''.join(sorted(partition, key=lambda x: ord(x), reverse=True)) for partition in column] for column in columns]
columns = ['#'.join(column) for column in columns]
columns = [[i+1 for i, char in enumerate(reversed(column)) if char == 'O'] for column in columns]
columns = [sum(column) for column in columns]

print(sum(columns))
