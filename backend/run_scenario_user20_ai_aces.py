from blackjack_engine import GameEngine
from unittest.mock import patch


def run_scenario():
    game = GameEngine()
    game.reset_game()

    # Set player's total to 20 (two initial cards of 10 each)
    game.user_points = 20

    # Give AI two small starting cards (so it must draw)
    game.computer_card = [("clubs", "two"), ("diamonds", "three")]
    game.computer_points = game.points_dictionary["two"]
    game.computer_hidden_point = game.points_dictionary["three"]

    # Make hearts contain many aces so AI draws aces first
    game.heart_ranks = ["ace", "ace", "ace", "ace", "ace"]
    game.diamond_ranks = []
    game.spade_ranks = []
    game.club_ranks = []

    def choice_mock(seq):
        # When selecting a suit, always pick hearts so we draw from heart_ranks
        if seq == game.suits:
            return "hearts"
        # When selecting a rank from a suit list, return the first available rank
        return seq[0] if seq else None

    with patch('blackjack_engine.random.choice', side_effect=choice_mock):
        cards, points, message = game.ai_turn()

    print("AI final cards:", cards)
    print("AI final points:", points)
    print("AI message:", message)


if __name__ == '__main__':
    run_scenario()
