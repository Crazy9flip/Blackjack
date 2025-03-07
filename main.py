# Dealer must show his first card!
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


def dealer_hand():

	cur_hand = []
	dealer_score = []

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


print('Well, well, well, if it ain\'t gambling motherfucker again.')


while True:

	cur_hand = []
	player_score = []
	
	run = True
	while run:
	
		# Взять карту / Остановиться
	
		a = input('\nWhat do we do? ( 1 - Hit | 2 - Pass | 3 - Leave ) : ')
	
		if a == '1':
	
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
	
		elif a == '2':
			dealer_turn = dealer_hand()
			if dealer_turn > sum(player_score) and dealer_turn <= 21:
				print('You lose!')
			else:
				print('You win!')
			break
	
		elif a == '3':
			leave()
	
		else:
			print('Unknown value.')
			continue
	
	
		# Проверка результатов раунда
	
		if sum(player_score) > 21:
			print('Bust!')
			break
	
		elif sum(player_score) == 21:
			print('BJ!')
			break
			# Ход дилера (перепроверить правила блэкджека)
	
		else:
			pass