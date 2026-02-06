<script lang="ts" setup>
import { ref, onMounted } from "vue";

const ai_cards = ref<number>(0);

const newGame = async () => {
  const response = await fetch("http://127.0.0.1:8000/new-game");
  const data = await response.json();
  console.log(data);
  ai_cards.value = data.cards_remaining.card_count;
};

onMounted(() => {
  newGame();
});
</script>

<template>
  <div>
    <p id="cards-remaining">
      <span id="remaining-text">Cards remaining: </span
      ><span id="cards-rem-number">{{ ai_cards }}</span>
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
