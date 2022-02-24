import typing
from typing import List

from .structs import Outcome

class Player():
    def __init__(self, cards:typing.List[str], money:int = 200) -> None:
        self.cards = cards
        self.money = money
        self.all_in = False
        self.folded = False
    @property
    def is_playing(self):
        return not self.folded and (self.money > 0) or self.all_in

    def wait(self, *args, **kwargs):
        return Outcome("wait")

    def fold(self, *args, **kwargs):
        self.folded=True
        return Outcome("fold")
    
    def moves_for_player(self, acctions):
        if not self.money:
            return()
        return acctions

    def bet(self, mini:int = 1, *args, **kwargs):
        if mini >= self.money:
            decision = None
            while(decision not in ('y', 'n')):
                decision = input("You can only all-in. Do you want to bet all? y/n ").lower()
                if decision == "y":
                    outcome = Outcome("bet", outcome_value = self.money)
                    self.money = 0
                    self.all_in = True
                    return outcome
                else:
                    return self.fold()
        amount = 0
        while amount not in range(mini, self.money+1):
            try:
                amount = int(input("How much you bet? "))
                if amount > self.money:
                    print("Not enough money ")
                    raise ValueError()
            except ValueError:
                print("Wrong value ")
        if self.money == amount:
            self.all_in = True
        self.money -= amount
        return Outcome("bet", outcome_value = amount)
