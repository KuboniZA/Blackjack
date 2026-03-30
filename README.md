🃏 Blackjack Web App

A full-stack Blackjack game built with Vue 3 (TypeScript) on the frontend and FastAPI (Python) on the backend. This project recreates a casino-style Blackjack experience with smooth animations, betting mechanics, and interactive gameplay.

Project Overview
This application allows users to:
* Play Blackjack against an AI dealer
* Place bets using a virtual bankroll
* Experience animated card dealing and chip placement
* Track points, bets, and remaining cards in real time

The project is designed with a modular frontend and a clean API-driven backend, making it scalable for future features like multiplayer and additional game modes.

Tech Stack

Frontend:

Vue 3 (<script setup> + Composition API)
TypeScript
Component-based architecture
Custom CSS animations

Backend:

FastAPI
Python game engine (custom Blackjack logic)
RESTful API endpoints

Features:
* Single-deck Blackjack gameplay
* Betting system with chip selection
* AI dealer logic (hit/stand rules implemented)
* Background music with mute toggle
* Keyboard controls:
* Space → Hit
* Enter → Stand
* Esc → Reset round
* Animated UI (cards, chips, transitions)
  
Installation & Setup
1. Clone the repo
  * git clone https://github.com/your-username/blackjack-app.git
  * cd blackjack-app
    
2. Backend (FastAPI)
  * cd backend
  * pip install -r requirements.txt
  * uvicorn main:app --reload
    
3. Frontend (Vue)
  * cd frontend
  * npm install
  * npm run dev


Game Logic Highlights:
* Dynamic Ace handling (1 or 11 depending on context)
* Dealer follows standard Blackjack rules (hits until ≥17)
* Deck tracking ensures no duplicate cards
* Betting system updates bankroll and payouts

Current Status (March 2026)
The project is in its final development stages. Current work includes:
* Finalising and polishing CSS and UI responsiveness
* Fixing edge-case bugs and improving stability
* Correcting and refining winnings logic to properly update the player's bank balance
* Adding a second deck game mode
* Exploring WebSocket integration for real-time multiplayer gameplay
* General performance improvements and minor fixes

Planned Features
1. Multiplayer Blackjack (WebSockets)
2. Multiple deck options
3. Persistent player stats
4. Advanced betting options (double down, split, etc.)
5. Improved audio controls and sound effects

Screenshots:

 <img width="1920" height="1080" alt="HigRollers" src="https://github.com/user-attachments/assets/9d57d187-1970-437c-be8f-f35ca711c70e" />

 <img width="1920" height="1080" alt="Screenshot 2026-03-09 at 18 12 23 (2)" src="https://github.com/user-attachments/assets/e5ad7515-ee7a-45d0-b29c-7893bcb577d7" />

Contributing:
This project is currently in active development, but contributions, suggestions, and feedback are welcome.

License: MIT License

Author: Sipumzo Trueman Lucwaba

Developed as part of my personal full-stack project (2026).

Final Notes:
This project focuses on combining:
* Clean frontend architecture
* Stateful backend game logic
* Smooth user experience

More updates coming soon...
