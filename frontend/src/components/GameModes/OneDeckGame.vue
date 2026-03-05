<script lang="ts" setup>
import { ref, onMounted, onUnmounted, nextTick } from "vue";
import type { Component } from "vue";
import AceOfClubs from "../Deck1/Clubs/AceOfClubs.vue";
import AceOfDiamonds from "../Deck1/Diamonds/AceOfDiamonds.vue";
import AceOfHearts from "../Deck1/Hearts/AceOfHearts.vue";
import AceOfSpades from "../Deck1/Spades/AceOfSpades.vue";
import TwoOfClubs from "../Deck1/Clubs/TwoOfClubs.vue";
import TwoOfHearts from "../Deck1/Hearts/TwoOfHearts.vue";
import TwoOfSpades from "../Deck1/Spades/TwoOfSpades.vue";
import TwoOfDiamonds from "../Deck1/Diamonds/TwoOfDiamonds.vue";
import ThreeOfClubs from "../Deck1/Clubs/ThreeOfClubs.vue";
import ThreeOfDiamonds from "../Deck1/Diamonds/ThreeOfDiamonds.vue";
import ThreeOfHearts from "../Deck1/Hearts/ThreeOfHearts.vue";
import ThreeOfSpades from "../Deck1/Spades/ThreeOfSpades.vue";
import FourOfClubs from "../Deck1/Clubs/FourOfClubs.vue";
import FourOfDiamonds from "../Deck1/Diamonds/FourOfDiamonds.vue";
import FourOfHearts from "../Deck1/Hearts/FourOfHearts.vue";
import FourOfSpades from "../Deck1/Spades/FourOfSpades.vue";
import FiveOfClubs from "../Deck1/Clubs/FiveOfClubs.vue";
import FiveOfDiamonds from "../Deck1/Diamonds/FiveOfDiamonds.vue";
import FiveOfHearts from "../Deck1/Hearts/FiveOfHearts.vue";
import FiveOfSpades from "../Deck1/Spades/FiveOfSpades.vue";
import SixOfClubs from "../Deck1/Clubs/SixOfClubs.vue";
import SixOfDiamonds from "../Deck1/Diamonds/SixOfDiamonds.vue";
import SixOfHearts from "../Deck1/Hearts/SixOfHearts.vue";
import SixOfSpades from "../Deck1/Spades/SixOfSpades.vue";
import SevenOfClubs from "../Deck1/Clubs/SevenOfClubs.vue";
import SevenOfDiamonds from "../Deck1/Diamonds/SevenOfDiamonds.vue";
import SevenOfHearts from "../Deck1/Hearts/SevenOfHearts.vue";
import SevenOfSpades from "../Deck1/Spades/SevenOfSpades.vue";
import EightOfClubs from "../Deck1/Clubs/EightOfClubs.vue";
import EightOfDiamonds from "../Deck1/Diamonds/EightOfDiamonds.vue";
import EightOfHearts from "../Deck1/Hearts/EightOfHearts.vue";
import EightOfSpades from "../Deck1/Spades/EightOfSpades.vue";
import NineOfClubs from "../Deck1/Clubs/NineOfClubs.vue";
import NineOfDiamonds from "../Deck1/Diamonds/NineOfDiamonds.vue";
import NineOfHearts from "../Deck1/Hearts/NineOfHearts.vue";
import NineOfSpades from "../Deck1/Spades/NineOfSpades.vue";
import TenOfClubs from "../Deck1/Clubs/TenOfClubs.vue";
import TenOfDiamonds from "../Deck1/Diamonds/TenOfDiamonds.vue";
import TenOfHearts from "../Deck1/Hearts/TenOfHearts.vue";
import TenOfSpades from "../Deck1/Spades/TenOfSpades.vue";
import JackOfClubs from "../Deck1/Clubs/JackOfClubs.vue";
import JackOfDiamonds from "../Deck1/Diamonds/JackOfDiamonds.vue";
import JackOfHearts from "../Deck1/Hearts/JackOfHearts.vue";
import JackOfSpades from "../Deck1/Spades/JackOfSpades.vue";
import QueenOfClubs from "../Deck1/Clubs/QueenOfClubs.vue";
import QueenOfDiamonds from "../Deck1/Diamonds/QueenOfDiamonds.vue";
import QueenOfHearts from "../Deck1/Hearts/QueenOfHearts.vue";
import QueenOfSpades from "../Deck1/Spades/QueenOfSpades.vue";
import KingOfClubs from "../Deck1/Clubs/KingOfClubs.vue";
import KingOfDiamonds from "../Deck1/Diamonds/KingOfDiamonds.vue";
import KingOfHearts from "../Deck1/Hearts/KingOfHearts.vue";
import KingOfSpades from "../Deck1/Spades/KingOfSpades.vue";
import HiddenCard from "../Deck1/HiddenCard.vue";
import ChipsView from "../ChipsView.vue";

const cards_left = ref<number>(0);
const player_card1 = ref<[string, string]>();
const player_card2 = ref<[string, string]>();
const blackjack = ref<string | null>(null);
const is_player_turn = ref<boolean>(false);
const blackjack_ai_pts = ref<number | null>(null);

const ai_card1 = ref<[string, string]>();
const ai_card2 = ref<[string, string]>();
const player_points = ref<number>(0);
const ai_points = ref<number>(0);
const player_turn_ai_points = ref<number | null>(null);
const ai_blackjack = ref<string | null>(null);
const is_ai_turn = ref<boolean>(false);

const winner = ref<string | null>(null);
const ai_turn_winner = ref<string | null>(null);
const double_black_jack = ref<string | null>(null);

const hasDealt = ref<boolean>(false);

const new_user_card = ref<[string, string] | null>(null);
type PlayerCard = { id: number; card: [string, string]; revealed: boolean };
const playerCards = ref<Array<PlayerCard>>([]);

const cardComponentMap: Record<string, Component> = {
  "clubs-ace": AceOfClubs,
  "clubs-two": TwoOfClubs,
  "clubs-three": ThreeOfClubs,
  "clubs-four": FourOfClubs,
  "clubs-five": FiveOfClubs,
  "clubs-six": SixOfClubs,
  "clubs-seven": SevenOfClubs,
  "clubs-eight": EightOfClubs,
  "clubs-nine": NineOfClubs,
  "clubs-ten": TenOfClubs,
  "clubs-jack": JackOfClubs,
  "clubs-queen": QueenOfClubs,
  "clubs-king": KingOfClubs,

  "spades-ace": AceOfSpades,
  "spades-two": TwoOfSpades,
  "spades-three": ThreeOfSpades,
  "spades-four": FourOfSpades,
  "spades-five": FiveOfSpades,
  "spades-six": SixOfSpades,
  "spades-seven": SevenOfSpades,
  "spades-eight": EightOfSpades,
  "spades-nine": NineOfSpades,
  "spades-ten": TenOfSpades,
  "spades-jack": JackOfSpades,
  "spades-queen": QueenOfSpades,
  "spades-king": KingOfSpades,

  "hearts-ace": AceOfHearts,
  "hearts-two": TwoOfHearts,
  "hearts-three": ThreeOfHearts,
  "hearts-four": FourOfHearts,
  "hearts-five": FiveOfHearts,
  "hearts-six": SixOfHearts,
  "hearts-seven": SevenOfHearts,
  "hearts-eight": EightOfHearts,
  "hearts-nine": NineOfHearts,
  "hearts-ten": TenOfHearts,
  "hearts-jack": JackOfHearts,
  "hearts-queen": QueenOfHearts,
  "hearts-king": KingOfHearts,

  "diamonds-ace": AceOfDiamonds,
  "diamonds-two": TwoOfDiamonds,
  "diamonds-three": ThreeOfDiamonds,
  "diamonds-four": FourOfDiamonds,
  "diamonds-five": FiveOfDiamonds,
  "diamonds-six": SixOfDiamonds,
  "diamonds-seven": SevenOfDiamonds,
  "diamonds-eight": EightOfDiamonds,
  "diamonds-nine": NineOfDiamonds,
  "diamonds-ten": TenOfDiamonds,
  "diamonds-jack": JackOfDiamonds,
  "diamonds-queen": QueenOfDiamonds,
  "diamonds-king": KingOfDiamonds,
};

const new_ai_cards = ref<[string, string] | null>(null);

type ComputerCard = { id: number; card: [string, string]; revealed: boolean };
const computerCards = ref<Array<ComputerCard>>([]);

const getCardComponent = (card?: [string, string]) => {
  if (!card) return null;
  const [suit, rank] = card;
  const cardKey = cardComponentMap[`${suit}-${rank}`];
  return cardKey;
};

const newGame = async () => {
  const response = await fetch("http://127.0.0.1:8000/new-game");
  const data = await response.json();
  cards_left.value = data.cards_remaining.card_count;

  const [user_points, ai_points_value] = data.get_points;
  player_points.value = user_points;
  ai_points.value = ai_points_value;

  bet_amount.value = data.bet_reset[0];
  current_bet.value = data.bet_reset[1];

  hasDealt.value = false;
  betPlaced.value = false;
};

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
const showHiddenCard = ref<boolean>(false);

const showCards = async () => {
  const response = await fetch("http://127.0.0.1:8000/deal-cards");
  const data = await response.json();
  cards_left.value = data.cards_remaining.card_count;

  player_card1.value = data.first_deal[0][0];
  player_card2.value = data.first_deal[0][1];
  player_points.value = data.first_deal[1];
  blackjack.value = data.first_deal[2];
  blackjack_ai_pts.value = data.first_deal[3];

  ai_card1.value = data.first_deal_ai[0][0];
  ai_card2.value = data.first_deal_ai[0][1];
  ai_points.value = data.first_deal_ai[1];
  ai_blackjack.value = data.first_deal_ai[2];
  double_black_jack.value = data.first_deal_ai[3];

  showHiddenCard.value = true;
  hasDealt.value = true;

  await nextTick();

  for (const id of ["p-card1", "p-card2"]) {
    const cardElement = document.getElementById(id);
    const chipsElement = document.querySelector(".chips-background, .game-chips");
    const placeBetElement = document.querySelector(".place-bet-container");
    if (cardElement) {
      cardElement.classList.add("show");
      chipsElement?.classList.add("hide");
      placeBetElement?.classList.add("hidePBC");
    }
    await sleep(300);
  }

  for (const id of ["ai-hiddenCard", "ai-card2"]) {
    const aiCardElement = document.getElementById(id);
    if (aiCardElement) {
      aiCardElement.classList.add("showAiCards");
    }
    await sleep(300);
  }
};

const resetGame = async () => {
  const response = await fetch("http://127.0.0.1:8000/reset-game", { method: "POST" });
  const data = await response.json();
  cards_left.value = data.cards_remaining.card_count;

  // player_card1.value = data.first_deal[0][0];
  // player_card2.value = data.first_deal[0][1];
  player_points.value = data.first_deal[1];
  // blackjack.value = data.first_deal[2];
  // blackjack_ai_pts.value = data.first_deal[3];

  // ai_card1.value = data.first_deal_ai[0][0];
  // ai_card2.value = data.first_deal_ai[0][1];
  ai_points.value = data.first_deal_ai[1];
  // ai_blackjack.value = data.first_deal_ai[2];
  // double_black_jack.value = data.first_deal_ai[3];

  new_user_card.value = null;
  playerCards.value = [];
  new_ai_cards.value = null;
  computerCards.value = [];
  winner.value = null;
  ai_turn_winner.value = null;
  player_turn_ai_points.value = null;
  is_ai_turn.value = false;
  is_player_turn.value = false;

  bet_amount.value = data.bet_reset[0];
  current_bet.value = data.winnings[1];
  winnings.value = data.winnings[2];
  hasDealt.value = false;
};

const player_turn = async () => {
  const response = await fetch("http://127.0.0.1:8000/hit", { method: "POST" });
  const data = await response.json();
  cards_left.value = data.cards_remaining.card_count;
  is_player_turn.value = true;

  new_user_card.value = data.card[0];
  player_points.value = data.card[1];

  if (new_user_card.value != null) {
    const newId = playerCards.value.length + 1;
    playerCards.value.push({ id: newId, card: new_user_card.value, revealed: true });
  }
  player_turn_ai_points.value = data.card[3];
  winner.value = data.card[4];
  current_bet.value = data.winnings[1];
  winnings.value = data.winnings[2];
};

const ai_turn = async () => {
  const response = await fetch("http://127.0.0.1:8000/stand", { method: "POST" });
  const data = await response.json();
  is_ai_turn.value = true;
  cards_left.value = data.cards_remaining.card_count;
  new_ai_cards.value = data.ai_cards[0];
  const allAiCards = new_ai_cards.value;
  ai_points.value = data.ai_cards[1];
  showHiddenCard.value = false;

  await nextTick();

  for (const id of ["ai-card1"]) {
    const aiCardElement = document.getElementById(id);
    if (aiCardElement) {
      aiCardElement.classList.add("showAiCards");
    }
    await sleep(300);
  }

  if (allAiCards && allAiCards.length > 2) {
    for (let index = 2; index < allAiCards.length; index++) {
      const aiCardId = computerCards.value.length + 1;
      computerCards.value.push({ id: aiCardId, card: allAiCards[index], revealed: true });
    }
  }
  ai_turn_winner.value = data.ai_cards[2];
  current_bet.value = data.winnings[1];
  winnings.value = data.winnings[2];
};

// Betting logic for chips

const bet_amount = ref<number>(0);
const winnings = ref<number>(0);
const current_bet = ref<number>(0);
const insufficient_funds = ref<string | null>(null);
const betPlaced = ref<boolean>(false);

const placeBet = async (amount: number, chipId: string) => {
  const response = await fetch("http://127.0.0.1:8000/place-bet", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ amount }),
  });
  const data = await response.json();
  betPlaced.value = true;
  bet_amount.value = data.bet_placed[0];
  current_bet.value = data.bet_placed[1];
  insufficient_funds.value = data.bet_placed[2];
  addChips(chipId);
};

const addChips = (chipId: string) => {
  const chipElement = document.getElementById(chipId)?.querySelector(".chips");
  if (!chipElement) return;
  console.log(chipElement);

  const chip = chipElement.getBoundingClientRect();
  console.log(chip.top, chip.left);

  const clone = chipElement.cloneNode(true) as HTMLElement;
  document.body.appendChild(clone);
  // clone.style.all = "unset";
  clone.style.position = "fixed";
  clone.style.left = `${chip.left}px`;
  clone.style.top = `${chip.top}px`;
  clone.style.transition = "all 0.2s ease-in-out";
  clone.style.margin = "0";

  clone.getBoundingClientRect();

  const centerX = window.innerWidth / 2 - chip.width / 2;
  const centerY = window.innerHeight / 2 - chip.height / 2;

  clone.style.left = `${centerX}px`;
  clone.style.top = `${centerY}px`;
  clone.style.zIndex = "-1";
};

// Keyboard event handler for game controls

const handleKeyDown = (event: KeyboardEvent) => {
  if (event.code === "Space") {
    event.preventDefault();
    player_turn();
  } else if (event.code === "Enter") {
    event.preventDefault();
    ai_turn();
  } else if (event.code === "Escape") {
    event.preventDefault();
    resetGame();
  }
};

onMounted(() => {
  newGame();
  window.addEventListener("keydown", handleKeyDown);
});

onUnmounted(() => {
  window.removeEventListener("keydown", handleKeyDown);
});
</script>

<template>
  <div class="game-container">
    <div class="chips-background">
      <chips-view
        :rand1="bet_amount >= 1"
        id="chip1"
        class="game-chips"
        @click="placeBet(1, 'chip1')"
      />
      <chips-view
        :rand5="bet_amount >= 5"
        id="chip5"
        class="game-chips"
        @click="placeBet(5, 'chip5')"
      />
      <chips-view
        :rand10="bet_amount >= 10"
        id="chip10"
        class="game-chips"
        @click="placeBet(10, 'chip10')"
      />
      <chips-view
        :rand25="bet_amount >= 25"
        id="chip25"
        class="game-chips"
        @click="placeBet(25, 'chip25')"
      />
      <chips-view
        :rand50="bet_amount >= 50"
        id="chip50"
        class="game-chips"
        @click="placeBet(50, 'chip50')"
      />
      <chips-view
        :rand100="bet_amount >= 100"
        id="chip100"
        class="game-chips"
        @click="placeBet(100, 'chip100')"
      />
      <chips-view
        :rand500="bet_amount >= 500"
        id="chip500"
        class="game-chips"
        @click="placeBet(500, 'chip500')"
      />
      <chips-view
        :rand1k="bet_amount >= 1000"
        id="chip1k"
        class="game-chips"
        @click="placeBet(1000, 'chip1k')"
      />
    </div>

    <div class="main-container">
      <div v-if="hasDealt == true" class="cards-remaining-container">
        <p class="cards-remaining">
          <span class="remaining-text">Cards remaining: </span>
          <span class="cards-rem-number">{{ cards_left }}</span>
        </p>
        <button class="reset" @click="resetGame">Reset Game</button>
      </div>
      <div v-if="hasDealt == true" class="points-container">
        <p class="points-text player-pts">
          Player<span class="points-badge">{{ player_points }}</span>
        </p>
        <p v-if="ai_points && player_turn_ai_points == null" class="points-text">
          Dealer<span class="points-badge">{{ blackjack ? blackjack_ai_pts : ai_points }}</span>
        </p>
        <p v-if="player_turn_ai_points" class="points-text">
          Dealer<span class="points-badge">{{ player_turn_ai_points }}</span>
        </p>
      </div>

      <div v-if="hasDealt == true" @click="player_turn" class="hit-stand-container">
        <span class="add-card">🃏</span>
        <span>HIT</span>
      </div>
      <div v-if="hasDealt == true" @click="ai_turn" class="hit-stand-container stand">
        <span class="add-card">✋🏾</span>
        <span>STAND</span>
      </div>
      <div v-if="betPlaced == true" @click="showCards" class="place-bet-container">
        <span>PLACE BET</span>
      </div>

      <div class="cards-container">
        <span v-if="blackjack" class="blackjack">{{ blackjack }}</span>

        <component
          id="p-card1"
          class="player-cards cards"
          v-if="player_card1 && hasDealt == true"
          :is="getCardComponent(player_card1)"
          style="--index: 0"
        />
        <component
          id="p-card2"
          class="player-cards cards"
          v-if="player_card2 && hasDealt == true"
          :is="getCardComponent(player_card2)"
          style="--index: 1"
        />

        <component
          v-for="playerCard in playerCards"
          :key="playerCard.id"
          class="cards dynamic-player-card show"
          :is="getCardComponent(playerCard.card)"
          :style="{ '--index': playerCard.id + 1 }"
        />
        <div class="winner-container">
          <h1 class="winner" v-if="winner">{{ winner }}</h1>
          <h1 class="winner" v-if="ai_turn_winner">{{ ai_turn_winner }}</h1>
          <h1 class="winner" v-if="double_black_jack">{{ double_black_jack }}</h1>
          <h1 class="winner" v-if="insufficient_funds">{{ insufficient_funds }}</h1>
        </div>

        <span v-if="ai_blackjack" class="blackjack ai-blackjack">{{ ai_blackjack }}</span>

        <component
          id="ai-hiddenCard"
          class="ai-cards cards"
          v-if="
            (hasDealt == true && showHiddenCard == true) ||
            (is_ai_turn == false && ai_blackjack == null && player_points <= 21)
          "
          :is="HiddenCard"
          style="--index: 0"
        />
        <component
          id="ai-card1"
          class="ai-cards cards"
          v-if="
            (is_ai_turn && showHiddenCard == false) ||
            blackjack ||
            ai_blackjack ||
            (is_player_turn && player_points > 21)
          "
          :is="getCardComponent(ai_card1)"
          style="--index: 0"
        />
        <component
          id="ai-card2"
          class="ai-cards cards"
          v-if="ai_card2"
          :is="getCardComponent(ai_card2)"
          style="--index: 1"
        />
        <component
          v-for="computerCard in computerCards"
          :key="computerCard.id"
          class="cards dynamic-ai-card showAiCards"
          :is="getCardComponent(computerCard.card)"
          :style="{ '--index': computerCard.id + 1 }"
        />
      </div>
      <div class="bet-counter ammount">
        <p class="points-text budget">
          Bank<span class="bet-container">R {{ bet_amount }}</span>
        </p>
      </div>
      <div v-if="hasDealt == true" class="bet-counter winnings">
        <p class="points-text budget">
          Total Winnings<span class="bet-container">R {{ winnings }}</span>
        </p>
      </div>
      <div class="current-bet-container">
        <p class="points-text budget">
          Current bet:<span class="current-bet">R {{ current_bet }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.game-container {
  position: relative;
  width: 100dvw;
  height: 100dvh;
  overflow: hidden;
}
.cards-remaining {
  background: linear-gradient(to right, blue, red);
  font-size: 2rem;
  color: white;
  position: relative;
  justify-content: center;
  border-radius: 25px;
  height: 3.5rem;
  width: 20rem;
  z-index: -2;
  border: 2px solid white;
  margin: 0;
}
.cards-rem-number {
  background-color: transparent;
  background: linear-gradient(to bottom right, red, blue);
  border-radius: 50%;
  font-size: 1.5rem;
  height: 2.5rem;
  width: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  justify-self: right;
  left: 82%;
  top: 15%;
  grid-row: 1;
}
.cards-rem-number::after {
  content: "";
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  position: absolute;
  background-color: transparent;
  background: linear-gradient(to bottom right, white, grey);
  z-index: -1;
  grid-column: 2;
  grid-row: 1;
}
.reset {
  color: white;
  position: relative;
  z-index: 3;
  font-size: 1.5rem;
  background-color: transparent;
  background: linear-gradient(to right, blue, red);
  border-style: solid;
  border-width: 0px 2px 2px 2px;
  border-color: white;
  padding: 0.5rem;
  border-bottom-left-radius: 25px;
  border-bottom-right-radius: 25px;
  grid-column: 1 / -1;
  grid-row: 2;
  justify-self: center;
  margin-top: 0;
}
.cards-remaining-container {
  position: relative;
  /* border: 1px solid red; */
  height: fit-content;
  width: fit-content;
  display: grid;
  grid-template-columns: max-content max-content;
  grid-template-rows: auto auto;
  align-items: center;
  left: 80%;
  top: 5rem;
  z-index: 5;
}
.remaining-text {
  width: fit-content;
  height: fit-content;
  position: absolute;
  top: 15%;
  left: 5%;
}
.reset:hover {
  background: linear-gradient(to right, rgb(1, 1, 215), rgb(202, 1, 1));
  transform: scale(1.02);
  cursor: pointer;
}
.hit-stand-container {
  color: white;
  background-color: rgba(255, 255, 255, 0.542);
  font-size: 2rem;
  border: 2px solid white;
  width: fit-content;
  padding: 1rem 2rem 1rem 2rem;
  border-radius: 25px;
  position: relative;
  top: 30rem;
  left: 10%;
  backdrop-filter: blur(5px);
}
.add-card {
  border: 1px solid white;
  padding: 0.75rem;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.455);
  margin-right: 1rem;
  position: relative;
  /* justify-items: center;
  align-items: center; */
}
.stand {
  top: 25rem;
  left: 75%;
  z-index: 25;
}
.hit-stand-container:hover {
  cursor: pointer;
  transform: scale(1.02);
  background-color: rgba(128, 128, 128, 0.492);
}
.main-container {
  position: relative;
  width: 100dvw;
  height: 100dvh;
}
.card-components {
  position: absolute;
}
.hit-stand-container:active {
  cursor: pointer;
  transform: scale(1.02);
  background-color: rgba(255, 255, 255, 0.627);
}
.cards-container {
  position: absolute;
  color: white;
  width: 54rem;
  height: 60rem;
  left: 35%;
  top: 0;
}
.player-cards {
  position: absolute;
  top: -16rem;
  height: fit-content;
  width: fit-content;
  display: none;
}
.player-cards.show,
.dynamic-player-card.show {
  display: flex;
  animation: show 0.2s linear forwards;
}
.dynamic-player-card {
  position: absolute;
  top: -16rem;
  height: fit-content;
  width: fit-content;
  display: none;
}
@keyframes show {
  0% {
    opacity: 0;
    top: 0%;
    transform: rotate(-180deg) scale(0.8);
  }
  100% {
    opacity: 1;
    top: 60%;
    transform: rotate(calc(-2deg + var(--index) * 3deg)) scale(0.8);
    left: calc(5% + var(--index) * 4%);
  }
}
@keyframes showAiCards {
  0% {
    opacity: 0;
    top: 0%;
    transform: rotate(-180deg) scale(0.8);
  }
  100% {
    opacity: 1;
    top: 2%;
    transform: rotate(calc(-2deg + var(--index) * 3deg)) scale(0.8);
    left: calc(5% + var(--index) * 4%);
  }
}
.ai-cards {
  position: absolute;
  height: fit-content;
  width: fit-content;
  top: -40rem;
  display: none;
}
.dynamic-ai-card {
  position: absolute;
  top: -16rem;
  height: fit-content;
  width: fit-content;
  display: none;
}
.ai-cards.showAiCards,
.dynamic-ai-card.showAiCards {
  display: flex;
  animation: showAiCards 0.2s linear forwards;
}

/* #p-card3 {
  top: 60%;
  left: 20%;
  transform: scale(0.7) rotate(-2deg);
} */
.points-container {
  color: white;
  position: absolute;
  height: fit-content;
  width: fit-content;
  left: 60%;
  top: 10%;
  display: grid;
  grid-template-rows: 1fr 1fr;
}
.points-text {
  font-size: 1.75rem;
  position: relative;
  border: 2px solid white;
  padding: 0.75rem;
  border-radius: 15px;
  height: fit-content;
  display: grid;
  grid-template-columns: 3fr 1fr;
  align-items: center;
  margin: 0;
  background: linear-gradient(to bottom right, blue, red);
  z-index: -2;
}
.points-badge {
  background-color: transparent;
  background: linear-gradient(to bottom right, red, blue);
  border-radius: 50%;
  font-size: 1.5rem;
  height: 2.5rem;
  width: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin: 0;
}
.points-badge::after {
  content: "";
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  position: absolute;
  background-color: transparent;
  background: linear-gradient(to bottom right, white, grey);
  z-index: -1;
  grid-column: 2;
  grid-row: 1;
}
.player-pts {
  top: 38rem;
}
.blackjack {
  color: white;
  font-size: 2rem;
  position: absolute;
  width: 25rem;
  top: 75%;
  left: 50%;
  transform: translateX(-50%);
  border: 2px solid white;
  border-radius: 15px;
  background: linear-gradient(to bottom right, blue, red);
  padding: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  justify-self: center;
  z-index: 20;
  transition: all 2s ease-in;
}
.ai-blackjack {
  top: 15%;
}
.winner-container {
  height: 100dvh;
  width: 100dvw;
  position: fixed;
  left: 0;
  top: 0;
}
.winner {
  font-size: 3rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  width: 36rem;
  height: fit-content;
  padding: 1rem;
  border: 2px solid white;
  border-radius: 15px;
  background: linear-gradient(to bottom right, rgba(0, 0, 255, 0.789), rgba(255, 0, 0, 0.728));
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}
.game-chips {
  position: relative;
  width: fit-content;
  height: fit-content;
  z-index: 5;
}
.hide {
  animation: hideChips 0.25s ease-in-out forwards;
}
@keyframes hideChips {
  0% {
    opacity: 1;
    top: 50%;
  }
  100% {
    opacity: 0;
    top: 5%;
  }
}
.chips-background {
  position: absolute;
  border: 2px solid white;
  background: linear-gradient(to bottom right, rgba(0, 0, 255, 0.53), rgba(255, 0, 0, 0.5));
  backdrop-filter: blur(4px);
  border-radius: 25px;
  width: 47rem;
  height: 28rem;
  top: 50%;
  transform: translateY(-50%);
  z-index: 5;
}
.bet-counter {
  position: absolute;
  top: 80%;
  left: 10%;
  color: white;
  min-width: 5rem;
}
.bet-container {
  background-color: transparent;
  background: linear-gradient(to bottom right, red, blue);
  border-radius: 15px;
  font-size: 1.5rem;
  height: 2.5rem;
  width: fit-content;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  padding: 0.35rem;
  left: -5%;
  white-space: nowrap;
}
.bet-container::after {
  content: "";
  width: 100%;
  height: 100%;
  border-radius: 15px;
  position: absolute;
  background-color: transparent;
  background: linear-gradient(to bottom right, white, grey);
  z-index: -1;
  grid-column: 2;
  grid-row: 1;
  transform: scale(1.075);
}
.current-bet-container {
  position: absolute;
  top: 80%;
  left: 68.25%;
  transform: translateX(-50%);
  width: 20rem;
  color: white;
}
.winnings {
  top: 10%;
  left: 10%;
}
.place-bet-container {
  color: white;
  background-color: rgba(255, 255, 255, 0.542);
  font-size: 2rem;
  border: 2px solid white;
  width: fit-content;
  padding: 1rem 2rem 1rem 2rem;
  border-radius: 25px;
  position: absolute;
  backdrop-filter: blur(5px);
  top: 65%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
}
.place-bet-container:hover {
  cursor: pointer;
  transform: translateX(-50%) scale(1.02);
  background-color: rgba(128, 128, 128, 0.492);
}
.hidePBC {
  animation: hidePlaceBet 0.5s ease-in-out forwards;
}
@keyframes hidePlaceBet {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>
