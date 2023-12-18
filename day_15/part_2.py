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
        self.boxes[HASH(key)].append((key, value))

    def __getitem__(self, key: str) -> str | None:
        box = self.boxes[HASH(key)]
        matching_items = [item for item in box if item[0] == key]
        if len(matching_items) == 0: return None
        return matching_items[0]

    def remove(self, key: str):
        self.boxes[HASH(key)].remove([value for value in self.boxes[HASH(key)] if value[0] == key][0])

hashmap = HashMap()
for string in strings:
    if '-' in string:
        hashmap.remove(string[:-1])
    else:
        key, value = string.split('=')
        hashmap[key] = value

print(hashmap)