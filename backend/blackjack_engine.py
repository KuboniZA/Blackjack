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
                if user_card_value1 == "ace":
                    self.user_points += 10
                    self.user_points += self.points_dictionary[user_card_value1]
                    break
                else:
                    self.user_points += self.points_dictionary[user_card_value1]
                    break

        for user_point2 in self.points_dictionary:
            if user_card_value2 in self.points_dictionary:
                if user_card_value1 == "ace" and user_card_value2 == "ten":
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points, "BLACKJACK"
                elif user_card_value1 == "ace" and user_card_value2 == "jack":
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points, "BLACKJACK"
                elif user_card_value1 == "ace" and user_card_value2 == "queen":
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points, "BLACKJACK"
                elif user_card_value1 == "ace" and user_card_value2 == "king":
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points, "BLACKJACK"
                elif self.user_points == 10 and user_card_value2 == "ace":
                    self.user_points += 10
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points, "BLACKJACK"
                elif user_card_value2 == "ace" and user_card_value1 !="ace":
                    self.user_points += 10
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points
                else:
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
                if ai_card_value1 == "ace":
                    self.computer_hidden_point += 10
                    self.computer_hidden_point += self.points_dictionary[ai_card_value1]
                    break
                else:
                    self.computer_hidden_point += self.points_dictionary[ai_card_value1]
                    break

        for computer_point2 in self.points_dictionary:
            if ai_card_value2 in self.points_dictionary:
                if ai_card_value1 == "ace" and ai_card_value2 == "ten":
                    self.computer_points += self.computer_hidden_point
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points, "BLACKJACK"
                elif ai_card_value1 == "ace" and ai_card_value2 == "jack":
                    self.computer_points += self.computer_hidden_point
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points, "BLACKJACK"
                elif ai_card_value1 == "ace" and ai_card_value2 == "queen":
                    self.computer_points += self.computer_hidden_point
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points, "BLACKJACK"
                elif ai_card_value1 == "ace" and ai_card_value2 == "king":
                    self.computer_points += self.computer_hidden_point
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points, "BLACKJACK"
                # This makes sure the score does not give away the hidden card by making a visible ace equal 1.
                elif ai_card_value1 == "ace" and ai_card_value2 == "ace":
                    self.computer_hidden_point -= 10
                    self.computer_points += 10
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points
                elif self.computer_hidden_point == 10 and ai_card_value2 == "ace":
                    self.computer_points += 10
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points, "BLACKJACK"
                elif ai_card_value2 == "ace" and ai_card_value1 !="ace":
                    self.computer_points += 10
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    return self.computer_card, self.computer_points
                else:
                    self.computer_points += self.points_dictionary[ai_card_value2]
                    break

        return self.computer_card, self.computer_points, # self.computer_hidden_point

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

    def user_turn(self):
        bust = self.user_points > 21

        card_suit = random.choice(self.suits)

        if card_suit == "hearts" and len(self.heart_ranks) > 0:
            rank = random.choice(self.heart_ranks)
            self.heart_ranks.remove(rank)

        elif card_suit == "diamonds" and len(self.diamond_ranks) > 0:
            rank = random.choice(self.diamond_ranks)
            self.diamond_ranks.remove(rank)

        elif card_suit == "spades" and len(self.spade_ranks) > 0:
            rank = random.choice(self.spade_ranks)
            self.spade_ranks.remove(rank)

        elif card_suit == "clubs" and len(self.club_ranks) > 0:
            rank = random.choice(self.club_ranks)
            self.club_ranks.remove(rank)

        self.user_cards.append((card_suit, rank))
        user_cards = self.user_cards
        new_card = user_cards[-1]
        new_card_pts = user_cards[-1][1]

        for user_point in self.points_dictionary:
            if new_card_pts in self.points_dictionary:
                self.user_points += self.points_dictionary[new_card_pts]
                if self.user_points > 21:
                    bust = True
                    computer_points = self.computer_points + self.computer_hidden_point
                    return new_card, self.user_points, self.computer_card, computer_points, "DEALER WINS!"
                else:
                    break

        return new_card, self.user_points
    
    def ai_turn(self):
        computer_points = self.computer_points + self.computer_hidden_point
        ai_bust = computer_points > 21
        if computer_points >= 17 and computer_points == self.user_points:
                    ai_bust = True
                    return self.computer_card, computer_points, "PUSH"
        elif computer_points <= 21 and computer_points > self.user_points:
                    ai_bust = True
                    return self.computer_card, computer_points, "DEALER WINS!"
        else:
            while not ai_bust:
                card_suit = random.choice(self.suits)

                if card_suit == "hearts" and len(self.heart_ranks) > 0:
                    rank = random.choice(self.heart_ranks)
                    self.heart_ranks.remove(rank)

                elif card_suit == "diamonds" and len(self.diamond_ranks) > 0:
                    rank = random.choice(self.diamond_ranks)
                    self.diamond_ranks.remove(rank)

                elif card_suit == "spades" and len(self.spade_ranks) > 0:
                    rank = random.choice(self.spade_ranks)
                    self.spade_ranks.remove(rank)

                elif card_suit == "clubs" and len(self.club_ranks) > 0:
                    rank = random.choice(self.club_ranks)
                    self.club_ranks.remove(rank)
                
                self.computer_card.append((card_suit, rank))
                ai_card_value = self.computer_card[-1][1]
                result = ""

                if ai_card_value in self.points_dictionary:
                    computer_points += self.points_dictionary[ai_card_value]
                    if computer_points >= 17 and computer_points == self.user_points:
                        ai_bust = True
                        result = "PUSH"
                    elif computer_points <= 21 and computer_points > self.user_points:
                        ai_bust = True
                        result = "DEALER WINS!"
                    elif computer_points > 21:
                        ai_bust = True
                        result = "YOU WIN!"
                    else:
                        continue

            return self.computer_card, computer_points, result


game_engine = GameEngine()

state = game_engine.ai_new_game()

print(state)
