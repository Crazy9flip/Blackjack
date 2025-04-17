# All the functions are declared in this module
# Add variations!
# Add additional rules!
# Do some refactoring!
# Save players' data in JSON!

from deck import deck
from config import *

from random import choice
from collections import Counter


# Quit
def leave():
    input('C\'ya, puta!')
    quit()


# Number of decks configuration
def numberOfDecksChecker():
    if SINGLE_DECK:
        return 1  
    if TWO_DECKS:
        return 2  
    if FOUR_DECKS:
        return 4  
    if SIX_DECKS:
        return 6  
    if EIGHT_DECKS:
        return 8


# Card duplicates protector
def duplicatesProtector(new_card, all_used_cards, max_num_of_duplicates = numberOfDecksChecker()):
    hand_counter = dict(Counter(all_used_cards))
    if hand_counter[new_card] > max_num_of_duplicates:
        all_used_cards.pop()
        return True
    return False


# Skip iteration on duplicate and choose a random card
def skipIterationOnDuplicateAndChoose(all_used_cards):
    while True:
        tmp_key, tmp_val = choice(list(deck.items()))
        all_used_cards.append(tmp_key)
        if duplicatesProtector(tmp_key, all_used_cards):
            continue
        break
    return [tmp_key, tmp_val]


# Interim results
def printCurResults(hand, score):
    print('Current hand: ', end='')
    for i in hand:
        print(i, end=' ')
    print('\nScore: ' + str(score))


# Variable Ace
def variableAce(score):
    while sum(score) > 21 and 11 in score:
        ace_index = score.index(11)
        score[ace_index] = 1 


# CSM (always for SINGLE_DECK and TWO_DECKS) | ASM
def shuffle(all_used_cards, max_num_of_duplicates = numberOfDecksChecker()):
    if max_num_of_duplicates in [1, 2]:
        all_used_cards.clear()
        print('The deck(s) have been shuffled.\n')
    else:
        if CSM:
            all_used_cards.clear()
            print('The deck(s) have been shuffled.\n')
        if ASM:
            if len(all_used_cards) >= (max_num_of_duplicates * 26):
                all_used_cards.clear()
                print('The deck(s) have been shuffled.\n')


def hit(hand, score, all_used_cards):
    ''' Take a card '''
    tmp_items = skipIterationOnDuplicateAndChoose(all_used_cards)
    tmp_key, tmp_val = tmp_items[0], tmp_items[1]    
    hand.append(tmp_key)
    score.append(tmp_val)
    variableAce(score)
    printCurResults(hand, sum(score))


def playerNaturalBJChecker(player_hand, dealer_primary_card, all_used_cards):
    ''' Check if player has natural blackjack (EU variation) '''
    if len(player_hand) == 2:
        print('Blackjack!\n')
        if dealer_primary_card[1] in [10, 11]:
            if dealerNaturalBJChecker(dealer_primary_card, all_used_cards):
                print('Push!\n')
            else:
                print('You win!\n')
        else:
            print('You win!\n')
    else:
        if dealer_primary_card[1] in [10, 11]:
            if dealerNaturalBJChecker(dealer_primary_card, all_used_cards):
                print('You lose!\n')
            else:
                print('You win!\n')
        else:
            print('You win!\n')


def dealerNaturalBJChecker(dealer_primary_card, all_used_cards):
    ''' Check if dealer has natural blackjack '''
    dealer_second_card = dealerPrimaryCard(all_used_cards)
    dealer_primary_card.extend(dealer_second_card)
    dealer_tmp_sum = 0

    for i in range(len(dealer_primary_card)):
        try:
            dealer_tmp_sum += dealer_primary_card[i]
        except TypeError:
            continue

    return True if dealer_tmp_sum == 21 else False


def dealerPrimaryCard(all_used_cards, max_num_of_duplicates = numberOfDecksChecker()):
    ''' Dealer's primary card '''
    tmp_items = skipIterationOnDuplicateAndChoose(all_used_cards)
    dealer_tmp_key, dealer_tmp_val = tmp_items[0], tmp_items[1]
    return [dealer_tmp_key, dealer_tmp_val]


def dealerPlay(dealer_hand, dealer_score, all_used_cards, max_num_of_duplicates = numberOfDecksChecker()):
    ''' Dealer's turn '''
    while sum(dealer_score) < 17:
        hit(dealer_hand, dealer_score, all_used_cards)
    return sum(dealer_score)


def main():
    ''' Main function '''

    ''' Pre-game declarations '''
    
    print('\nWell, well, well, if it ain\'t gambling motherfucker again.\n')
    
    max_num_of_duplicates = numberOfDecksChecker()
    
    all_used_cards = []

    bankroll = 500
    
    ''' Game loop '''
    while True:

        if bankroll <= 0:
            print('Looks like you\'re out of the Big Bens...\n')
            leave()
        
        bankroll -= 25
        print(f'Bankroll: {bankroll}')

        shuffle(all_used_cards)

        player_hand  = []
        player_score = []

        dealer_hand  = []
        dealer_score = []

        dealer_primary_card = dealerPrimaryCard(all_used_cards)
        dealer_hand.append(dealer_primary_card[0])
        dealer_score.append(dealer_primary_card[1])

        # Variation checker
        if EU:
            print('Upcard: ' + dealer_primary_card[0])
        if US:
            print('Upcard: ' + dealer_primary_card[0] + ' and (hole card)')
            if dealerNaturalBJChecker(dealer_primary_card, all_used_cards):
                print('You lose!\n')
                continue
        
        hit(player_hand, player_score, all_used_cards)

        ''' Round loop '''
        while True:
        
            ''' Player's actions '''
    
            action = input('\nWhat do we do? ( 1 - Hit | 2 - Stand | 3 - Leave ) : ')
        
            # Hit
            if action == '1':
                hit(player_hand, player_score, all_used_cards)
        
            # Stand
            elif action == '2':
                dealer_turn = dealerPlay(dealer_hand, dealer_score, all_used_cards)

                if dealer_turn > sum(player_score) and dealer_turn <= 21:
                    print('You lose!\n')
                elif dealer_turn == sum(player_score):
                    print('Push!\n')
                else:
                    print('You win!\n')
                break
        
            # Leave
            elif action == '3':
                leave()
        
            else:
                print('Unknown value.\n')
                continue
        
            ''' Round results '''
    
            # Bust
            if sum(player_score) > 21:
                print('Bust!\n')
                break
        
            # Blackjack
            elif sum(player_score) == 21:

                # Natural blackjack
                playerNaturalBJChecker(player_hand, dealer_primary_card, all_used_cards)
                break


''' Initiation '''

if __name__ == '__main__':
    main()