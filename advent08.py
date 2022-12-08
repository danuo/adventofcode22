#%%
# ─── Challenge 1 ──────────────────────────────────────────────────────────────

import numpy as np

with open('input08') as file:
    lines = file.read().splitlines()

matrix_tree_heights = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    for j, num in enumerate(line):
        matrix_tree_heights[i,j] = int(num)

matrix_visible_trees = np.ones(matrix_tree_heights.shape, dtype=int)
matrix_visible_trees[1:-1, 1:-1] = 0

def c1_check_vis_top_to_down():
    for x in range(1, matrix_tree_heights.shape[1]-1):
        ranges = (1, matrix_tree_heights.shape[0], 1), (matrix_tree_heights.shape[0]-2, 0, -1)
        for ran in ranges:
            level = matrix_tree_heights[ran[0]-ran[2], x]
            for y in range(*ran):
                if matrix_tree_heights[y, x] > level:
                    matrix_visible_trees[y, x] = 1
                level = max(matrix_tree_heights[y, x], level)

for _ in range(2):
    c1_check_vis_top_to_down()
    matrix_tree_heights = matrix_tree_heights.transpose()
    matrix_visible_trees = matrix_visible_trees.transpose()

print(np.count_nonzero(matrix_visible_trees))

# ─── Challenge 2 ──────────────────────────────────────────────────────────────

def c2_count_trees_from_y_x(y, x, matrix):
    def find_trees_top_down(y, x, matrix):
        score = 1
        ranges = (y-1, -1, -1), (y+1, matrix.shape[1], 1)
        for ran in ranges:
            level = 0
            counter = 0
            for y_i in range(*ran):
                height = matrix[y_i,x]
                if height >= matrix[y,x]:
                    counter += 1
                    break
                else:
                    counter += 1
                    if height >= level:
                        level = height
            score *= counter
        return score

    score = 1
    for _ in range(2):
        score *= find_trees_top_down(y, x, matrix)
        matrix = matrix.transpose()
        x, y = y, x
    return score

max_score = 0
for y, x in np.ndindex(matrix_tree_heights.shape):
    score = c2_count_trees_from_y_x(y, x, matrix_tree_heights)
    if score > max_score:
        max_score = score
print(max_score)
