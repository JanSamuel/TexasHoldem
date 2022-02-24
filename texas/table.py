import typing
from typing import List


from .player import Player
from .structs import Outcome, EndGameException

class Table():
    def __init__(self, cards:typing.List[str]) -> None:
        self.cards = cards
        self.visible_cards = []
        self.jackpot = 0
        self.highest_bid = 0
        self.last_bidder = 0
        
    def interact(self, outcome: Outcome, player: Player):
        if outcome.interaction == "fold":
            return

        if self.last_bidder == None or (outcome.interaction == "bet" and self.highest_bid < outcome.outcome_value):
            self.last_bidder = player

        if outcome.interaction == "bet":
            self.jackpot += outcome.outcome_value
            self.highest_bid = max(outcome.outcome_value, self.highest_bid)

    def dealer_move(self, player: Player):
        if player is self.last_bidder:
            if self.cards:
                self.visible_cards.append(self.cards.pop())
            else:
                self.end_game()
    def end_game(self):
        raise EndGameException()

    def possible_moves(self):
        if self.jackpot == 0:
            return{"fold","wait","bet"}
        return {"fold", "bet"}
