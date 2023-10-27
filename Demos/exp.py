import pygame
pygame.init()

# Setup the display
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Setup the paddles
paddle_width = 20
paddle_height = 60
paddle1_x = 50
paddle1_y = height//2 - paddle_height//2
paddle_speed = 0.5

# Setup the color
white = (255, 255, 255)
black = (0, 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Make the paddles move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle1_y > 0:
        paddle1_y -= paddle_speed

    if keys[pygame.K_DOWN] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed

    # Draw the background
    screen.fill(black)

    # Draw the paddles
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))

    pygame.display.update()