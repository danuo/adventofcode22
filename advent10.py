#%%

# ─── Challenge 1 & 2 ───────────────────────────────────────────────────────────

with open('input10') as file:
    lines = file.read().splitlines()

gen = iter(lines)
x = 1
instruction = None
c1_values = []
c2_output_string = ""
for cycle in range(0,240):
    # challenge 1 logging
    if cycle+1 in [20, 60, 100, 140, 180, 220]:
        c1_values.append(x * (cycle+1))
    # challenge 2 logging
    c2_output_string += "#" if cycle%40 in [x-1, x, x+1] else "."
    if instruction is None:
        string = next(gen)
        if string.startswith('noop'):
            instruction = None
        elif string.startswith('addx'):
            ins, val = string.split(' ')
            instruction = int(val)
    elif isinstance(instruction, int):
        x += instruction
        instruction = None
        
print('result 1: ', sum(c1_values))

print('result 2: ')
for i in range(6):
    print(c2_output_string[i*40:(i+1)*40])
