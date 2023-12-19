from collections import defaultdict


with open('input.txt') as f:
    strings = f.read().split(',')

def HASH(s: str) -> int:
    current_value = 0
    for char in s:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value



class HashMap:
    def __init__(self):
        self.boxes = defaultdict(list)

    def __setitem__(self, key: str, value: str):
        box = self.boxes[HASH(key)]
        matching_items = [item for item in box if item[0] == key]
        if len(matching_items) == 0:
            box.append((key, value))
        else:
            box[box.index(matching_items[0])] = (key, value)

    def __getitem__(self, key: str) -> str | None:
        box = self.boxes[HASH(key)]
        matching_items = [item for item in box if item[0] == key]
        if len(matching_items) == 0: return None
        return matching_items[0]

    def remove(self, key: str):
        box = self.boxes[HASH(key)]
        matching_items = [item for item in box if item[0] == key]
        if len(matching_items) == 0: return None
        box.remove(matching_items[0])

    def score(self) -> int:
        sum = 0
        for box_number, contents in self.boxes.items():
            for i, (key, value) in enumerate(contents):
                sum += (box_number+1) * (i+1) * int(value)
        return sum


hashmap = HashMap()
for string in strings:
    if '-' in string:
        hashmap.remove(string[:-1])
    else:
        key, value = string.split('=')
        hashmap[key] = value

print(hashmap.score())