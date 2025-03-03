# Ace's value must change mid-game if needed!

from deck import deck
import random as r

def dealer_hand(cur_hand):
	score = 0
	while score <= cur_hand:
		tmp_act_key_dealer, tmp_act_val_dealer = r.choice(list(deck.items()))
		if tmp_act_key_dealer.startswith("A"):
			if score <= 10:
				tmp_act_val_dealer = 11
			else:
				tmp_act_val_dealer = 1
		score += tmp_act_val_dealer
		print(tmp_act_key_dealer + ' - ' + str(score))
	return score