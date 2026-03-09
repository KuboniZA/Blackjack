from blackjack_engine import GameEngine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
        "cards_remaining": game.check_deck(),
        "bet_reset": game.reset_bet(),
        "get_points": game.get_points(),
    }

@app.get("/deal-cards")
def get_cards():
    return {
        "first_deal_ai": game.ai_new_game(),
        "first_deal": game.new_game_state(),
        "cards_remaining": game.check_deck(),
        "winnings": game.winnings_tracker(),
        "bet_reset": game.reset_bet(),
    }


@app.post("/reset-game")
def reset_game():
    return {
        "reset-cards": game.reset_game(),
        # "first_deal_ai": game.ai_new_game(),
        # "first_deal": game.new_game_state(),
        "cards_remaining": game.check_deck(),
        "new_round": game.reset_round(),
        # "winnings": game.winnings_tracker(),
    }

@app.post("/reset-round")
def round_reset():
    return {
        "new_round": game.reset_round(),
        "cards_remaining": game.check_deck(),
    }

@app.post("/hit")
def get_new_card():
    return {
        "card": game.user_turn(),
        "cards_remaining": game.check_deck(),
        "winnings": game.winnings_tracker(),
    }

@app.post("/stand")
def ai_plays():
    return {
        "ai_cards": game.ai_turn(),
        "cards_remaining": game.check_deck(),
        "winnings": game.winnings_tracker(),
    }

class bet_amount(BaseModel):
    amount: int

@app.post("/place-bet")
def place_bet(req: bet_amount):
    return {
        "bet_placed": game.bet(req.amount),
        "cards_remaining": game.check_deck(),
    }

# @app.post("/check-winner")
# def check_winner():
#     return {
#         "winner": game.check_winner(),
#         "cards_remaining": game.check_deck(),
#     }

# @app.post("/surrender")
# def surrender():
#     return {
#         "surrendered": game.surrender(),
#         "cards_remaining": game.check_deck(),
#     }

# @app.post("/split")
# def split_hand():
#     return {
#         "split_hand": game.split_hand(),
#         "cards_remaining": game.check_deck(),
#     }

# @app.post("/double-down")
# def double_down():
#     return {
#         "doubled": game.double_down(),
#         "cards_remaining": game.check_deck(),
#     }

# @app.post("/play-again")
# def play_again():
#     return {
#         "reset": game.play_again(),
#         "cards_remaining": game.check_deck(),
#     }