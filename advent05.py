#%%

from collections import deque
import string
import re
import copy

with open('input05') as file:
    lines = file.read().splitlines()

def move_n(from_index, to_index, n_items, data):
    items = deque()
    for _ in range(n_items):
        items.appendleft(data[from_index].pop())
    data[to_index].extend(items)

data_1 = [deque() for _ in range(9)]
in_upper = True
for line in lines:
    if len(line) == 0:
        in_upper = False
        data_2 = copy.deepcopy(data_1)
    elif in_upper:
        for stack_index, str_index in enumerate(range(1, len(line), 4)):
            letter = line[str_index]
            if letter in string.ascii_uppercase:
                data_1[stack_index].appendleft(letter)
    else:
        n_moves, from_stack, to_stack = list(map(int, re.findall("\d+", line)))
        # ─── Move For Challenge 1 ─────────────────────────────────────
        for _ in range(n_moves):
            move_n(from_index=from_stack-1, to_index=to_stack-1, n_items=1, data=data_1)
        # ─── Move For Challenge 2 ─────────────────────────────────────
        move_n(from_index=from_stack-1, to_index=to_stack-1, n_items=n_moves, data=data_2)
    

print('result 1: ', "".join([stack[-1] for stack in data_1 if stack]))

print('result 2: ', "".join([stack[-1] for stack in data_2 if stack]))

