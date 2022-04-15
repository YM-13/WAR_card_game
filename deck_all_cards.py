import random
from cards import *


class Deck:
	def __init__(self):
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				'''create the Card object'''
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)

	def shuffle(self):
		# Note this doesn't return anything
		random.shuffle(self.all_cards)

	def deal_one(self):
		# Note we remove one card from the list of all_cards
		return self.all_cards.pop()
