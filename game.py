#import and initalize
import pygame
import random

pygame.init()
pygame.mixer.init()

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_q,
    QUIT,
)
DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1080
global SCORE
SCORE = 0
#defining player object sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(r"tri3NATMdevsBackend/tswift.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.shoot_delay = 1000
        self.last_shot = pygame.time.get_ticks()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
        if pressed_keys[K_q]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                newProj = Projectile()
                green.add(newProj)
                all_sprites.add(newProj)
            
        #keeps player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > DISPLAY_WIDTH:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.rect.bottom = DISPLAY_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(r"tri3NATMdevsBackend/kanye.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(DISPLAY_WIDTH + 20, DISPLAY_WIDTH + 100), random.randint(0, DISPLAY_HEIGHT)))
        self.speed = random.randint(1, 3)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            global SCORE
            SCORE = SCORE + 1
            self.kill()

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        self.surf = pygame.image.load(r"tri3NATMdevsBackend/microphone.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center = (player.rect.left, player.rect.top))
        self.speed = 2
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > DISPLAY_WIDTH:
            self.kill()

display = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

#event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()

background = pygame.image.load(r"tri3NATMdevsBackend/speaknow.png")
background2 = pygame.image.load(r"tri3NATMdevsBackend/speaknow.png")

#groups to hold enemy sprites - all_sprites for rendering
enemies = pygame.sprite.Group()
green = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

font = pygame.font.Font('freesansbold.ttf', 45)
pygame.mixer.music.load(r"tri3NATMdevsBackend/mine.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)
hundred_sound = pygame.mixer.Sound(r"tri3NATMdevsBackend/coinsound.wav")
hundred_sound.set_volume(0.2)

#run until quit requested
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        #checks for esc key or close window
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            myEnemy = Enemy()
            enemies.add(myEnemy)
            all_sprites.add(myEnemy)
    
    #getting keystrokes
    pressed_keys = pygame.key.get_pressed()
    #score
    i = 'Score: ' + str(SCORE)
    text = font.render(i, True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1800, 1060)

    #update sprite
    player.update(pressed_keys)
    enemies.update()
    green.update()
    
    #white background
    display.fill((0, 0, 0))
    display.blit(background, (0, 0))
    #if (SCORE < 100):
     #   display.blit(background, (0, 0))
    #else:
     #   display.blit(background2, (0, 0))
    display.blit(text, textRect)
    #creating surface - thingy you can draw on seperate from background
    surf = pygame.Surface((100, 100))
    surf.fill((0, 0, 255))
    rect1 = surf.get_rect()
    
    if (SCORE >= 20 and SCORE % 20 == 0):
        hundred_sound.play()
    #blit - block transfer copy one surface to another
    surfCenter = ((DISPLAY_WIDTH-surf.get_width())/2, (DISPLAY_HEIGHT - surf.get_height())/2)
    #display.blit(surf, surfCenter)
    for entity in all_sprites:
        display.blit(entity.surf, entity.rect)
    
    if pygame.sprite.spritecollideany(player, enemies):
        print(SCORE)
        player.kill()
        running = False
    for i in enemies:
        if pygame.sprite.spritecollide(i, green, True):
            i.kill()
            SCORE = SCORE + 5
    #draws green circle in center
    #pygame.draw.circle(display, (0, 255, 0), (250, 250), 75)
    
    #flip display - pushes to display
    pygame.display.flip()
    
    
    ##quit out
    # pygame.quit()