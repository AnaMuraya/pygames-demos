import pygame
pygame.init()

# Setup the display
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Setup the ball
ball_size = 10
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2
ball_speed_x = 0.5
ball_speed_y = 0.5

# Setup the paddles
paddle_width = 80
paddle_height = 20
paddle1_x = width // 2 - paddle_width // 2
paddle1_y = height - paddle_height - 10
paddle_speed = 0.5

# Setup the scores
score_player1 = 0
font = pygame.font.Font(None, 36)

# Setup the color
white = (255, 255, 255)
black = (0, 0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Make the ball move
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collision with paddles
    if (
        ball_x < paddle1_x + paddle_width
        and ball_x + ball_size > paddle1_x
        and ball_y + ball_size > paddle1_y
        and ball_y < paddle1_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y  # Reverse the vertical direction of the ball
        score_player1 += 1

    # Check for collision with walls
    if ball_x > width - ball_size or ball_x < 0:
        ball_speed_x = -ball_speed_x

    if ball_y > height - ball_size or ball_y < 0:
        ball_speed_y = -ball_speed_y

    # Make the paddle move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle1_x > 0:
        paddle1_x -= paddle_speed

    if keys[pygame.K_RIGHT] and paddle1_x < width - paddle_width:
        paddle1_x += paddle_speed

    # Draw the background
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_size)

    # Draw the paddles
    pygame.draw.rect(screen, white, (int(paddle1_x), int(paddle1_y), paddle_width, paddle_height))

    # Draw the scores
    score_text_player1 = font.render("Player Score: " + str(score_player1), True, white)
    screen.blit(score_text_player1, (10, 10))

    pygame.display.update()
