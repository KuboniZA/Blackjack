<script lang="ts" setup>
// import { ref } from "vue";
// import OneDeckGame from "./OneDeckGame.vue";

const emit = defineEmits(["oneDeck", "back"]);

// defineProps({
//   isVisible: Boolean,
// });
</script>

<template>
  <div id="game-mode-modal">
    <div id="game-mode-container">
      <button class="game-mode-btn GM" @click="emit('oneDeck')">1 Deck</button>
      <button class="game-mode-btn GM">2 Decks</button>
      <!--<button class="game-mode-btn GM">3 Decks</button>
      <button class="game-mode-btn GM">4 Decks</button>
      <button class="game-mode-btn GM">5 Decks</button>
      <button class="game-mode-btn GM">6 Decks</button>
      <button class="game-mode-btn GM">7 Decks</button>
      <button class="game-mode-btn GM">8 Decks</button> -->
      <button id="back-btn" @click="emit('back')">Back</button>
    </div>
  </div>
</template>

<style scoped>
#game-mode-modal {
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  position: fixed;
  background-color: rgba(255, 255, 255, 0.258);
  backdrop-filter: blur(4px);
  z-index: 10;
}
.game-mode-btn {
  width: 30rem;
  height: 7rem;
  font-size: 1.5rem;
  background-color: transparent;
  border: 2px solid white;
  background: linear-gradient(to bottom right, rgba(0, 0, 255, 0.48), rgba(255, 0, 0, 0.486));
  border-radius: 1000px;
  margin-bottom: 1rem;
  backdrop-filter: blur(2px);
  color: white;
  overflow: hidden;
  box-shadow:
    inset -2px 2px 4px rgba(0, 0, 0, 0.6),
    inset 2px -2px 6px rgba(0, 0, 0, 0.6);
}
#game-mode-container {
  width: fit-content;
  height: fit-content;
  position: absolute;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(5, 1fr);
  column-gap: 3rem;
  row-gap: 1rem;
  z-index: 20;
  left: 50%;
  top: 50%;
  transform: translateX(-50%);
}
#back-btn {
  position: relative;
  grid-column: span 2;
  justify-self: center;
  top: 15%;
  width: 12rem;
  height: 4rem;
  border-radius: 1000px;
  font-size: 1.2rem;
  background-color: transparent;
  border: 2px solid white;
  background: linear-gradient(to bottom right, rgba(255, 0, 0, 0.486), rgba(0, 0, 255, 0.48));
  color: white;
}
.game-mode-btn:hover {
  transform: scale(1.05);
  background: linear-gradient(to bottom right, rgba(255, 0, 0, 0.771), rgba(0, 0, 255, 0.717));
  cursor: pointer;
}
#back-btn:hover {
  transform: scale(1.05);
  background: linear-gradient(to bottom right, rgba(0, 0, 255, 0.717), rgba(255, 0, 0, 0.771));
  cursor: pointer;
}
/* Shimmer layer */
.shimmerGM::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;

  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.35) 50%,
    rgba(255, 255, 255, 0) 100%
  );

  opacity: 0;
  pointer-events: none;
}
/* Run animation ONLY while hovered */
.game-mode-btn:hover.shimmerGM::before {
  animation: shimmer-sweep 2.25s ease-out infinite;
}

/* Keyframes */
@keyframes shimmer-sweep {
  0% {
    transform: translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  50% {
    transform: translateX(200%);
    opacity: 1;
  }
  100% {
    transform: translateX(200%);
    opacity: 0;
  }
}

/* ****************** MEDIA QUERIES BELOW **********************/

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  .game-mode-btn:hover.shimmerGM::before {
    animation: none;
  }
}

@media (min-width: 710px) and (max-width: 1024px) {
  #game-mode-container {
    column-gap: 2rem;
    row-gap: 1rem;
  }

  .game-mode-btn {
    width: 22rem;
    height: 6rem;
    font-size: 1.3rem;
    transform: scale(0.9);
  }

  #back-btn {
    width: 10rem;
    height: 3.5rem;
  }
}

@media (max-width: 709px) {
  #game-mode-container {
    grid-template-columns: 1fr;
    row-gap: 1rem;
    transform: translate(-50%, -30%) scale(0.5);
  }

  .game-mode-btn {
    width: 80vw;
    height: 5rem;
    font-size: 1.1rem;
  }

  #back-btn {
    width: 8rem;
    height: 3rem;
  }
}
</style>
