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
        level = matrix_tree_heights[0, x]
        for y in range(1, matrix_tree_heights.shape[0]):
            if matrix_tree_heights[y, x] > level:
                matrix_visible_trees[y, x] = 1
            level = max(matrix_tree_heights[y, x], level)

c1_check_vis_top_to_down()
matrix_tree_heights = np.flip(matrix_tree_heights, axis=0)
matrix_visible_trees = np.flip(matrix_visible_trees, axis=0)
c1_check_vis_top_to_down()
matrix_tree_heights = matrix_tree_heights.transpose()
matrix_visible_trees = matrix_visible_trees.transpose()
c1_check_vis_top_to_down()
matrix_tree_heights = np.flip(matrix_tree_heights, axis=0)
matrix_visible_trees = np.flip(matrix_visible_trees, axis=0)
c1_check_vis_top_to_down()

print(np.count_nonzero(matrix_visible_trees))

# ─── Challenge 2 ──────────────────────────────────────────────────────────────

def c2_count_trees_for_y_x(y, x, matrix):
    def find_trees_top_down(y, x, matrix):
        level = 0
        tree_counter = 0
        for y_i in range(y+1, matrix.shape[1]):
            height = matrix[y_i,x]
            if height >= matrix[y,x]:
                tree_counter += 1
                break
            else:
                tree_counter += 1
                if height >= level:
                    level = height
        return tree_counter

    score = 1
    score *= find_trees_top_down(y, x, matrix)
    matrix = np.flip(matrix, axis=0)
    score *= find_trees_top_down(matrix.shape[0]-y-1, x, matrix)
    matrix = matrix.transpose()
    score *= find_trees_top_down(x, matrix.shape[0]-y-1, matrix)
    matrix = np.flip(matrix, axis=0)
    score *= find_trees_top_down(matrix.shape[1]-x-1, matrix.shape[0]-y-1, matrix)
    return score

max_score = 0
for y, x in np.ndindex(matrix_tree_heights.shape):
    score = c2_count_trees_for_y_x(y, x, matrix_tree_heights)
    if score > max_score:
        max_score = score
print(max_score)
