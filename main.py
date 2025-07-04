import pygame
import sys
import random
from pygame import locals

#initialize pygame
pygame.init()

#create the display  , caption,font,clock
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
pygame.display.set_caption('catch the falling blocks')
font = pygame.font.SysFont(None,36)
clock = pygame.time.Clock()

# Colors
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
yellow = (200,200,0)
white = (255,255,255)
colors = [red,green,blue,yellow,white]
# setup spirit classes
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120,20))
        self.image.fill((200,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,550)
    
    def update(self,keys,paddle_speed):
        if keys[pygame.K_LEFT] and self.rect.left > 0 :
            self.rect.x -= paddle_speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += paddle_speed

class blocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill(colors[random.randint(0,4)])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,800 - self.rect.width)
        self.rect.y = -10
    
    def update(self):
        self.rect.y += (random.randint(1,12))
        if self.rect.y > 550 :
            self.kill()
    





all_sprites = pygame.sprite.Group()
block_group = pygame.sprite.Group()

paddle = Paddle()
new_block = blocks()

all_sprites.add(paddle)
all_sprites.add(new_block)
block_group.add(new_block)

score = 0
game_over = False
running = True
while running:
    paddle_speed = 12
    for keys in pygame.event.get():
        if keys.type == pygame.QUIT:
            running =False

    if not game_over :
        keys= pygame.key.get_pressed()
        paddle.update(keys,paddle_speed)
        block_group.update()

    hits = pygame.sprite.spritecollide(paddle,block_group,True)

    for hit in hits:
        score += 1
        new_block = blocks()
        all_sprites.add(new_block)
        block_group.add(new_block)
        
        
    if len(block_group) == 0 :
        game_over = True
    
    screen.fill((0,0,0))
    points = font.render(f'Score : {score}',True,white)
    screen.blit(points,(50,50))
    all_sprites.draw(screen)

    if game_over:
        over_text = font.render(f"Game Over! Final Score: {score}", True,red)
        screen.blit(over_text, (800 // 2 - 170, 600 // 2))
    




    #setup and upgrade background
    
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()