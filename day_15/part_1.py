with open('input.txt') as f:
    strings = f.read().split(',')

def HASH(s: str) -> int:
    current_value = 0
    for char in s:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

print(sum(HASH(string) for string in strings))