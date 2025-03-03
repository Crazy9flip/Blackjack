# Ace's value must change mid-game if needed!
# Dealer must tip a card if the score < cur_hand in main.py

from deck import deck
import random as r

def dealer_hand():
	score = 0
	while score <= 16:
		tmp_act_key_dealer, tmp_act_val_dealer = r.choice(list(deck.items()))
		if tmp_act_key_dealer.startswith("A"):
			if score <= 10:
				tmp_act_val_dealer = 11
			else:
				tmp_act_val_dealer = 1
		score += tmp_act_val_dealer
	return score