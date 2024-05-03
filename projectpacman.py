import pygame
import random
import time
import heapq

# Define game constants
GRID_WIDTH = 20
GRID_HEIGHT = 15
CELL_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PACMAN_SPEED = 1  # Adjust speed by increasing or decreasing sleep time
GHOST_SPEED = 0.1



# Define Maze class
class Maze:
    def __init__(self):
        self.maze = [
            "############################",
            "#..........................#",
            "#..####...###..###...####..#",
            "#..####..#...###..#..####..#",
            "#..........................#",
            "######...####  ####...######",
            "    ###...########...###    ",
            "######...#   ##   #...######",
            "      ...    ##    ...      ",
            "######...#   ##   #...######",
            "    ##...#########...###    ",
            "   ###....#     #....###    ",
            "######....##   ##....#######",
            "#..........................#",
            "#..###...####..####...###..#",
            "#..###...##..##..##...###..#",
            "#..........................#",
            "############################"
            ]

    def draw(self, screen):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.maze[y][x] == "#":
                    pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))



# Define Pacman class
class Pacman:
    def __init__(self):
        self.x = 1
        self.y = 1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 3)

    def move(self, dx, dy):
        if 0 <= self.x + dx < GRID_WIDTH and 0 <= self.y + dy < GRID_HEIGHT:
            if maze.maze[self.y + dy][self.x + dx] != "#":
                self.x += dx
                self.y += dy


# Define Ghost class
class Ghost:
    def __init__(self):
        self.x = 10
        self.y = 10

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    def move(self, target):
        dx, dy = self.find_next_move(target)
        if 0 <= self.x + dx < GRID_WIDTH and 0 <= self.y + dy < GRID_HEIGHT:
            if maze.maze[self.y + dy][self.x + dx] != "#":
                self.x += dx
                self.y += dy

    def find_next_move(self, target):
        open_list = []
        closed_list = set()
        heapq.heappush(open_list, (0, (self.x, self.y), []))

        while open_list:
            f, (x, y), path = heapq.heappop(open_list)
            if (x, y) == target:
                return path[0] if path else (0, 0)

            closed_list.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) not in closed_list and 0 <= next_x < GRID_WIDTH and 0 <= next_y < GRID_HEIGHT and \
                        maze.maze[next_y][next_x] != "#":
                    g = len(path) + 1
                    h = abs(next_x - target[0]) + abs(next_y - target[1])
                    f = g + h
                    heapq.heappush(open_list, (f, (next_x, next_y), path + [(dx, dy)]))

        return (0, 0)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

# Create objects
maze = Maze()
pacman = Pacman()
ghost = Ghost()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman.move(-1, 0)
    elif keys[pygame.K_RIGHT]:
        pacman.move(1, 0)
    elif keys[pygame.K_UP]:
        pacman.move(0, -1)
    elif keys[pygame.K_DOWN]:
        pacman.move(0, 1)

    ghost.move((pacman.x, pacman.y))

    # Draw everything
    screen.fill(BLACK)
    maze.draw(screen)
    pacman.draw(screen)
    ghost.draw(screen)

    pygame.display.flip()
    time.sleep(PACMAN_SPEED)

pygame.quit()
