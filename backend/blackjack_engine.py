import random

greeting =  input("Would you like tp play Blackjack? Type 'y' or 'n':\n")

class GameEngine:

    def __init__(self):
        self.suits = ["hearts", "diamonds", "spades", "clubs"]
        self.heart_ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        self.diamond_ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        self.spade_ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack","queen", "king"]
        self.club_ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack","queen", "king"]

    def new_game_state(self):
        user_cards = []

        for card in range(2):
            while True:
                card_suit = random.choice(self.suits)

                if card_suit == "hearts" and len(self.heart_ranks) > 0:
                    rank = random.choice(self.heart_ranks)
                    self.heart_ranks.remove(rank)
                    break

                elif card_suit == "diamonds" and len(self.diamond_ranks) > 0:
                    rank = random.choice(self.diamond_ranks)
                    self.diamond_ranks.remove(rank)
                    break

                elif card_suit == "spades" and len(self.spade_ranks) > 0:
                    rank = random.choice(self.spade_ranks)
                    self.spade_ranks.remove(rank)
                    break

                elif card_suit == "clubs" and len(self.club_ranks) > 0:
                    rank = random.choice(self.club_ranks)
                    self.club_ranks.remove(rank)
                    break

            user_cards.append((card_suit, rank))

        return user_cards


    def check_deck(self):
        return {
            "hearts": self.heart_ranks,
            "diamonds": self.diamond_ranks,
            "spades": self.spade_ranks,
            "clubs": self.club_ranks,
        }


    # def card_choices(self):
    #     user_cards = {}
    #     computer_cards = []
    #     cards = []

        # print(user_rank1)

        # user_cards[user_card1] = user_rank1
        #
        # user_card2 = random.choice(suits)
        # user_rank2 = random.choice(ranks)
        # user_cards[user_card2] = user_rank2

        # user_cards.append(user_card2)
    #     computer_card1 = int(random.choice(cards))
    #     computer_cards.append(computer_card1)
    #     user_score = user_card1 + user_card2
    #     print(f"Your cards are: {user_cards}, current score is: {user_score}\n"
    #           f"The computer's first card is: {computer_card1}")
    #     bust = user_score > 21
    #
    #
    #     while not bust:
    #         more_cards = input("Type 'y' to get another card or 'n' to pass:\n").lower()
    #         if more_cards == "y":
    #             user_card3 = int(random.choice(cards))
    #             user_score += user_card3
    #             user_cards.append(user_card3)
    #             if user_score > 21:
    #                 bust = True
    #                 print(f"😫 YOU LOSE 😭: Your final hand is: {user_cards}. Your final score is: {user_score}\n"
    #                         f"The computer's score is: {computer_card1}")
    #             else:
    #                 print(f"Your cards are: {user_cards}, current score is: {user_score}\n"
    #                         f"The computer's first card is: {computer_card1}")
    #         elif more_cards == "n":
    #             computer_score = computer_card1
    #             if computer_score > user_score:
    #                 bust = True
    #                 print(f"😫 YOU LOSE 😭: Your final hand is {user_cards}. Your final score is: {user_score}\n"
    #                       f"The computer's final hand is: {computer_cards}. The computer's final score is: {computer_card1}")
    #             else:
    #                 computer_card2 = int(random.choice(cards))
    #                 while computer_score <= user_score and computer_score < 21:
    #                     computer_score += computer_card2
    #                     computer_cards.append(computer_card2)
    #                 if computer_score > 21:
    #                     bust = True
    #                     print(f"😎 YOU WIN 🥇: Your final hand is {user_cards}. Your final score is: {user_score}\n"
    #                         f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #                 elif computer_score > user_score and computer_score <= 21:
    #                     bust = True
    #                     print(f"😫 YOU LOSE 😭: Your final hand is {user_cards}. Your final score is: {user_score}\n"
    #                         f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #                 elif computer_score == user_score:
    #                     print(f"😕 DRAW 🫠: Your final hand is {user_cards}. Your final score is: {user_score}\n"
    #                         f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #                 else:
    #                     bust = True
    #                     print(f"😎 YOU WIN 🥇: Your final hand is {user_cards}. Your final score is: {user_score}\n"
    #                         f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #     play_again = input("Would you like tp play again? Type 'y' or 'n':\n")
    #     if play_again == "y":
    #         card_choices()
    #     else:
    #         print("Thank you for playing! ☺️")
    #
    # if greeting == "y":
    #     card_choices()
    # else:
    #     print("Thank you for visiting Kuboni Blackjack. Please refresh to start again.")

# game_engine = GameEngine()

# deck = game_engine.check_deck()
# player_cards = game_engine.new_game_state()

# print(player_cards)
# print(deck)
