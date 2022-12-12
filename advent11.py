#%%

import re
from operator import add, mul

with open('input11') as file:
    lines = file.read().splitlines()

class Monkey:
    def __init__(self, challenge, starting_items, operand, operand_number, test_div_by_n, target_true, target_false, least_common_multiple):
        self.challenge = challenge
        self.starting_items = starting_items
        self.operand = operand
        self.operand_number = operand_number
        self.test_number = test_div_by_n
        self.target_true = target_true
        self.target_false = target_false
        self.count_inspections = 0
        self.least_common_multiple = least_common_multiple

    def execute_turn(self):
        items_out = []
        while len(self.starting_items) > 0:
            self.count_inspections += 1

            # operation
            item = self.starting_items.pop(0)
            op_2 = self.operand_number if isinstance(self.operand_number, int) else item
            item_new = self.operand(item, op_2)

            if self.challenge == 1:
                item_new = int(item_new/3)
            else: 
                item_new = item_new % self.least_common_multiple

            # test
            target_monkey = self.target_true if (item_new % self.test_number == 0) else self.target_false
            items_out.append((item_new, target_monkey))
        return items_out

    def receive(self, item):
        self.starting_items.append(item)


def parse_input(challenge):
    least_common_multiple = 1
    for line in lines:
        if 'Test' in line:
            least_common_multiple *= int(re.search('\d+', line)[0])

    monkeys = []
    for line in lines:
        if 'Monkey' in line:
            starting_items = []
        elif 'Starting' in line:
            numbers = re.findall('\d+', line)
            for number in numbers:
                starting_items.append(int(number))
        elif 'Operation' in line:
            string_end = line.split('= old ')[1]
            opperand = add if string_end[0] == "+" else mul
            operand_num = string_end[1:].strip()
            if operand_num.isdigit():
                opperand_arg = int(operand_num)
            else:
                opperand_arg = operand_num
        elif 'Test' in line:
            test_div_by_n = int(re.search('\d+', line)[0])
        elif 'true' in line:
            target_true = int(re.search('\d+', line)[0])
        elif 'false' in line:
            target_false = int(re.search('\d+', line)[0])
            monkeys.append(Monkey(challenge, starting_items, opperand, opperand_arg, test_div_by_n, target_true, target_false, least_common_multiple))
    return monkeys

# ─── Challenge 1 ──────────────────────────────────────────────────────────────

monkeys = parse_input(challenge=1)
for _ in range(20):
    for monkey in monkeys:
        out_list = monkey.execute_turn()
        for item, target_monkey in out_list:
            monkeys[target_monkey].receive(item)
inspec_times = [monkey.count_inspections for monkey in monkeys]
inspec_times.sort()
print('result 1: ', mul(*inspec_times[-2:]))

# ─── Challenge 2 ──────────────────────────────────────────────────────────────

monkeys = parse_input(challenge=2)
for _ in range(10000):
    for monkey in monkeys:
        out_list = monkey.execute_turn()
        for item, target_monkey in out_list:
            monkeys[target_monkey].receive(item)
inspec_times = [monkey.count_inspections for monkey in monkeys]
inspec_times.sort()
print('result 2: ', mul(*inspec_times[-2:]))
