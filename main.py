# All the functions are declared in this module
# Make the decks common for both player and dealer!
# Add unique logic for multiple decks!
# Add variations!
# Add additional rules!

from deck import deck
from config import *

import random
from collections import Counter
from time import sleep


# Quit
def leave():
	input('C\'ya, puta!')
	quit()


# Number of decks configuration
def number_of_decks_checker():
	if SINGLE_DECK  ==  True:
		return 1  
	if TWO_DECKS    ==  True:
		return 2  
	if FOUR_DECKS   ==  True:
		return 4  
	if SIX_DECKS    ==  True:
		return 6  
	if EIGHT_DECKS  ==  True:
		return 8


# Card duplicates protector
def number_of_decks(used_cards, new_card, num_of_decks):
	hand_counter = dict(Counter(used_cards))
	if hand_counter[new_card] > num_of_decks:
		used_cards.pop()
		return True
	return False


# Interim results
def print_cur_results(cards, score):
	print('Current hand: ', end='')
	for i in cards:
		print(i, end=' ')
	print('\nScore: ' + str(score))


# Variable Ace
def variable_ace(score):
	while sum(score) > 21 and 11 in score:
		ace_index = score.index(11)
		score[ace_index] = 1 


# Dealer's turn
def dealer_hand(primary_card, primary_val):
	cur_hand = []
	dealer_score = []

	num_of_decks_checker = number_of_decks_checker()

	cur_hand.append(primary_card)
	dealer_score.append(primary_val)

	while sum(dealer_score) < 17:
		tmp_key, tmp_val = random.choice(list(deck.items()))
	
		cur_hand.append(tmp_key)
	
		# Duplicates checker
		if number_of_decks(cur_hand, tmp_key, num_of_decks_checker):
			continue
		
		dealer_score.append(tmp_val)
	
		variable_ace(dealer_score)

		print_cur_results(cur_hand, sum(dealer_score)) 

		sleep(1)

	return sum(dealer_score)


def main():

	''' Pre-game declarations '''
	
	print('\nWell, well, well, if it ain\'t gambling motherfucker again.\n')
	
	num_of_decks_checker = number_of_decks_checker()
	
	''' Game loop '''
	while True:
	
		cur_hand = []
		player_score = []
	
		# Dealer's primary card
		tmp_key_dealer, tmp_val_dealer = random.choice(list(deck.items()))
		print('Dealer\'s got ' + tmp_key_dealer + ' and (hole card)')
		
		''' Round loop '''
		while True:
		
			''' Player's actions '''
	
			action = input('\nWhat do we do? ( 1 - Hit | 2 - Stand | 3 - Leave ) : ')
		
			# Hit
			if action == '1':
		
				tmp_key, tmp_val = random.choice(list(deck.items()))
		
				cur_hand.append(tmp_key)
		
				# Duplicates checker
				if number_of_decks(cur_hand, tmp_key, num_of_decks_checker):
					continue
				
				player_score.append(tmp_val)
		
				variable_ace(player_score)
	
				print_cur_results(cur_hand, sum(player_score)) 
		
			# Stand
			elif action == '2':
				dealer_turn = dealer_hand(tmp_key_dealer, tmp_val_dealer)
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
		
			# Dealer and player both got blackjacks
			elif sum(player_score) == 21:
				print('Blackjack!\n')
				if tmp_key_dealer.startswith('A'):
					tmp_key_dealer, tmp_val_dealer = random.choice(list(deck.items()))
					print_cur_results(tmp_key_dealer, tmp_val_dealer)
					if tmp_val_dealer == 10:
						print('Push!\n')
					else:
						print('You win!\n')
				break
	
			else:
				pass


''' Initiation '''

if __name__ == '__main__':
	main()