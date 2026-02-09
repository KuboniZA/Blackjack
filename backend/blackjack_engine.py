import random


class GameEngine:
    def __init__(self):
        self.suits = ["hearts", "diamonds", "spades", "clubs"]
        self.user_cards = []
        self.computer_card = []
        self.user_points = 0
        self.computer_points = 0
        self.computer_hidden_point = 0
        self.heart_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.diamond_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.spade_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.club_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.budget = 1000
        self.points_dictionary = {
            "ace": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "jack": 10,
            "queen": 10,
            "king": 10,
        }

    def new_game_state(self):
        card_suit = ""
        rank = ""

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

            self.user_cards.append((card_suit, rank))

        initial_user_cards = self.user_cards
        user_card_value1 = initial_user_cards[0][1]
        user_card_value2 = initial_user_cards[1][1]

        for user_point1 in self.points_dictionary:
            if user_card_value1 in self.points_dictionary:
                self.user_points += self.points_dictionary[user_card_value1]
                break

        for user_point2 in self.points_dictionary:
            if user_card_value2 in self.points_dictionary:
                self.user_points += self.points_dictionary[user_card_value2]
                break

        return self.user_cards, self.user_points

    def ai_new_game(self):
        card_suit = ""
        rank = ""

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
            self.computer_card.append((card_suit, rank))

        initial_ai_cards = self.computer_card
        ai_card_value1 = initial_ai_cards[0][1]
        ai_card_value2 = initial_ai_cards[1][1]

        for computer_point1 in self.points_dictionary:
            if ai_card_value1 in self.points_dictionary:
                self.computer_hidden_point += self.points_dictionary[ai_card_value1]
                break

        for computer_point2 in self.points_dictionary:
            if ai_card_value2 in self.points_dictionary:
                self.computer_points += self.points_dictionary[ai_card_value2]
                break

        return self.computer_card, self.computer_points, self.computer_hidden_point

    def check_deck(self):
        card_count = (
            len(self.heart_ranks)
            + len(self.diamond_ranks)
            + len(self.spade_ranks)
            + len(self.club_ranks)
        )
        return {"card_count": card_count}

    def reset_game(self):
        self.user_cards = []
        self.computer_card = []
        self.user_points = 0
        self.computer_points = 0
        self.computer_hidden_point = 0
        self.heart_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.diamond_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.spade_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]
        self.club_ranks = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "jack",
            "queen",
            "king",
        ]

    def chip_counter(self):
        bank = self.budget

    # def game_loop(self):

    #     user_card2 = random.choice(suits)
    #     user_rank2 = random.choice(ranks)
    #     self.user_cards[user_card2] = user_rank2

    #     self.user_cards.append(user_card2)
    #         computer_card1 = int(random.choice(cards))
    #         computer_cards.append(computer_card1)
    #         user_score = user_card1 + user_card2
    #         print(f"Your cards are: {self.user_cards}, current score is: {user_score}\n"
    #             f"The computer's first card is: {computer_card1}")
    #         bust = user_score > 21

    #         while not bust:
    #             more_cards = input("Type 'y' to get another card or 'n' to pass:\n").lower()
    #             if more_cards == "y":
    #                 user_card3 = int(random.choice(cards))
    #                 user_score += user_card3
    #                 self.user_cards.append(user_card3)
    #                 if user_score > 21:
    #                     bust = True
    #                     print(f"😫 YOU LOSE 😭: Your final hand is: {self.user_cards}. Your final score is: {user_score}\n"
    #                             f"The computer's score is: {computer_card1}")
    #                 else:
    #                     print(f"Your cards are: {self.user_cards}, current score is: {user_score}\n"
    #                             f"The computer's first card is: {computer_card1}")
    #             elif more_cards == "n":
    #                 computer_score = computer_card1
    #                 if computer_score > user_score:
    #                     bust = True
    #                     print(f"😫 YOU LOSE 😭: Your final hand is {self.user_cards}. Your final score is: {user_score}\n"
    #                         f"The computer's final hand is: {computer_cards}. The computer's final score is: {computer_card1}")
    #                 else:
    #                     computer_card2 = int(random.choice(cards))
    #                     while computer_score <= user_score and computer_score < 21:
    #                         computer_score += computer_card2
    #                         computer_cards.append(computer_card2)
    #                     if computer_score > 21:
    #                         bust = True
    #                         print(f"😎 YOU WIN 🥇: Your final hand is {self.user_cards}. Your final score is: {user_score}\n"
    #                             f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #                     elif computer_score > user_score and computer_score <= 21:
    #                         bust = True
    #                         print(f"😫 YOU LOSE 😭: Your final hand is {self.user_cards}. Your final score is: {user_score}\n"
    #                             f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #                     elif computer_score == user_score:
    #                         print(f"😕 DRAW 🫠: Your final hand is {self.user_cards}. Your final score is: {user_score}\n"
    #                             f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #                     else:
    #                         bust = True
    #                         print(f"😎 YOU WIN 🥇: Your final hand is {self.user_cards}. Your final score is: {user_score}\n"
    #                             f"The computer's final hand is {computer_cards}. The computer's final score is: {computer_score}")
    #         play_again = input("Would you like tp play again? Type 'y' or 'n':\n")
    #         if play_again == "y":
    #             card_choices()
    #         else:
    #             print("Thank you for playing! ☺️")


game_engine = GameEngine()

state = game_engine.ai_new_game()

print(state)
