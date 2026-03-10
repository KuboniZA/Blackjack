<script lang="ts" setup>
import { ref } from "vue";
// import GameModes from "./GameModes/GameModes.vue";
import AceOfSpades from "./Deck1/Spades/AceOfSpades.vue";
import QueenOfHearts from "./Deck1/Hearts/QueenOfHearts.vue";
import ChipsView from "./ChipsView.vue";

const showWelcome = ref(true);
// const showMenu = ref(false);

const hideWelcomeShowMenu = () => {
  showWelcome.value = false;
  // showMenu.value = true;
};

const emit = defineEmits(["play"]);
</script>

<template>
  <!-- <GameModes :isVisible="showMenu" /> -->
  <div class="main-container">
    <div class="card-scale z-index">
      <AceOfSpades :spade1="showWelcome" id="ace" />
    </div>
    <div class="card-scale">
      <QueenOfHearts :heartQ="showWelcome" id="queen" />
    </div>
    <div class="chips-bg">
      <ChipsView :rand500="showWelcome" id="chip500" class="welcome-chips" />
      <ChipsView :rand25="showWelcome" id="chip25" class="welcome-chips" />
      <ChipsView :rand1m="showWelcome" id="chip1m" class="welcome-chips" />
      <ChipsView :rand5="showWelcome" id="chip5" class="welcome-chips" />
    </div>

    <div class="welcome-container">
      <h1>Welcome to</h1>
      <button id="play-btn" @click="(emit('play'), hideWelcomeShowMenu)">Play</button>
    </div>
  </div>
</template>

<style scoped>
.main-container {
  position: fixed;
  width: 100dvw;
  height: 100dvh;
}
.welcome-container {
  width: 80dvw;
  height: 80dvh;
  /* border: 1px solid red; */
  position: relative;
  left: 10dvw;
  top: 10dvh;
  align-items: center;
  z-index: 100;
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
#ace {
  left: 10%;
  top: 43%;
  transform: rotate(-30deg);
}
#queen {
  left: 75%;
  top: 20%;
  transform: rotate(30deg);
}
.card-scale {
  position: absolute;
  width: 100dvw;
  height: 100dvh;
  transform: scale(0.8);
}
.z-index {
  z-index: -1001;
}
.chips-bg {
  width: 100dvw;
  height: 100dvh;
  position: absolute;
}
#chip500 {
  left: 15%;
  top: 4%;
}
#chip25 {
  left: 35%;
  top: 64%;
}
#chip1m {
  left: 67%;
  top: -13%;
  z-index: -1001;
}
#chip5 {
  left: -5%;
  top: 49%;
  z-index: -1001;
}
</style>
