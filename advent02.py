#%%

with open('input02') as file:
    lines = file.read().splitlines()
    
wins_against = {
    3: 2,
    2: 1,
    1: 3,
}
looses_against = {a: b for b, a in wins_against.items()}

total_score = 0 
for line in lines:
    letter_a, letter_b = line.split(' ')
    opponent_choice = ord(letter_a) - 64
    my_choice = ord(letter_b) - 87
    total_score += my_choice
    if my_choice == opponent_choice:  # draw
        total_score += 3
    elif wins_against[my_choice] == opponent_choice:  # win
        total_score += 6

print('result 1: ', total_score)

total_score = 0
for line in lines:
    letter_a, letter_b = line.split(' ')
    opponent_choice = ord(letter_a) - 64
    result = ord(letter_b) - 87
    if result == 1:  # loose
        my_choice = wins_against[opponent_choice]
    elif result == 2:  # draw
        total_score += 3
        my_choice = opponent_choice
    else:  # win
        total_score += 6
        my_choice = looses_against[opponent_choice]
    total_score += my_choice

print('result 2: ', total_score)
