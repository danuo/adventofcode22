#%%

with open('input03') as file:
    lines = file.read().splitlines()

def eval_set(result: set):
    counter = 0
    for item in result:
        if item.islower():
            counter += ord(item) - 96
        else:
            counter += ord(item) - 38
    return counter

counter = 0
for line in lines:
    items_first, items_second = line[:len(line)//2], line[len(line)//2:]
    intersection = set.intersection({c for c in items_first}, {c for c in items_second})
    counter += eval_set(intersection)
print(counter)

counter = 0
for i in range(0, len(lines), 3):
    three_rucksacks = lines[i:i+3]
    rucksack_sets = (set(item) for item in three_rucksacks)
    intersection = set.intersection(*rucksack_sets)
    counter += eval_set(intersection)
print(counter)