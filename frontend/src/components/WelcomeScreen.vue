<script lang="ts" setup>
import { ref } from "vue";
import GameModes from "./GameModes/GameModes.vue";
const showWelcome = ref(true);
const showMenu = ref(false);

const hideWelcomeShowMenu = () => {
  showWelcome.value = false;
  showMenu.value = true;
};
</script>

<template>
  <GameModes :isVisible="showMenu" />
  <div class="welcome-container" v-if="showWelcome">
    <h1>Welcome to</h1>
    <button id="play-btn" @click="hideWelcomeShowMenu">Play</button>
  </div>
</template>

<style scoped>
.welcome-container {
  width: 80dvw;
  height: 80dvh;
  /* border: 1px solid red; */
  position: relative;
  left: 10dvw;
  top: 10dvh;
  align-items: center;
}
h1 {
  position: absolute;
  color: transparent;
  background: linear-gradient(
    90deg,
    rgb(247, 210, 2),
    rgb(247, 39, 2),
    rgb(2, 247, 14),
    rgb(1, 202, 182),
    rgb(198, 1, 201),
    rgb(228, 3, 67)
  );
  background-size: 400% 200%;
  background-position: 0% 50%;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 8rem;
  left: 50%;
  top: 5%;
  transform: translateX(-50%);
  animation: text-btn-animation 5s linear infinite;
}
#play-btn {
  font-size: 4rem;
  padding: 1rem;
  width: 15rem;
  position: absolute;
  top: 70%;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 1000px;
  background-color: transparent;
  background: linear-gradient(
    /* Must fix animation so that it's smooth */ 90deg,
    rgb(247, 210, 2),
    rgb(247, 39, 2),
    rgb(2, 247, 14),
    rgb(1, 202, 182),
    rgb(198, 1, 201),
    rgb(228, 3, 67),
    rgb(247, 210, 2)
  );
  background-size: 400% 200%;
  color: white;
  border: none;
  animation: text-btn-animation 5s linear infinite;
}
#play-btn:hover {
  transform: scale(1.05) translateX(-50%);
  cursor: pointer;
}
@keyframes text-btn-animation {
  0% {
    background-position: 0 50%;
  }
  100% {
    background-position: 200% 50%;
  }
}
</style>
