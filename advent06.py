#%%

with open('input06') as file:
    line = file.read()

from collections import deque

def eval_str(line, n):
    deq = deque(maxlen=n)
    for i, s in enumerate(line, start=1):
        deq.append(s)
        if len(set(deq)) == n:
            print(i)
            return i


eval_str(line, 4)
eval_str(line, 14)

