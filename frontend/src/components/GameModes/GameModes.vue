<script lang="ts" setup>
defineProps({
  isVisible: Boolean,
});
</script>

<template>
  <div id="game-mode-modal" v-if="isVisible">
    <div id="game-mode-container">
      <button class="game-mode-btn shimmer">Low Roller</button>
      <button class="game-mode-btn shimmer">Mid Roller</button>
      <button class="game-mode-btn shimmer">High Roller</button>
    </div>
  </div>
</template>

<style scoped>
#game-mode-modal {
  width: 100dvw;
  height: 100dvh;
  position: fixed;
  background-color: rgba(255, 255, 255, 0.258);
  backdrop-filter: blur(4px);
}
.game-mode-btn {
  display: block;
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
  position: relative;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  top: 50%;
}
.game-mode-btn:hover {
  transform: scale(1.05);
  background: linear-gradient(to bottom right, rgba(255, 0, 0, 0.771), rgba(0, 0, 255, 0.717));
  cursor: pointer;
}
/* Shimmer layer */
.shimmer::before {
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
.game-mode-btn:hover.shimmer::before {
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

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  .game-mode-btn:hover.shimmer::before {
    animation: none;
  }
}
</style>
