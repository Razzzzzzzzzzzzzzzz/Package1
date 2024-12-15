from CardGame import CardGame

player_one_name = input("Enter the first player name: ")
player_two_name = input("Enter the second player name: ")
card_game = CardGame(player_one_name, player_two_name)
print(card_game.player_one)
print(card_game.player_two)
for game_round in range(1,11):
    player_one_card = card_game.player_one.get_card()
    player_two_card = card_game.player_two.get_card()
    player_one_won = player_one_card > player_two_card
    if player_one_won:
        round_winner = card_game.player_one.name
        card_game.player_one.add_card(player_one_card)
        card_game.player_one.add_card(player_two_card)
    else:
        round_winner = card_game.player_two.name
        card_game.player_two.add_card(player_one_card)
        card_game.player_two.add_card(player_two_card)
    print(f"[Round {game_round} winner: {round_winner}]\n"
          f"{card_game.player_one.name} card: {player_one_card} - {card_game.player_two.name} card: {player_two_card}")

player_one_total_cards = len(card_game.player_one.player_cards)
player_two_total_cards = len(card_game.player_two.player_cards)

if player_one_total_cards > player_two_total_cards:
    print(f"{card_game.player_one.name} Won the game! {player_one_total_cards} - {player_two_total_cards}")
elif player_one_total_cards < player_two_total_cards:
    print(f"{card_game.player_two.name} Won the game! {player_one_total_cards} - {player_two_total_cards}")
else:
    print("It's a draw!")