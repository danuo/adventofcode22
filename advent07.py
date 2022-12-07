#%%

with open('input07') as file:
    lines = file.read().splitlines()

parser = []
folder_structure = dict()
folder_sizes = []

def run_cd(arg):
    if arg == "/":
        parser.append(folder_structure)
    elif arg == "..":
        parser.pop()
    else:
        obj = parser[-1]
        parser.append(obj[arg])

def parse_ls_results(line):
    obj = parser[-1]
    a, b = line.split(" ")
    if a[0].isdigit():  # is file
        num = int(a)
        name = b
        obj[name] = num
    else:  # is folder
        obj[b] = dict()

for line in lines:
    if line.startswith("$ cd"):
        _, arg = line.split("$ cd ")
        run_cd(arg)
    elif line.startswith("$ ls"):
        pass
    else:
        parse_ls_results(line)

def get_folder_size(obj):
    total_size = 0
    for value in obj.values():
        size = value if isinstance(value, int) else get_folder_size(value)
        total_size += size
    folder_sizes.append(total_size)
    return total_size
root_size = get_folder_size(folder_structure)

# ─── Challenge 1 ──────────────────────────────────────────────────────────────
challenge_1_counter = 0
for folder_size in folder_sizes:
    if folder_size <= 100000:
        challenge_1_counter += folder_size
print('result 1: ', challenge_1_counter)

# ─── Challenge 2 ──────────────────────────────────────────────────────────────
folder_sizes.sort()
required_space = root_size - 40000000
for folder_size in folder_sizes:
    if folder_size > required_space:
        break
print('result 2: ', folder_size)
