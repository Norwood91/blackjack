import random

# Create constant variables to hold the values for J, Q and K
JACK = 10
QUEEN = 10
KING = 10

# Initiate Ace as 11
ace = 11

user_score = 0
dealer_score = 0

# Create placeholder hand to add cards to
user_hand = []

# Create placeholder hand for the dealer
dealer_hand = []

# Create placeholder list to add the deck of cards to
deck_of_cards = []

game_running = True
while game_running:

    # Create list of suites
    suite_for_cards = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

    # Depending on the score, the value of Ace will either be 11 or 1
    if user_score > 21 or dealer_score > 21:
        ace -= 10
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ace]
    else:
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ace]

    # Create the deck of 52 cards with the suite and value
    for suite in suite_for_cards:
        for value in card_values:
            deck_of_cards.append({'suite': suite, 'value': value})


    def create_hand(deck):
        card_1 = random.choice(deck)
        card_2 = random.choice(deck)
        card_one_notice = f"Your first card is: {card_1['value']} of {card_1['suite']}"
        card_two_notice = f"Your second card is: {card_2['value']} of {card_2['suite']}"
        print(card_one_notice)
        print(card_two_notice)
        card_one = card_1['value']
        card_two = card_2['value']
        user_hand.append(card_one)
        user_hand.append(card_two)


    # Create the user's hand
    user_card_1 = random.choice(deck_of_cards)
    user_card_1_suite = user_card_1['suite']
    user_card_1_value = user_card_1['value']
    print()
    card_one_notice = f"Your first card is: {user_card_1_value} of {user_card_1_suite}"
    print(card_one_notice)
    card_one = user_card_1_value
    user_hand.append(card_one)

    user_card_2 = random.choice(deck_of_cards)
    user_card_2_suite = user_card_2['suite']
    user_card_2_value = user_card_2['value']
    if user_card_1 == user_card_2:
        user_card_2 = random.choice(deck_of_cards)
        user_card_2_suite = user_card_2['suite']
        user_card_2_value = user_card_2['value']
    card_two_notice = f"Your second card is: {user_card_2_value} of {user_card_2_suite}"
    print(card_two_notice)
    card_two = user_card_2_value
    user_hand.append(card_two)
    user_score = sum(user_hand)
    print("Your current score is: ", user_score)
    print()

    # Create dealer's hand
    dealer_card_1 = random.choice(deck_of_cards)
    dealer_card_1_suite = dealer_card_1['suite']
    dealer_card_1_value = dealer_card_1['value']
    dealer_card_one_notice = f"The dealer's first card is: {dealer_card_1_value} of {dealer_card_1_suite}"
    print(dealer_card_one_notice)
    dealer_card_one = dealer_card_1_value
    dealer_hand.append(dealer_card_one)

    dealer_card_2 = random.choice(deck_of_cards)
    dealer_card_2_suite = dealer_card_2['suite']
    dealer_card_2_value = dealer_card_2['value']
    if dealer_card_1 == dealer_card_2:
        dealer_card_2 = random.choice(deck_of_cards)
        dealer_card_2_suite = dealer_card_2['suite']
        dealer_card_2_value = dealer_card_2['value']
    dealer_card_two_notice = f"The dealer's second card is: {dealer_card_2_value} of {dealer_card_2_suite}"
    print(dealer_card_two_notice)
    dealer_card_two = dealer_card_2_value
    dealer_hand.append(dealer_card_two)
    dealer_score = sum(dealer_hand)
    print("The dealer's current score is: ", dealer_score)
    print()

    # Compare user's score to Dealer's score
    if user_score > 21 and dealer_score > 21:
        print(f"Your score is: {user_score}, and the dealer's score is: {dealer_score}\nBoth of your hands"
              f" were a BUST. You BOTH LOSE!")
    elif user_score > 21 and dealer_score <= 21:
        print(f"Your score is: {user_score}, and the dealer's score is: {dealer_score}\nYour hand was over 21,"
              f" It was a BUST. YOU LOSE!")
    elif user_score <= 21 and dealer_score > 21:
        print(f"Your score is: {user_score}, and the dealer's score is: {dealer_score}\nThe dealer's hand was over 21,"
              f" It was a BUST. You WIN!")
    elif user_score == dealer_score:
        print(f"Your score is: {user_score}, and the dealer's score is: {dealer_score}\nIt's a two-way TIE!")
    elif user_score > dealer_score and user_score <= 21:
        print(f"Your score is: {user_score}, and the dealer's score is: {dealer_score}\nYou WIN!")
    elif user_score < dealer_score and dealer_score <= 21:
        print(f"Your score is: {user_score}, and the dealer's score is: {dealer_score}\n")
        hold_or_hit = input("Would you like to HOLD or HIT?: Type 'hold' or 'hit':\n").lower()
        if hold_or_hit == "hit":
            extra_card = random.choice(deck_of_cards)
            extra_card_suite = dealer_card_2['suite']
            extra_card_value = dealer_card_2['value']
            if extra_card == user_card_1 or extra_card == user_card_2:
                extra_card = random.choice(deck_of_cards)
                extra_card_suite = dealer_card_2['suite']
                extra_card_value = dealer_card_2['value']
            else:
                extra_card_notice = f"Your extra card is: {extra_card_value} of {extra_card_suite}"
                print(extra_card_notice)
                xtra_card = extra_card_value
                user_hand.append(xtra_card)
                user_score = sum(user_hand)
                print("Your current score is: ", user_score)
                hold_or_hit = input("Would you like to HOLD or HIT?: Type 'hold' or 'hit':\n").lower()
        elif hold_or_hit == "hold":
            print(f"You chose to hold with the hand: {user_card_1_value} of {user_card_1_suite}"
                  f" and {user_card_2_value} of {user_card_2_suite}. Your final score is: {user_score}.")
            if dealer_score > user_score and dealer_score <= 21:
                print(f"You LOSE! The dealer had a score of {dealer_score} and you finished with a score of"
                      f" {user_score}.")
            elif user_score > dealer_score and user_score <= 21:
                print(f"You WIN! The dealer had a score of {dealer_score} and you finished with a score of"
                      f" {user_score}.")
    print()

    play_again = input("Would you like to play again? Type 'yes' or type 'no':\n").lower()

    if play_again == 'no':
        game_running = False
        # If yes, empty user and dealer hand(s) list and add two new cards