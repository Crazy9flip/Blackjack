import pygame
import os

from config import *
from deck import deck
from base import *


# CONFIG
WIDTH, HEIGHT = 1000, 800
FPS = 60

# ASSETS
IMG_FOLDER   = os.path.join(__file__, '../assets/img')
SFX_FOLDER   = os.path.join(__file__, '../assets/sfx')
MUSIC_FOLDER = os.path.join(__file__, '../assets/music')
FONT_FOLDER  = os.path.join(__file__, '../assets/font')

# INIT
pygame.init()
pygame.mixer.init()
pygame.font.init()

# PRESETS

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
pygame.display.set_icon(pygame.image.load(os.path.join(__file__, '../resources/icon/icon.png')))

clock = pygame.time.Clock()

button_click_sound = pygame.mixer.Sound(os.path.join(SFX_FOLDER, "button_click.wav"))

pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, "Howlin Wolf - Spoonful.mp3"))
pygame.mixer.music.play(-1)

font = pygame.font.Font(os.path.join(FONT_FOLDER, 'Bukukoo.ttf'), 36)

max_num_of_duplicates = numberOfDecksChecker()

all_used_cards = []

# Card images dict
vintage_cards_images = {}
for i in deck.keys():
    img_path = os.path.join(IMG_FOLDER, f"cards/vintage_cards/{i}.png")
    original_image = pygame.image.load(img_path).convert_alpha()
    scaled_image = pygame.transform.smoothscale(original_image, (original_image.get_width()/6, original_image.get_height()/6))
    vintage_cards_images[i] = scaled_image
first_card = list(vintage_cards_images.values())[0] 
CARD_WIDTH, CARD_HEIGHT = first_card.get_width(), first_card.get_height()

# STATIC SPRITES
bg_img = pygame.image.load(os.path.join(IMG_FOLDER, 'static/background/background.jpg')).convert()

bg_deck = pygame.image.load(os.path.join(IMG_FOLDER, 'cards/vintage_deck/white_small.png')).convert_alpha()
bg_deck = pygame.transform.smoothscale(bg_deck, (bg_deck.get_width()/5, bg_deck.get_height()/5))

# DYNAMIC SPRITES
button_hit = pygame.image.load(os.path.join(IMG_FOLDER, 'interaction/buttons/hit.png')).convert_alpha()
button_hit = pygame.transform.scale(button_hit, (button_hit.get_width()/8.5, button_hit.get_height()/8.5))

button_stand = pygame.image.load(os.path.join(IMG_FOLDER, 'interaction/buttons/stand.png')).convert_alpha()
button_stand = pygame.transform.scale(button_stand, (button_stand.get_width()/8.5, button_stand.get_height()/8.5))

button_width, button_height = button_hit.get_width(), button_hit.get_height()
button_y = HEIGHT - button_height - 20
hit_x = (WIDTH / 2) - button_width - 25
stand_x = (WIDTH / 2) + 25


# Static sprites rendering
def drawStatic():
    screen.blit(bg_img, (0, 0))
    screen.blit(bg_deck, (800, 80))
    screen.blit(button_hit, (hit_x, button_y))
    screen.blit(button_stand, (stand_x, button_y))

# Text rendering
def drawText(screen, text, x, y, color=(255, 255, 255), outline_color=(0, 0, 0)):
    # Text
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    # Outline
    text_outline = font.render(text, True, outline_color)
    screen.blit(text_outline, (text_rect.x - 2, text_rect.y))
    screen.blit(text_outline, (text_rect.x + 2, text_rect.y))
    screen.blit(text_outline, (text_rect.x, text_rect.y - 2))
    screen.blit(text_outline, (text_rect.x, text_rect.y + 2))
    
    screen.blit(text_surface, text_rect)

# Cards rendering
def drawHand(screen, hand, x_start, y_pos):
    for i, card in enumerate(hand):
        screen.blit(vintage_cards_images[card], (x_start + i * (CARD_WIDTH + 20), y_pos))

# Registers click on a specific button and makes a play
def buttonIdentifierAndActivator(pos):
    # Hit
    if hit_x <= pos[0] <= hit_x + button_width and button_y <= pos[1] <= button_y + button_height:
        button_click_sound.play()
        hit(player_hand, player_score, all_used_cards)
    # Stand
    elif stand_x <= pos[0] <= stand_x + button_width and button_y <= pos[1] <= button_y + button_height:
        button_click_sound.play()
        dealer_turn = dealerPlay(dealer_hand, dealer_score, dealer_primary_card, all_used_cards)
        if dealer_turn > sum(player_score) and dealer_turn <= 21:
            return 'L'
        elif dealer_turn == sum(player_score):
            return 'P'
        else:
            return 'W'


''' Game loop '''
run_game = True
while run_game:

    time_delay = False
    result = None

    shuffle(all_used_cards)

    player_hand  = []
    player_score = []

    dealer_hand  = []
    dealer_score = []

    dealer_primary_card = dealerPrimaryCard(all_used_cards)
    dealer_hand.append(dealer_primary_card[0])
    dealer_score.append(dealer_primary_card[1])

    ## Variation checker
    #if EU:
    #    drawHand(screen, [dealer_primary_card[0]], 50, 80)
    #if US:
    #    print('Upcard: ' + dealer_primary_card[0] + ' and (hole card)')
    #    if dealerNaturalBJChecker(dealer_primary_card, all_used_cards):
    #        print('You lose!\n')
    #        continue


    ''' Round loop '''
    run_round = True
    while run_round:

        clock.tick(FPS)

        # Event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game, run_round = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                result = buttonIdentifierAndActivator(event.pos)
                
        # Rendering
        drawStatic()

        drawHand(screen, dealer_hand, 50, 80)
        drawHand(screen, player_hand, 50, 340)

        drawText(screen, 'SCORE: '  + str(sum(player_score)), 120, 690)
        drawText(screen, 'DEALER: ' + str(sum(dealer_score)), 120, 50)

        if result == 'L':
            drawText(screen, 'YOU LOSE', WIDTH // 2, HEIGHT // 2, color=(224, 11, 0))
            time_delay = True
            run_round = False
    
        elif result == 'W':
            drawText(screen, 'YOU WIN', WIDTH // 2, HEIGHT // 2, color=(143, 197, 97))
            time_delay = True
            run_round = False
    
        elif result == 'P':
            drawText(screen, 'PUSH', WIDTH // 2, HEIGHT // 2, color=(255, 255, 255))
            time_delay = True
            run_round = False

        # Round results
        if sum(player_score) > 21:
            drawText(screen, 'YOU LOSE', WIDTH / 2, HEIGHT / 2, color=(224, 11, 0))
            time_delay = True
            
            run_round = False
        elif sum(player_score) == 21:
            drawText(screen, 'YOU WIN', WIDTH / 2, HEIGHT / 2, color=(143, 197, 97))
            time_delay = True
            run_round = False

        pygame.display.flip()

        if time_delay:
            pygame.time.delay(2000)

pygame.quit()