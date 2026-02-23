import random
from typing_extensions import Literal


class GameEngine:
    def __init__(self) -> None:
        self.suits = ["hearts", "diamonds", "spades", "clubs"]
        self.user_cards = []
        self.computer_card = []
        self.user_points = 0
        self.computer_points = 0
        self.computer_hidden_point = 0
        # Tracks whether we've already adjusted an ace from 11->1 for the current user turn
        self.user_ace_adjusted = False
        self.computer_ace_adjusted = False
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
        self.bet_amount = 0
        self.winnings = 0
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
    
    def get_points(self):
        return self.user_points, self.computer_points

    def new_game_state(self) -> tuple[list, int, Literal['BLACKJACK'], int] | tuple[list, int, None, None]:
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

        # start of a new hand / user turn -> reset ace-adjust flag
        self.user_ace_adjusted = False

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
                if user_card_value1 == "ace" and user_card_value2 in ("ten", "jack", "queen", "king"):
                    self.user_points += self.points_dictionary[user_card_value2]
                    self.computer_points += self.computer_hidden_point
                    self.winnings += self.bet_amount
                    self.bet_amount = 0
                    self.winnings_tracker()
                    return self.user_cards, self.user_points, "BLACKJACK", self.computer_points
                elif self.user_points == 10 and user_card_value2 == "ace":
                    self.user_points += 10
                    self.user_points += self.points_dictionary[user_card_value2]
                    self.computer_points += self.computer_hidden_point
                    self.winnings += self.bet_amount
                    self.bet_amount = 0
                    self.winnings_tracker()
                    return self.user_cards, self.user_points, "BLACKJACK", self.computer_points
                elif user_card_value2 == "ace" and user_card_value1 !="ace":
                    self.user_points += 10
                    self.user_points += self.points_dictionary[user_card_value2]
                    return self.user_cards, self.user_points, None, None
                else:
                    self.user_points += self.points_dictionary[user_card_value2]
                    break

        return self.user_cards, self.user_points, None, None


    def ai_new_game(self) -> tuple[list, Literal[21], Literal['BLACKJACK'], Literal['PUSH']] | tuple[list, int, None, None]:
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

        
        if ai_card_value1 in self.points_dictionary:
            if ai_card_value1 == "ace":
                self.computer_hidden_point += 10
                self.computer_hidden_point += self.points_dictionary[ai_card_value1]
            else:
                self.computer_hidden_point += self.points_dictionary[ai_card_value1]

    
        if ai_card_value2 in self.points_dictionary:
            if ai_card_value1 == "ace" and ai_card_value2 in ("ten", "jack", "queen", "king"):
                self.computer_points += self.computer_hidden_point
                self.computer_points += self.points_dictionary[ai_card_value2]
                if self.computer_points == 21 == self.user_points:
                    self.budget += self.bet_amount
                    self.winnings -= self.bet_amount
                    self.winnings_tracker()
                    return self.computer_card, self.computer_points, "BLACKJACK", 'PUSH'
                else:
                    self.bet_amount = 0
                    self.winnings_tracker()
                    return self.computer_card, self.computer_points, "BLACKJACK", None
            # This makes sure the score does not give away the hidden card by making a visible ace equal 1.
            elif ai_card_value1 == "ace" and ai_card_value2 == "ace":
                self.computer_hidden_point -= 10
                self.computer_points += 10
                self.computer_points += self.points_dictionary[ai_card_value2]
                return self.computer_card, self.computer_points, None, None
            elif self.computer_hidden_point == 10 and ai_card_value2 == "ace":
                self.computer_points += 10
                self.computer_points += self.points_dictionary[ai_card_value2]
                self.bet_amount = 0
                self.winnings_tracker()
                return self.computer_card, self.computer_points, "BLACKJACK", None
            elif ai_card_value2 == "ace" and ai_card_value1 != "ace":
                self.computer_points += 10
                self.computer_points += self.points_dictionary[ai_card_value2]
                return self.computer_card, self.computer_points, None, None
            else:
                self.computer_points += self.points_dictionary[ai_card_value2]

        return self.computer_card, self.computer_points, None, None

    def check_deck(self) -> dict[str, int]:
        card_count = (
            len(self.heart_ranks)
            + len(self.diamond_ranks)
            + len(self.spade_ranks)
            + len(self.club_ranks)
        )
        return {"card_count": card_count}

    def reset_game(self) -> None:
        self.user_cards = []
        self.computer_card = []
        self.user_points = 0
        self.computer_points = 0
        self.computer_hidden_point = 0
        self.user_ace_adjusted = False
        self.computer_ace_adjusted = False
        self.winnings = 0 # Reset winnings at the start of a new game for now, but this may be used in future iterations to track winnings across multiple games
        self.bet_amount = 0 # Reset bet amount at the start of a new game
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

    def bet(self, amount: int) -> bool:
        if self.budget > 0:    
            self.budget -= amount
            self.bet_amount += amount
            return self.budget, self.bet_amount, None, self.winnings
        else:
            return self.budget, self.bet_amount, "Insufficient funds!"
    
    def reset_bet(self) -> int:
        self.budget = 1000
        self.bet_amount = 0
        return self.budget, self.bet_amount
    
    def winnings_tracker(self) -> tuple[int, int, int]:
        return self.budget, self.bet_amount, self.winnings
            

    def user_turn(self) -> tuple[tuple[str, str], int] | tuple[tuple[str, str], int, tuple[str, str], int, Literal['DEALER WINS!']]:
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
        new_card_pts_key = user_cards[-1][1]

        if new_card_pts_key in self.points_dictionary:
            self.user_points += self.points_dictionary[new_card_pts_key]
            #check that the user doesn't have an ace first. Note that this does permanently alter self.user_cards.
            user_has_ace = any(rank == "ace" for suit, rank in self.user_cards[:-1])
            if new_card_pts_key == "ace" and not user_has_ace:
                if self.user_points < 21 and (self.user_points + 10) <= 21:
                    self.user_points += 10
                elif self.user_points < 21 and (self.user_points +10) > 21:
                    self.user_ace_adjusted = True
            elif self.user_points > 21 and user_has_ace and not self.user_ace_adjusted:
                self.user_points -= 10
                # Only adjust an ace from 11->1 once per user turn
                self.user_ace_adjusted = True
            elif self.user_points > 21:
                bust = True
                computer_points = self.computer_points + self.computer_hidden_point
                self.bet_amount = 0
                self.winnings_tracker()
                return new_card, self.user_points, self.computer_card, computer_points, "DEALER WINS!"

        return new_card, self.user_points
    

    def ai_turn(self) -> tuple[list[tuple[str, str]], int, Literal['PUSH']] | tuple[list[tuple[str, str]], int, Literal['DEALER WINS!']]:
        computer_points = self.computer_points + self.computer_hidden_point
        ai_bust = computer_points > 21
        if computer_points >= 17 and computer_points == self.user_points:
                    ai_bust = True
                    self.budget += self.bet_amount
                    self.bet_amount = 0
                    self.winnings_tracker()
                    return self.computer_card, computer_points, "PUSH"
        elif computer_points <= 21 and computer_points > self.user_points:
                    ai_bust = True
                    self.bet_amount = 0
                    self.winnings_tracker()
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
                else:
                    break
                
                self.computer_card.append((card_suit, rank))
                ai_card_value = rank
                result = ""
                
                if ai_card_value in self.points_dictionary:
                    computer_points += self.points_dictionary[ai_card_value]
                    ai_has_ace = any(rank == "ace" for suit, rank in self.computer_card[:-1])
                    
                    if ai_card_value == "ace" and not ai_has_ace:
                        if computer_points < 21 and (computer_points + 10) <= 21:
                            computer_points += 10
                            if computer_points > self.user_points:
                                ai_bust = True
                                self.bet_amount = 0
                                self.winnings_tracker()
                                result = "DEALER WINS!"
                            elif computer_points == self.user_points:
                                ai_bust = True
                                self.budget += self.bet_amount
                                self.bet_amount = 0
                                self.winnings_tracker()
                                result = "PUSH"
                            else:
                                continue
                        elif computer_points > 21:
                            ai_bust = True
                            self.winnings += self.bet_amount
                            self.bet_amount = 0
                            self.winnings_tracker()
                            result = "YOU WIN!"
                            continue
                        elif computer_points < 21 and (computer_points + 10) > 21:
                            self.computer_ace_adjusted = True
                            continue
                    elif ai_card_value == "ace" and ai_has_ace:
                        if computer_points > self.user_points and computer_points <= 21:
                            ai_bust = True
                            self.bet_amount = 0
                            self.winnings_tracker()
                            result = "DEALER WINS!"
                        elif computer_points == self.user_points:
                            ai_bust = True
                            self.budget += self.bet_amount
                            self.bet_amount = 0
                            self.winnings_tracker()
                            result = "PUSH"
                        if computer_points < 21 and computer_points < self.user_points:
                            continue
                        elif computer_points > 21 and (ai_has_ace and not self.computer_ace_adjusted):
                            computer_points -= 10
                            # Only adjust an ace from 11->1 once per user turn
                            self.computer_ace_adjusted = True
                            continue
                    elif computer_points >= 17 and computer_points == self.user_points:
                        ai_bust = True
                        self.budget += self.bet_amount
                        self.bet_amount = 0
                        self.winnings_tracker()
                        result = "PUSH"
                    elif computer_points <= 21 and computer_points > self.user_points:
                        ai_bust = True
                        self.bet_amount = 0
                        self.winnings_tracker()
                        result = "DEALER WINS!"
                    elif computer_points > 21 and (ai_has_ace and not self.computer_ace_adjusted):
                        computer_points -= 10
                        # Only adjust an ace from 11->1 once per user turn
                        self.computer_ace_adjusted = True
                        if computer_points > self.user_points:
                            ai_bust = True
                            self.bet_amount = 0
                            self.winnings_tracker()
                            result = "DEALER WINS!"
                        elif computer_points == self.user_points:
                            ai_bust = True
                            self.budget += self.bet_amount
                            self.bet_amount = 0
                            self.winnings_tracker()
                            result = "PUSH"
                        else:
                            continue
                    elif computer_points > 21 or (computer_points > 21 and self.computer_ace_adjusted):
                        ai_bust = True
                        self.winnings += self.bet_amount
                        self.bet_amount = 0
                        self.winnings_tracker()
                        result = "YOU WIN!"
                    else:
                        continue

            return self.computer_card, computer_points, result

 