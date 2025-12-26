from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
greeting =  input("Would you like tp play Blackjack? Type 'y' or 'n':\n")

def card_choices():
    user_cards = []
    computer_cards = []
    user_card1 = int(random.choice(cards))
    user_cards.append(user_card1)
    user_card2 = int(random.choice(cards))
    user_cards.append(user_card2)
    computer_card1 = int(random.choice(cards))
    computer_cards.append(computer_card1)
    user_score = user_card1 + user_card2
    print(f"Your cards are: {user_cards}, current score is: {user_score}\n"
          f"The computer's first card is: {computer_card1}")
    bust = user_score > 21

    while not bust:
        more_cards = input("Type 'y' to get another card or 'n' to pass:\n").lower()
        if more_cards == "y":
            user_card3 = int(random.choice(cards))
            user_score += user_card3
            user_cards.append(user_card3)
            if user_score > 21:
                bust = True
                print(f"😫 YOU LOSE 😭: Your final hand is: {user_cards}. Your final score is: {user_score}\n"
                        f"The computer's score is: {computer_card1}")
            else:
                print(f"Your cards are: {user_cards}, current score is: {user_score}\n"
                        f"The computer's first card is: {computer_card1}")
        elif more_cards == "n":
            computer_score = computer_card1
            if computer_score > user_score:
                bust = True
                print(f"😫 YOU LOSE 😭: Your final hand is {user_cards}. Your final score is: {user_score}\n"
                      f"The computer's final hand is: {computer_cards}. The computer's final score is: {computer_card1}")
            else:
                computer_card2 = int(random.choice(cards))
                while computer_score <= user_score and computer_score < 21:
                    computer_score += computer_card2
                    computer_cards.append(computer_card2)
                if computer_score > 21:
                    bust = True
                    print(f"😎 YOU WIN 🥇: Your final hand is {user_cards}. Your final score is: {user_score}\n"
                        f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
                elif computer_score > user_score and computer_score <= 21:
                    bust = True
                    print(f"😫 YOU LOSE 😭: Your final hand is {user_cards}. Your final score is: {user_score}\n"
                        f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
                elif computer_score == user_score:
                    print(f"😕 DRAW 🫠: Your final hand is {user_cards}. Your final score is: {user_score}\n"
                        f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
                else:
                    bust = True
                    print(f"😎 YOU WIN 🥇: Your final hand is {user_cards}. Your final score is: {user_score}\n"
                        f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    play_again = input("Would you like tp play again? Type 'y' or 'n':\n")
    if play_again == "y":
        card_choices()
    else:
        print("Thank you for playing! ☺️")

if greeting == "y":
    card_choices()
else:
    print("Thank you for visiting Kuboni Blackjack. Please refresh to start again.")

