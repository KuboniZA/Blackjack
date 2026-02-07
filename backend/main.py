from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from blackjack_engine import GameEngine

app = FastAPI()

game = GameEngine()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/new-game")
def get_cards():
    return {
        "first_deal": game.new_game_state(),
        "first_deal_ai": game.ai_new_game(),
        "cards_remaining": game.check_deck()
        }

@app.get('/reset-game')
def reset_game():
    return {
        "reset-cards": game.reset_game(),
        "first_deal": game.new_game_state(),
        "first_deal_ai": game.ai_new_game(),
        "cards_remaining": game.check_deck()
    }