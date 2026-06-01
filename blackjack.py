import random 
import blackjack_list as bl
from art import blackjack_logo

# Dictionary for blackjack card values
deck_card = bl.deck_card

def deal_card():
    """ select random cards """
    random_card = random.choice(list(deck_card.keys()))
    value = deck_card[random_card]
    return value
    
def calculate_score(card_hand):
    """ total score of the blackjack cards """
    running_total = 0
    for hand in card_hand:
        running_total += hand
    while running_total > 21 and 11 in card_hand:
        running_total -= 10
    if len(card_hand) == 2 and running_total == 21:
        return 0
    else:
        return running_total

def compare_score(player_score, dealer_score, player_num=1):
    """ compare the player score to the dealer score"""
    print(f"\n{'='*40}")
    print(f"🃏  PLAYER {player_num} RESULTS")
    print(f"{'='*40}")
    if player_score == 0:
        print(f"🎉 BLACKJACK! Player {player_num} wins!")
    elif player_score > 21:
        print(f"💥 Player {player_num} busted with {player_score}! Dealer wins.")
    elif dealer_score == 0:
        print(f"🏦 Dealer has Blackjack! Player {player_num} loses.")
    elif dealer_score > 21:
        print(f"💥 Dealer busted with {dealer_score}! Player {player_num} wins! 🎉")
    elif player_score == dealer_score:
        print(f"🤝 It's a draw! Both scored {player_score}.")
    elif player_score > dealer_score:
        print(f"🎉 Player {player_num} wins with {player_score} vs dealer's {dealer_score}!")
    elif player_score < dealer_score:
        print(f"😞 Dealer wins with {dealer_score} vs Player {player_num}'s {player_score}.")
    print(f"{'='*40}")

def play_game():
    """ To play blackjack game """
    print(blackjack_logo)

    # ask number of players
    while True:
        try:
            num_players = int(input("\n👥 How many players? (1-4): "))
            if 1 <= num_players <= 4:
                break
            else:
                print("⚠️  Please enter a number between 1 and 4.")
        except ValueError:
            print("⚠️  Please enter a valid number.")

    # initialise hands and scores for all players
    all_hands = [[] for _ in range(num_players)]
    dealer_hand = []

    # deal 2 cards to each player and dealer
    for i in range(num_players):
        for _ in range(2):
            all_hands[i].append(deal_card())
    for _ in range(2):
        dealer_hand.append(deal_card())

    # calculate initial scores
    all_scores = [calculate_score(hand) for hand in all_hands]
    dealer_score = calculate_score(dealer_hand)

    # show initial hands
    print(f"\n{'='*40}")
    print(f"🏦 DEALER'S VISIBLE CARD: {dealer_hand[0]}")
    print(f"{'='*40}")
    for i in range(num_players):
        print(f"🃏 Player {i+1} hand: {all_hands[i]} | Score: {all_scores[i] if all_scores[i] != 0 else 'BLACKJACK!'}")

    # check immediate blackjack
    game_continue = True
    if 0 in all_scores or dealer_score == 0:
        print(f"\n🏦 Dealer's full hand: {dealer_hand} | Score: {dealer_score if dealer_score != 0 else 'BLACKJACK!'}")
        for i in range(num_players):
            compare_score(all_scores[i], dealer_score, i+1)
        game_continue = False

    # each player takes their turn
    if game_continue:
        for i in range(num_players):
            print(f"\n{'='*40}")
            print(f"🃏 PLAYER {i+1}'S TURN")
            print(f"{'='*40}")

            while True:
                print(f"\n👤 Player {i+1} hand: {all_hands[i]} | Score: {all_scores[i]}")
                hit_or_stand = input(f"\nPlayer {i+1} — Hit or Stand? ").lower()

                if hit_or_stand == "hit":
                    all_hands[i].append(deal_card())
                    all_scores[i] = calculate_score(all_hands[i])
                    print(f"\n✅ Player {i+1} drew a card!")
                    print(f"👤 Player {i+1} hand: {all_hands[i]} | Score: {all_scores[i]}")
                    if all_scores[i] > 21:
                        print(f"💥 Player {i+1} busted with {all_scores[i]}!")
                        break

                elif hit_or_stand == "stand":
                    print(f"\n🛑 Player {i+1} stands with {all_scores[i]}.")
                    break

                else:
                    print("⚠️  Please type 'hit' or 'stand'.")

        # dealer draws
        print(f"\n{'='*40}")
        print(f"🏦 DEALER'S TURN")
        print(f"{'='*40}")
        print(f"🏦 Dealer reveals full hand: {dealer_hand} | Score: {dealer_score}")

        while dealer_score != 0 and dealer_score < 17:
            dealer_hand.append(deal_card())
            dealer_score = calculate_score(dealer_hand)
            print(f"🏦 Dealer draws... {dealer_hand} | Score: {dealer_score}")

        if dealer_score >= 17:
            print(f"\n🛑 Dealer stands with {dealer_score}.")

        # compare all players to dealer
        print(f"\n{'='*40}")
        print(f"📊 FINAL RESULTS")
        print(f"{'='*40}")
        for i in range(num_players):
            compare_score(all_scores[i], dealer_score, i+1)

