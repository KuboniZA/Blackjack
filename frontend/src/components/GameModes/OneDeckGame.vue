<script lang="ts" setup>
import { ref, onMounted } from "vue";
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
import SevenofDiamonds from "../Deck1/Diamonds/SevenofDiamonds.vue";
import SevenOfHearts from "../Deck1/Hearts/SevenOfHearts.vue";
import SevenOfSpades from "../Deck1/Spades/SevenOfSpades.vue";
import EightOfClubs from "../Deck1/Clubs/EightOfClubs.vue";
import EightOfDiamonds from "../Deck1/Diamonds/EightOfDiamonds.vue";
import EightOFHearts from "../Deck1/Hearts/EightOFHearts.vue";
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

const newGame = async () => {
  const response = await fetch("http://127.0.0.1:8000/new-game");
  const data = await response.json();
  console.log(data);
  cards_left.value = data.cards_remaining.card_count;
};

onMounted(() => {
  newGame();
});
</script>

<template>
  <div>
    <AceOfClubs />
    <AceOfDiamonds />
    <AceOfHearts />
    <AceOfSpades />
    <TwoOfClubs />
    <TwoOfDiamonds />
    <TwoOfHearts />
    <TwoOfSpades />
    <ThreeOfClubs />
    <ThreeOfDiamonds />
    <ThreeOfHearts />
    <ThreeOfSpades />
    <FourOfClubs />
    <FourOfDiamonds />
    <FourOfHearts />
    <FourOfSpades />
    <FiveOfClubs />
    <FiveOfDiamonds />
    <FiveOfHearts />
    <FiveOfSpades />
    <SixOfClubs />
    <SixOfDiamonds />
    <SixOfHearts />
    <SixOfSpades />
    <SevenOfClubs />
    <SevenofDiamonds />
    <SevenOfHearts />
    <SevenOfSpades />
    <EightOfClubs />
    <EightOfDiamonds />
    <EightOFHearts />
    <EightOfSpades />
    <NineOfClubs />
    <NineOfDiamonds />
    <NineOfHearts />
    <NineOfSpades />
    <TenOfClubs />
    <TenOfDiamonds />
    <TenOfHearts />
    <TenOfSpades />
    <JackOfClubs />
    <JackOfDiamonds />
    <JackOfHearts />
    <JackOfSpades />
    <QueenOfClubs />
    <QueenOfDiamonds />
    <QueenOfHearts />
    <QueenOfSpades />
    <KingOfClubs />
    <KingOfDiamonds />
    <KingOfHearts />
    <KingOfSpades />
  </div>

  <div>
    <p id="cards-remaining">
      <span id="remaining-text">Cards remaining: </span
      ><span id="cards-rem-number">{{ cards_left }}</span>
    </p>
  </div>
</template>

<style scoped>
#cards-remaining {
  position: absolute;
  top: 8%;
  left: 80dvw;
  background: linear-gradient(to right, blue, red);
  font-size: 2rem;
  color: white;
  display: flex;
  justify-content: center;
  border-radius: 25px;
  height: 3.5rem;
  width: 20rem;
  place-items: center;
  justify-content: center;
  gap: 1rem;
  z-index: -2;
  border: 2px solid white;
}
#cards-rem-number {
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
}
#cards-rem-number::after {
  content: "";
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 50%;
  position: absolute;
  background-color: transparent;
  background: linear-gradient(to bottom right, white, grey);
  z-index: -1;
}
</style>
