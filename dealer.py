from deck import deck
import random as r

def dealer_hand():
	score = 0
	while score <= 16:
		tmp_act_key_dealer, tmp_act_val_dealer = r.choice(list(deck.items()))
		score += tmp_act_val_dealer
	return score