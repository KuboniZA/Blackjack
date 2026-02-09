<script lang="ts" setup>
import { ref, onMounted } from "vue";
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

const cards_left = ref<number>(0);
const player_card1 = ref<[string, string]>();
const player_card2 = ref<[string, string]>();
const ai_card1 = ref<[string, string]>();
const ai_card2 = ref<[string, string]>();
const player_points = ref<number>(0);
const ai_points = ref<number>(0);

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

const getCardComponent = (card?: [string, string]) => {
  if (!card) return null;
  const [suit, rank] = card;
  console.log(suit, rank);
  console.log(cardComponentMap[`${suit}-${rank}`]);
  const cardKey = cardComponentMap[`${suit}-${rank}`];
  return cardKey;
};

const newGame = async () => {
  const response = await fetch("http://127.0.0.1:8000/new-game");
  const data = await response.json();
  cards_left.value = data.cards_remaining.card_count;

  player_card1.value = data.first_deal[0][0];
  player_card2.value = data.first_deal[0][1];
  player_points.value = data.first_deal[1];

  ai_card1.value = data.first_deal_ai[0][0];
  ai_card2.value = data.first_deal_ai[0][1];
  ai_points.value = data.first_deal_ai[1];
};

const resetGame = async () => {
  const response = await fetch("http://127.0.0.1:8000/reset-game", { method: "POST" });
  const data = await response.json();
  cards_left.value = data.cards_remaining.card_count;

  player_card1.value = data.first_deal[0][0];
  player_card2.value = data.first_deal[0][1];
  player_points.value = data.first_deal[1];

  ai_card1.value = data.first_deal_ai[0][0];
  ai_card2.value = data.first_deal_ai[0][1];
  ai_points.value = data.first_deal_ai[1];
};

onMounted(() => {
  newGame();
});
</script>

<template>
  <div class="main-container">
    <div class="cards-remaining-container">
      <p class="cards-remaining">
        <span class="remaining-text">Cards remaining: </span>
        <span class="cards-rem-number">{{ cards_left }}</span>
      </p>
      <button class="reset" @click="resetGame">Reset Game</button>
    </div>

    <div class="hit-stand-container">
      <span class="add-card">🃏</span>
      <span>HIT</span>
    </div>
    <div class="hit-stand-container stand">
      <span class="add-card">✋🏾</span>
      <span>STAND</span>
    </div>
    <div class="cards-container">
      <component
        id="p-card1"
        class="player-cards cards"
        v-if="player_card1"
        :is="getCardComponent(player_card1)"
      />
      <component
        id="p-card2"
        class="player-cards cards"
        v-if="player_card2"
        :is="getCardComponent(player_card2)"
      />

      <component
        id="ai-card1"
        class="ai-cards cards"
        v-if="ai_card1"
        :is="getCardComponent(ai_card1)"
      />
      <component
        id="ai-card2"
        class="ai-cards cards"
        v-if="ai_card2"
        :is="getCardComponent(ai_card2)"
      />
    </div>
  </div>
</template>

<style scoped>
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
  left: 25%;
  top: 0;
  grid-template-columns: repeat(2, 1fr);
  display: grid;
  row-gap: 3rem;
}
.player-cards {
  top: 6rem;
  height: fit-content;
  width: fit-content;
}
#p-card1 {
  top: 60%;
  left: 30%;
  transform: scale(0.7) rotate(0deg);
}
#p-card2 {
  top: 60%;
  left: 40%;
  transform: scale(0.7) rotate(-5deg);
}
#ai-card1 {
  top: 2%;
  left: 30%;
  transform: scale(0.7) rotate(0deg);
}
#ai-card2 {
  top: 2%;
  left: 40%;
  transform: scale(0.7) rotate(-5deg);
}
</style>
