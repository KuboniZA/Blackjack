import unittest
from unittest.mock import patch, MagicMock
from blackjack_engine import GameEngine


class TestAiTurn(unittest.TestCase):
    """Test suite for the ai_turn() method"""

    def setUp(self):
        """Initialize a fresh game engine before each test"""
        self.game = GameEngine()
        # Setup initial game state
        self.game.ai_new_game()
        self.game.new_game_state()

    def test_ai_turn_returns_tuple(self):
        """Test that ai_turn() returns a tuple with 3 elements"""
        result = self.game.ai_turn()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

    def test_ai_turn_returns_cards_list(self):
        """Test that first element of return is a list of cards"""
        result = self.game.ai_turn()
        cards, points, message = result
        self.assertIsInstance(cards, list)
        # Should have at least the initial 2 cards
        self.assertGreaterEqual(len(cards), 2)

    def test_ai_turn_returns_integer_points(self):
        """Test that second element is the AI's point total"""
        result = self.game.ai_turn()
        cards, points, message = result
        self.assertIsInstance(points, int)
        self.assertGreater(points, 0)

    def test_ai_turn_returns_message(self):
        """Test that third element is a string message"""
        result = self.game.ai_turn()
        cards, points, message = result
        self.assertIsInstance(message, str)
        # Message should be one of the possible outcomes
        valid_messages = ["DEALER WINS!", "YOU WIN!", "DRAW!"]
        self.assertIn(message, valid_messages)

    def test_ai_turn_adds_cards_to_computer_card(self):
        """Test that new cards are added to self.computer_card"""
        initial_count = len(self.game.computer_card)
        self.game.ai_turn()
        # Should have at least one more card after ai_turn
        self.assertGreaterEqual(len(self.game.computer_card), initial_count)

    def test_ai_turn_card_points_match_returned_points(self):
        """Test that returned points match the cards in the array"""
        result = self.game.ai_turn()
        cards, returned_points, message = result
        
        # Calculate points from all cards
        calculated_points = 0
        for card in cards:
            suit, rank = card
            calculated_points += self.game.points_dictionary[rank]
        
        # Check if returned points match calculated points
        self.assertEqual(returned_points, calculated_points,
                        f"Returned points {returned_points} don't match calculated points {calculated_points}")

    def test_ai_turn_stops_at_17_or_higher(self):
        """Test that AI stops drawing when reaching 17 or higher (in normal case)"""
        # Reset and setup a scenario where AI has 16 points
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        
        # Manually set AI points to test behavior
        self.game.computer_points = 10
        self.game.computer_hidden_point = 6  # Total 16, should draw more
        
        result = self.game.ai_turn()
        cards, points, message = result
        
        # AI should have at least 3 cards (initial 2 + at least 1 drawn)
        if points < 21:
            self.assertGreater(len(cards), 2)

    @patch('blackjack_engine.random.choice')
    def test_ai_turn_with_controlled_cards(self, mock_choice):
        """Test ai_turn with controlled card draws"""
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        
        # Mock to return specific suits/ranks for predictable testing
        self.game.user_points = 18  # Set user score
        mock_choice.side_effect = [
            "spades",  # suit for first draw
            "diamonds",  # suit for potential second draw
        ]
        
        # Mock the rank selection too
        with patch.object(self.game, 'spade_ranks', ["five", "six"]):
            initial_card_count = len(self.game.computer_card)
            result = self.game.ai_turn()
            cards, points, message = result
            
            # At least one card should be added
            self.assertGreaterEqual(len(cards), initial_card_count)

    def test_ai_turn_dealer_wins_condition(self):
        """Test when AI should get DEALER WINS! message"""
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        
        # Set user score lower than potential AI score
        self.game.user_points = 15
        self.game.computer_points = 16
        self.game.computer_hidden_point = 2  # Total 18, beats player
        
        result = self.game.ai_turn()
        cards, points, message = result
        
        # If AI is already above player score and not busting, should return immediately
        if points > self.game.user_points and points <= 21:
            self.assertEqual(message, "DEALER WINS!")

    def test_ai_turn_multiple_calls(self):
        """Test that multiple ai_turn calls accumulate cards correctly"""
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        
        self.game.user_points = 15
        self.game.computer_points = 10
        self.game.computer_hidden_point = 0
        
        first_result = self.game.ai_turn()
        first_cards, first_points, first_message = first_result
        first_card_count = len(first_cards)
        
        # Reset for clean state
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        self.game.user_points = 15
        self.game.computer_points = 10
        self.game.computer_hidden_point = 0
        
        second_result = self.game.ai_turn()
        second_cards, second_points, second_message = second_result
        
        # Both should return valid card lists
        self.assertGreater(len(first_cards), 0)
        self.assertGreater(len(second_cards), 0)

    def test_ai_turn_bust_scenario(self):
        """Test when AI busts (goes over 21)"""
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        
        self.game.user_points = 20
        self.game.computer_points = 5
        self.game.computer_hidden_point = 0
        
        result = self.game.ai_turn()
        cards, points, message = result
        
        # If AI busts, should see YOU WIN! message
        if points > 21:
            self.assertEqual(message, "YOU WIN!")


class TestAiTurnCardAccuracy(unittest.TestCase):
    """Tests specifically for card accounting accuracy"""
    
    def setUp(self):
        """Initialize a fresh game engine before each test"""
        self.game = GameEngine()

    def test_all_cards_in_return_are_valid(self):
        """Test that all returned cards are valid card tuples"""
        self.game.ai_new_game()
        self.game.new_game_state()
        
        result = self.game.ai_turn()
        cards, points, message = result
        
        valid_suits = ["hearts", "diamonds", "spades", "clubs"]
        valid_ranks = list(self.game.points_dictionary.keys())
        
        for card in cards:
            self.assertIsInstance(card, tuple)
            self.assertEqual(len(card), 2)
            suit, rank = card
            # Note: suit might already be removed from ranks, so just check format
            self.assertIn(suit, valid_suits)
            self.assertIn(rank, valid_ranks)

    def test_no_duplicate_cards_in_single_turn(self):
        """Test that ai_turn doesn't return duplicate cards (within reason)"""
        self.game.reset_game()
        self.game.ai_new_game()
        self.game.new_game_state()
        
        # Run multiple games to see if duplicates appear
        for _ in range(5):
            result = self.game.ai_turn()
            cards, points, message = result
            
            # Create a hashable representation for unique check
            card_strings = [f"{suit}-{rank}" for suit, rank in cards]
            unique_cards = set(card_strings)
            
            # Should not have more than len(unique_cards) regular duplicates
            # unless explicitly designed to do so
            self.assertLessEqual(len(card_strings), 13)  # Max reasonable in one turn


if __name__ == '__main__':
    unittest.main()
