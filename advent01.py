#%%

with open('input01') as file:
    lines = file.read().splitlines()

total_weights = []
weight_counter = 0
for line in lines:
    if line == "":
        total_weights.append(weight_counter)
        weight_counter = 0
    else:
        weight_counter += int(line)
total_weights.sort()

print(max(total_weights))
print(sum(total_weights[-3:]))
