from fastapi import FastAPI
from blackjack_engine import GameEngine

app = FastAPI()

game = GameEngine()

@app.get("/one-deck-game")
def get_cards():
    return {"first_deal": game.new_game_state()}