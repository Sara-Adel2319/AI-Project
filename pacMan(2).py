import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

# Set up colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up Pac-Man's initial position and speed
pacman_x = 790
pacman_y = 260
pacman_radius = 20
pacman_speed = 0.8

# Set up ghosts' initial positions and speeds
ghost1_x = 200
ghost1_y = 200
ghost1_radius = 20
ghost1_speed = 0.01

ghost2_x = 600
ghost2_y = 400
ghost2_radius = 20
ghost2_speed = 0.01

# Define maze layout
maze = [
    "########################################",
    "#......................................#",
    "#......................................#",
    "#....####....####......####....####....#",
    "#....##......##..........##......##....#",
    "#....####....##...####...##....####....#",
    "#......................................#",
    "#......................................#"
    "#########....#####    #####....#########",
    "      ###.....###      ###.....###      ",
    "      ###.....############.....###      ",
    "      ###.....############.....###      ",
    "#########.....#    ##    #.....#########",
    "         .....     ##     .....         ",
    "         .....     ##     .....         ",
    "#########.....#    ##    #.....#########",
    "      ###.....############.....###      ",
    "      ###.....############.....###      ",
    "      ###.....#          #.....###      ",
    "#########.....##        ##.....#########",
    "#......................................#",
    "#......................................#",
    "#....####....####......####....####....#",
    "#....##......##..........##......##....#",
    "#....####....##...####...##....####....#",
    "#......................................#",
    "#......................................#",
    "########################################"
]

# Set up pellets
pellets = [(60, 100), (740, 100), (60, 450), (750, 450)]

# Set up score
score = 0

# Set up game state and game over flag
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Move Pac-Man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Move ghosts
    if ghost1_x < pacman_x:
        ghost1_x += ghost1_speed
    else:
        ghost1_x -= ghost1_speed

    if ghost1_y < pacman_y:
        ghost1_y += ghost1_speed
    else:
        ghost1_y -= ghost1_speed

    if ghost2_x < pacman_x:
        ghost2_x += ghost2_speed
    else:
        ghost2_x -= ghost2_speed

    if ghost2_y < pacman_y:
        ghost2_y += ghost2_speed
    else:
        ghost2_y -= ghost2_speed

    # Check collision between Pac-Man and ghosts
    pacman_rect = pygame.Rect(pacman_x - 20, pacman_y - 20, 40, 40)
    ghost1_rect = pygame.Rect(ghost1_x - 20, ghost1_y - 20, 40, 40)
    ghost2_rect = pygame.Rect(ghost2_x - 20, ghost2_y - 20, 40, 40)

    if pacman_rect.colliderect(ghost1_rect) or pacman_rect.colliderect(ghost2_rect):
        game_over = True

    # Check collision between Pac-Man and pellets
    for pellet in pellets:
        pellet_rect = pygame.Rect(pellet[0] - 5, pellet[1] - 5, 10, 10)
        if pacman_rect.colliderect(pellet_rect):
            pellets.remove(pellet)
            score += 10

        # Check for collision with walls
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "#":
                wall_rect = pygame.Rect(x * 20, y * 20, 20, 20)
                pacman_rect = pygame.Rect(pacman_x - pacman_radius, pacman_y - pacman_radius, pacman_radius * 2,
                                          pacman_radius * 2)
                if wall_rect.colliderect(pacman_rect):
                    if keys[pygame.K_LEFT]:
                        pacman_x += pacman_speed
                    if keys[pygame.K_RIGHT]:
                        pacman_x -= pacman_speed
                    if keys[pygame.K_UP]:
                        pacman_y += pacman_speed
                    if keys[pygame.K_DOWN]:
                        pacman_y -= pacman_speed

        # Clear the screen
    screen.fill(BLACK)

    # Draw maze
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "#":
                pygame.draw.rect(screen, BLUE, (x * 20, y * 20, 20, 20))

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (int(pacman_x), int(pacman_y)), pacman_radius)

    # Draw ghosts
    pygame.draw.circle(screen, RED, (int(ghost1_x), int(ghost1_y)), 20)
    pygame.draw.circle(screen, RED, (int(ghost2_x), int(ghost2_y)), 20)

    # Draw pellets
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, pellet, 5)

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # update the screen
    pygame.display.flip()

    while score == 40:
        # Clear the screen
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game if the 'R' key is pressed
                    # Reset game state and variables
                    pacman_x = 790
                    pacman_y = 260
                    ghost1_x = 200
                    ghost1_y = 200
                    ghost2_x = 600
                    ghost2_y = 400
                    pellets = [(60, 100), (740, 100), (60, 450), (750, 450)]
                    score = 0
                    game_over = False

            # Clear the screen
            screen.fill(BLACK)
        font = pygame.font.Font(None, 48)
        win_text = font.render("You Win", True, WHITE)
        screen.blit(win_text, (width // 2 - 100, height // 2 - 50))

        # display restart message
        restart_text = font.render("Press 'R' to restart", True, WHITE)
        screen.blit(restart_text, (width // 2 - 130, height // 2 + 50))

        # update the screen
        pygame.display.flip()

    # Game over logic
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game if the 'R' key is pressed
                    # Reset game state and variables
                    pacman_x = 790
                    pacman_y = 260
                    ghost1_x = 200
                    ghost1_y = 200
                    ghost2_x = 600
                    ghost2_y = 400
                    pellets = [(60, 100), (740, 100), (60, 450), (750, 450)]
                    score = 0
                    game_over = False

        # Clear the screen
        screen.fill(BLACK)

        # Display game over message
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (width // 2 - 100, height // 2 - 50))

    # display restart message
        restart_text = font.render("Press 'R' to restart", True, WHITE)
        screen.blit(restart_text, (width // 2 - 130, height // 2 + 50))

    # update the screen
        pygame.display.flip()
