'''
run = True
while run == True:

	cur_round = True
	cur_hand = 0

	try:
		action = int(input('\nOne more? ( 1 - Begin | 2 - Leave ) : '))
	
		if action == 2:
			leave()
	
		elif action == 1:
			while cur_round == True:
	
				if cur_hand == 21:
					print('You lucky bastard!')
					cur_round = False
	
				elif cur_hand < 21:
					try:
						action_begun = int(input('What do we do? ( 1 - Tap | 2 - Pass | 3 - Leave ) : '))
			
						if action_begun == 1:
							tmp_act_key, tmp_act_val = random.choice(list(deck.items()))
							print('You got', tmp_act_key)
							if tmp_act_key.startswith("A"):
								if cur_hand <= 10:
									tmp_act_val = 11
								else:
									tmp_act_val = 1
							cur_hand += tmp_act_val
							print('Score:', cur_hand)
		
						elif action_begun == 2:
							x = dealer_hand(cur_hand)
							print('Dealer\'s got', x)
							if x > 21:
								print('Not dealer\'s day!')
							elif x == cur_hand:
								print('It\'s a tie!')
							elif x > cur_hand:
								print('You lose!')
							elif x < cur_hand:
								print('You win!')
							cur_round = False
		
						elif action_begun == 3:
							leave()
		
						else:
							print('Unknown value.')
							continue

					except ValueError:
						print('ValueErrorandom.')
						print('Score:', cur_hand)
	
				elif cur_hand > 21:
					print('Not your day!')
					break
	
		else:
			print('Unknown value.')
			continue

	except ValueError:
		print('ValueErrorandom.') 








					# Изменяемый туз  |  не работает нихера
			if sum(player_score) > 21:
				for i in cur_hand:
					if i.startswith('A'):
						index = cur_hand.index(i) # Проблема в index(). Она возращает первое совпадение в списке. И если i = 'As', то index() вернется вначало списка и будет там искать 'As'
						if player_score[index] == 1:
							continue
						player_score[index] = 1 




						
def dealer_hand():
	score = 0
	played_cards = []
	while score <= 17:
		tmp_key, tmp_val = random.choice(list(deck.items()))
		if tmp_key.startswith("A"):
			if score <= 10:
				tmp_val = 11
			else:
				tmp_val = 1
		score += tmp_val
		print(tmp_key + ' - ' + str(score))
	return score

def dealer_hand():

	tmp_key, tmp_val = random.choice(list(deck.items()))

	# 4 колоды
	hand_counter = dict(Counter(cur_hand))
	hand_counter_key, hand_counter_val = list(hand_counter.items())
	for i in hand_counter_key:
		if hand_counter_val == 4:
			continue

	cur_hand.append(tmp_key)
	sum(player_score) += tmp_val

	# Изменяемый туз
	if sum(player_score) > 21:
		for i in cur_hand:
			if i.startswith('A'):
				sum(player_score) -= 10
'''