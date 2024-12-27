import random
import time

JACK = 10
QUEEN = 10
KING = 10
ace = 11

user_score = 0
dealer_score = 0

user_hand = []

dealer_hand = []

deck_of_cards = []

used_cards = []

game_running = True
while game_running:

    suite_for_cards = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

    if user_score > 21 or dealer_score > 21:
        ace -= 10
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ace]
    else:
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ace]

    for suite in suite_for_cards:
        for value in card_values:
            deck_of_cards.append({'suite': suite, 'value': value})


    def slight_pause(seconds):
        time.sleep(seconds)

    def add_screen_space():
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

    def create_starting_hand(deck, player_hand):
        card_one = random.choice(deck)
        card_two = random.choice(deck)

        if card_one == card_two:
            card_two = random.choice(deck_of_cards)

        card_one_value = card_one['value']
        card_one_suite = card_one['suite']

        card_two_value = card_two['value']
        card_two_suite = card_two['suite']


        if player_hand == user_hand:
            card_one_notice = f"Your first card is: {card_one_value} of {card_one_suite}"
            card_two_notice = f"Your second card is: {card_two_value} of {card_two_suite}"
        else:
            card_one_notice = f"The dealer's first card is: {card_one_value} of {card_one_suite}"
            card_two_notice = f"The dealer's second card is: {card_two_value} of {card_two_suite}"

        print(card_one_notice)
        slight_pause(1)
        print(card_two_notice)
        slight_pause(1)
        player_hand.append(card_one_value)
        player_hand.append(card_two_value)
        used_cards.append(card_one)
        used_cards.append(card_two)
        deck.remove(card_one)
        deck.remove(card_two)


    def add_new_card(deck, player_hand):
        global ace

        new_card = random.choice(deck)
        new_card_value = new_card['value']
        new_card_suite = new_card['suite']

        if new_card_value == ace and sum(player_hand) <= 10:
            new_card_value = 11
        elif new_card_value == ace and sum(player_hand) > 10:
            new_card_value = 1
        else:
            new_card_value == new_card_value
        if player_hand == user_hand:
            slight_pause(2)
            print(f"Your new card is: {new_card_value} of {new_card_suite}")
        else:
            slight_pause(2)
            print(f"The dealer's new card is: {new_card_value} of {new_card_suite}")
        player_hand.append(new_card_value)
        used_cards.append(new_card)
        deck.remove(new_card)


    def dealer_hit():
        global dealer_score

        while dealer_score < 17:
            slight_pause(1)
            print("The dealer chose to hit.")
            add_new_card(deck_of_cards, dealer_hand)
            dealer_score = sum(dealer_hand)
            slight_pause(1)
            print(f"The dealer's new score is: {dealer_score}")
            slight_pause(1)
        else:
            calculate_score(user_score, dealer_score)


    def player_hit():
        global user_score

        keep_asking_to_hit = True
        while keep_asking_to_hit:
            if user_score == 21 or dealer_score == 21:
                calculate_score(user_score, dealer_score)
                keep_asking_to_hit = False

            slight_pause(1)
            user_input = input("Would you like to stay or hit?: ").lower()
            if user_input == "hit":
                slight_pause(1)
                print("You chose to hit.")
                add_new_card(deck_of_cards, user_hand)
                user_score = sum(user_hand)
                slight_pause(1)
                print(f"Your new score is {user_score}")

                if user_score > 21:
                    calculate_score(user_score, dealer_score)
                    keep_asking_to_hit = False
            else:
                slight_pause(1)
                print(f"You chose to stay. Your score remains {user_score}.")
                dealer_hit()
                keep_asking_to_hit = False


    create_starting_hand(deck_of_cards, user_hand)
    user_score = sum(user_hand)
    slight_pause(1)
    print("Your current score is: ", user_score)
    print()

    slight_pause(2)
    create_starting_hand(deck_of_cards, dealer_hand)
    dealer_score = sum(dealer_hand)
    slight_pause(1)
    print("The dealer's current score is: ", dealer_score)
    slight_pause(2)
    print()


    # Compare user's score to Dealer's score
    def calculate_score(user_score, dealer_score):
        # If users score is greater than 21 and the Dealers score is greater than 21
        if user_score > 21 and dealer_score > 21:
            print("That's a bust, you lose The house wins.")
        # If user score is greater than 21 and the dealers score is less than 21
        elif user_score > 21 and dealer_score <= 21:
            print("That's a bust, you lose! The house wins.")
        # If user score is less than or equal to 21 and the dealers score is over 21
        elif user_score <= 21 and dealer_score > 21:
            print("You win! The house busted.")
        # If user score is greater than dealer score but less than or equal to 21
        elif user_score > dealer_score and user_score <= 21:
            print("You win!")
        # If dealer score is greater than user score but less than or equal to 21
        elif dealer_score > user_score and dealer_score <= 21:
            print("You lose, the dealer wins.")
        else:
            print("It's a PUSH, no one wins.")


    if user_score == 21 or dealer_score == 21:
        calculate_score(user_score, dealer_score)
        play_again
    else:
        player_hit()
        slight_pause(2)
        play_again = input("Would you like to play again? Type 'yes' or type 'no': ").lower()

        if play_again == "no":
            game_running = False
            print("Thanks for playing, goodbye!")
        else:
            add_screen_space()
            dealer_hand.clear()
            user_hand.clear()
            used_cards.clear()
            deck_of_cards.clear()
            dealer_score = 0
            user_score = 0
