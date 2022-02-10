import typing

from texas import cards, Player, Table, hand_value, EndGameException
def clear():
    clear = "\n" * 40
    print(clear)

def round(players: typing.List[Player], table: Table):
    for idx, player in enumerate(players):
        clear()
        table.dealer_move(player)
        if not player.is_playing:
            continue
        print(f"playera {idx+1} moves")
        print(f"==============================================")
        print("Your cards: ")
        [print(f" {cards}") for cards in player.cards]
        print(f"Card on table: ")
        [print(f" {cards}") for cards in table.visible_cards]
        print(f"==============================================")
        print(f"Minimal bet: {table.highest_bid or 0}")
        print(f"==============================================")
        print("You can : ")

        basic_moves = table.possible_moves()
        player_moves = player.moves_for_player(basic_moves)
        moves = {str(idx+1): opcja for idx, opcja in enumerate(player_moves)}
        for num, move in moves.items():
            print(f"{num}. {move} ")
        actions = {
            idx: getattr(player, move)
            for idx, move in moves.items()
        }

        action_num = None
        while action_num not in actions:
            action_num = input("What do you wish to do? write number of action ")
        action = actions[action_num](mini=max(1,table.highest_bid))
        table.interact(action, player)

def sit_players(deck: cards):
    player_number = 0
    while player_number not in range(2, 9):
        try:
            player_number = int(input("How many players? "))
        except ValueError:
            player_number = 0
    return [Player([deck.pop() for _ in range(2)]) for _ in range(player_number)]

def game(players: typing.List[Player], table: Table):
    try:
        while len([g for g in players if g.is_playing]) > 1 and len([g for g in players if g.all_in]) < len([g for g in players]):
            round(players, table)
        raise EndGameException()
    except EndGameException:
        pass
    finally:
        if len([g for g in players if g.is_playing]) != 0:
            result = {}
            table.visible_cards += ([table.cards.pop() for _ in list(table.cards)])
            for idx, player in enumerate(players):
                if player.is_playing:
                    result[idx] = hand_value(player.cards + table.visible_cards)
                    print(f"Player {idx+1} hand : {player.cards + table.visible_cards}")
            winner = max(result, key=result.get)
            players[winner].money += table.jackpot

def main():
    deck = cards.shuffle_deck()
    players = sit_players(deck)
    table = Table([deck.pop() for _ in range(3)])

    game(players, table)

    for idx, player in enumerate(players):
        print(f"Player {idx} ended with {player.money} USD")

if __name__ == "__main__":
        main()