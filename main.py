import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Block")

# Colors
white = (255,255,255)
red = (255,0,0)
gray = (200,200,200)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Paddle and falling block
paddle = pygame.Rect(screen_width//2 - 60, screen_height - 30, 120, 10)
block = pygame.Rect(random.randint(0, screen_width - 20), 0, 20, 20)
block_speed = 5
score = 0

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-8, 0)
        if keys[pygame.K_RIGHT] and paddle.right < screen_width:
            paddle.move_ip(8, 0)

        block.y += block_speed

        # Caught
        if paddle.colliderect(block):
            block.y = 0
            block.x = random.randint(0, screen_width - 20)
            score += 1
            block_speed += 0.5

        # Missed
        if block.y > screen_height:
            game_over = True

    # Draw everything
    window.fill((30, 30, 30))
    pygame.draw.rect(window, red, paddle)
    pygame.draw.rect(window, gray, block)

    score_text = font.render(f"Score: {score}", True, white)
    window.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render(f"Game Over! Final Score: {score}", True, red)
        window.blit(over_text, (screen_width//2 - 170, screen_height//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
