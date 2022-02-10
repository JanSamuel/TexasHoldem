# TexasHoldem
Project by Jan Samuel Owczarek
Simple console based game of Poker

This was created in part during Basic Python course with @mwozniczak (https://github.com/mw-katas/)

What it intends to do:
- Shuffle cards
- Each player receives two cards
- Three cards are on table, they are not visible for players
- Player can wait, fold, or bid
- Wait can be only done if no bid were placed
- Fold ends game for specific player money bided are lost
- Bid player can put some amount on table
- Other player must put >= of last player bid or fold
- Player can bid all-in putting all money on to the table, all-in can be lower than highest bid
- If all Players bided same amount round ends
- New round start with one of cards from table being reveled
- Game ends if all cards are reveled on table or only one player stays in game
- If more than one player is left hand strength is calculated for each
- All money from table is received by player with stronger hand

To run game:
Python3 ./holdem.py

To run tests:
python -m pytest --doctest-modules