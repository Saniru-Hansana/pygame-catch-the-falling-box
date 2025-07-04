import pygame
from pygame.locals import *
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
window.fill((50,50,0))

pygame.display.set_caption("catch the falling ball")

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,255)
yellow = (255,255,0)
pink = (255,0,255)

class Sq(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__ ()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((200,200,200))

#colors        
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

colors = [white,red,blue,green]

#clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,36)

#paddle and block
paddle = pygame.Rect(screen_width//2-60,screen_height - 20 ,120,10)
block = pygame.Rect(random.randint(0,screen_width-20),0,20,20)
b_speed = 5

score = 0 #Score

running = True

while running:
    window.fill((50,50,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        
    #paddle movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0 :
        paddle.move_ip(-8,0)
    if keys[pygame.K_RIGHT] and paddle.right < screen_width :
        paddle.move_ip(8,0)

    #move block
    block.y += b_speed

    #block caught

    if block.colliderect(paddle):
        block.y = 0
        block.x = random.randint(0,screen_width-20)
        score += 1
        b_speed += 0.5 #speed up

    #block missed

    if block.y > screen_height :
        game_over = font.render(f'Game over! Final Score : {score}',True,red)

        window.blit(game_over,(screen_width//2-150,screen_height//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        run = False
        pygame.quit()
        sys.exit()

    # draw Objects
    pygame.draw.rect(window,white,paddle)
    pygame.draw.rect(window,blue,block)
    
    # Display score
    score_text = font.render(f'Score : {score}',True,white)
    window.blit(score_text,(10,10))
    
    pygame.display.flip()
    clock.tick(60)
