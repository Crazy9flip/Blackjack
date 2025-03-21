import pygame
import os

# Config
WIDTH, HEIGHT = 1000, 800
FPS = 60

# Assets
IMG_FOLDER = os.path.join(__file__, '../../assets/img')
SFX_FOLDER = os.path.join(__file__, '../../assets/sfx')

# Init
pygame.init()
pygame.mixer.init()

# Display Surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
pygame.display.set_icon(pygame.image.load(os.path.join(__file__, '../../resources/icon/icon.png')))

# Other
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

#all_sprites.add()

# Static background
bg_img = pygame.image.load(os.path.join(IMG_FOLDER, 'background/background.jpg')).convert()

bg_deck = pygame.image.load(os.path.join(IMG_FOLDER, 'vintage_backface/white_small.png'))
bg_deck = pygame.transform.scale(bg_deck, (bg_deck.get_width()/8, bg_deck.get_height()/8))

screen.blit(bg_img, (0, 0))
screen.blit(bg_deck, (800, 80))

run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()