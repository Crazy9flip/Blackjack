# Do some refactoring and add if __name__ == '__main__'!
# Add config.py to modify game rules!

from deck import deck
import random
from collections import Counter


def leave():
	input('C\'ya, puta!')
	quit()


def print_cur_results(cards, score):
	print('Current hand: ', end='')
	for i in cards:
		print(i, end=' ')
	print('\nScore: ' + str(score))


def dealer_hand(primary_card, primary_val):

	cur_hand = []
	dealer_score = []

	cur_hand.append(primary_card)
	dealer_score.append(primary_val)

	while sum(dealer_score) < 17:
		tmp_key, tmp_val = random.choice(list(deck.items()))
	
		cur_hand.append(tmp_key)
	
		# 4 колоды
		hand_counter = dict(Counter(cur_hand))
		if hand_counter[tmp_key] > 4:
			cur_hand.pop()
			continue
		
		dealer_score.append(tmp_val)
	
		# Изменяемый туз
		while sum(dealer_score) > 21 and 11 in dealer_score:
			ace_index = dealer_score.index(11)
			dealer_score[ace_index] = 1 

		print_cur_results(cur_hand, sum(dealer_score)) 

	return sum(dealer_score)


print('\nWell, well, well, if it ain\'t gambling motherfucker again.\n')

# Game loop
while True:

	cur_hand = []
	player_score = []

	# Первичная карта дилера
	tmp_key_dealer, tmp_val_dealer = random.choice(list(deck.items()))
	print('Dealer\'s got ' + tmp_key_dealer + ' and (hole card)')
	
	# Round loop
	while True:
	
		# Действия игрока
		action = input('\nWhat do we do? ( 1 - Hit | 2 - Stand | 3 - Leave ) : ')
	
		# Hit
		if action == '1':
	
			tmp_key, tmp_val = random.choice(list(deck.items()))
	
			cur_hand.append(tmp_key)
	
			# 4 колоды
			hand_counter = dict(Counter(cur_hand))
			if hand_counter[tmp_key] > 4:
				cur_hand.pop()
				continue
			
			player_score.append(tmp_val)
	
			# Изменяемый туз
			while sum(player_score) > 21 and 11 in player_score:
				ace_index = player_score.index(11)
				player_score[ace_index] = 1 

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
	
	
		# Проверка результатов раунда
		if sum(player_score) > 21:
			print('Bust!\n')
			break
	
		# Ситуация с двумя блэкджеками (неверные правила!)
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