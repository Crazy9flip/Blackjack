from deck import deck
from dealer import dealer_hand
import random as r

print('Well, well, well, if it ain''t gambling motherfucker again.')

run = True
while run == True:

	cur_round = True
	cur_hand = 0

	action = int(input('\nOne more? ( 1 - Begin | 2 - Leave ) : '))
	
	if action == 2:
		input('C''ya, puta!')
		break

	elif action == 1:
		while cur_round == True:

			if cur_hand == 21:
				print('You lucky bastard!')
				cur_round = False

			elif cur_hand < 21:

				action_begun = int(input('What do we do? ( 1 - Tap | 2 - Pass | 3 - Leave ) : '))
	
				if action_begun == 1:
					tmp_act_key, tmp_act_val = r.choice(list(deck.items()))
					print('You got', tmp_act_key)
					cur_hand += tmp_act_val
					print('Score:', cur_hand)

				elif action_begun == 2:
					x = dealer_hand()
					print('Dealer''s got', x)
					if x > 21:
						print('Not dealer\'s day!')
					elif x == cur_hand:
						print('It''s a tie!')
					elif x > cur_hand:
						print('You lose!')
					elif x < cur_hand:
						print('You win!')
					cur_round = False

				elif action_begun == 3:
					input('C''ya, puta!')
					quit()

			elif cur_hand > 21:
				print('Not your day!')
				break

	else:
		print('Unknown value.')
		continue