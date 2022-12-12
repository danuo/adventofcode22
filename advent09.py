#%%

with open('input09') as file:
    lines = file.read().splitlines()

class Snake:
    def __init__(self, n=2):
        self.n = n
        self.x = [0 for _ in range(self.n)]
        self.y = [0 for _ in range(self.n)]
        self.tail_places = set()

    def move(self, direc):
        self.move_head(direc)
        for i in range(1, self.n):
            self.move_tail(i)
        self.tail_places.add((self.x[-1], self.y[-1]))

    def move_head(self, direc):
        match direc:
            case "U":
                self.y[0] += 1
            case "D":
                self.y[0] -= 1
            case "R":
                self.x[0] += 1
            case "L":
                self.x[0] -= 1

    def move_tail(self, i):
        if abs(self.x[i-1] - self.x[i]) + abs(self.y[i-1] - self.y[i]) >= 3:
            self.x[i] += 1 if (self.x[i-1] > self.x[i]) else -1
            self.y[i] += 1 if (self.y[i-1] > self.y[i]) else -1
        elif dist:= abs(self.x[i-1] - self.x[i]) > 1:
            self.x[i] += dist if (self.x[i-1] > self.x[i]) else -dist
        elif dist:= abs(self.y[i-1] - self.y[i]) > 1:
            self.y[i] += dist if (self.y[i-1] > self.y[i]) else -dist

# ─── Challenge 1 ──────────────────────────────────────────────────────────────

snake = Snake(n=2)
for line in lines:
    direction, steps = line.split(' ')
    for _ in range(int(steps)):
        snake.move(direction)
print('result 1: ', len(snake.tail_places))

# ─── Challenge 2 ──────────────────────────────────────────────────────────────

snake = Snake(n=10)
for line in lines:
    direction, steps = line.split(' ')
    for _ in range(int(steps)):
        snake.move(direction)
print('result 2: ', len(snake.tail_places))
