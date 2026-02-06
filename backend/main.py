from fastapi import FastAPI
from blackjack_engine import GameEngine

app = FastAPI()

game = GameEngine()

@app.get("/new-game")
def get_cards():
    return {
        "first_deal": game.new_game_state(),
        "first_deal_ai": game.ai_new_game(),
        "cards_remaining": game.check_deck()
        }