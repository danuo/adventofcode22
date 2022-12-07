#%%
with open('input04') as file:
    lines = file.read().splitlines()

counter_1, counter_2 = 0, 0
for line in lines:
    ranges = line.split(',')
    results = []
    for ran in ranges:
        a, b = ran.split('-')
        ran_set = set(range(int(a), int(b)+1))
        results.append(ran_set)
    inter = set.intersection(*results)
    if len(inter) == len(results[0]) or len(inter) == len(results[1]):
        counter_1 += 1
    if len(inter) > 0:
        counter_2 += 1

print(counter_1)
print(counter_2)