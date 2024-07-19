import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle
paddle_width, paddle_height = 100, 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2,
                     HEIGHT - 30, paddle_width, paddle_height)

# Ball
ball_size = 10
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT //
                   2 - ball_size // 2, ball_size, ball_size)
ball_speed_x, ball_speed_y = 5, -5

# Bricks
brick_width, brick_height = 80, 30
bricks = [pygame.Rect(col * (brick_width + 5), row * (brick_height + 5),
                      brick_width, brick_height) for row in range(5) for col in range(10)]

# Health system
health = 3

# Score system
score = 0

# Font for text
font = pygame.font.Font(None, 36)


def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    return 5, -5  # Reset ball speed


def show_game_over():
    game_over_text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() //
                2, HEIGHT // 2 - game_over_text.get_height() // 2))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() //
                2, HEIGHT // 2 + game_over_text.get_height()))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before quitting


# Game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 7
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 7

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            score += 10  # Increase score when a brick is broken
            break

    # Ball goes out of bounds
    if ball.bottom >= HEIGHT:
        health -= 1
        if health > 0:
            ball_speed_x, ball_speed_y = reset_ball()
        else:
            game_over = True

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw health
    health_text = font.render(f"Health: {health}", True, GREEN)
    screen.blit(health_text, (10, 10))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Show game over screen
if game_over:
    show_game_over()

pygame.quit()
sys.exit()
