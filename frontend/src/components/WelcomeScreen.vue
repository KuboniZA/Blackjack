<script lang="ts" setup>
import { ref } from "vue";
// import GameModes from "./GameModes/GameModes.vue";
import AceOfSpades from "./Deck1/Spades/AceOfSpades.vue";
import QueenOfHearts from "./Deck1/Hearts/QueenOfHearts.vue";
import ChipsView from "./ChipsView.vue";
import TenOfDiamonds from "./Deck1/Diamonds/TenOfDiamonds.vue";

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
    <div class="card-scale">
      <TenOfDiamonds :diamond10="showWelcome" id="ten" />
    </div>
    <div class="chips-bg">
      <ChipsView :rand500="showWelcome" id="chip500" class="welcome-chips" />
      <ChipsView :rand25="showWelcome" id="chip25" class="welcome-chips" />
      <ChipsView :rand1m="showWelcome" id="chip1m" class="welcome-chips" />
      <ChipsView :rand5="showWelcome" id="chip5" class="welcome-chips" />
      <ChipsView :rand10k="showWelcome" id="chip10k" class="welcome-chips" />
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
  width: 100%;
  height: 100%;
  overflow: hidden;
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
  font-size: clamp(1rem, 8vw, 5rem);
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
#ten {
  left: 30%;
  top: -60% !important;
  transform: rotate(-15deg);
  display: none;
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
#chip10k {
  left: -13%;
  top: -20%;
  display: none;
}

/******************* TABLETS *******************/

@media screen and (min-width: 1000px) and (max-width: 1999px) and (orientation: portrait) {
  #play-btn {
    font-size: 2.5rem;
    width: 12rem;
  }
  h1 {
    top: 25%;
  }
  #queen {
    left: 80%;
    top: 25%;
  }

  #ace {
    left: 5%;
    top: 60%;
  }
  #ten {
    left: 0%;
    top: -10% !important;
    display: flex;
  }
  /* .welcome-chips {
    transform: scale(1.2) !important;
  } */
  #chip500 {
    left: 20%;
    top: -10%;
  }
  #chip25 {
    left: -55%;
    top: 30%;
  }
  #chip1m {
    left: -25%;
    top: 50%;
    z-index: -1001;
  }
  #chip5 {
    left: 53%;
    top: 72%;
    z-index: -1001;
  }
  #chip10k {
    left: -14%;
    top: 32%;
    display: flex;
  }
}

@media screen and (min-width: 900px) and (max-width: 999px) and (orientation: portrait) {
  #play-btn {
    font-size: 2.5rem;
    width: 12rem;
  }
  h1 {
    top: 25%;
  }
  #queen {
    left: 70%;
    top: 25%;
  }

  #ace {
    left: 5%;
    top: 60%;
  }
  #ten {
    left: 10%;
    top: -10% !important;
    display: flex;
  }
  #chip500 {
    left: 20%;
    top: -10%;
  }
  #chip25 {
    left: -55%;
    top: 30%;
  }
  #chip1m {
    left: -30%;
    top: 50%;
    z-index: -1001;
  }
  #chip5 {
    left: 50%;
    top: 70%;
    z-index: -1001;
  }
  #chip10k {
    left: -22%;
    top: 32%;
    display: flex;
  }
}

@media screen and (min-width: 800px) and (max-width: 899px) {
  h1 {
    top: 10%;
    text-align: center;
  }

  #play-btn {
    font-size: 1.8rem;
    width: 10rem;
    top: 75%;
    /* transform: translateX(-50%) scale(0.8); */
  }
  .card-scale {
    transform: scale(0.75);
  }

  #queen {
    left: 90%;
    top: 14%;
    z-index: -1;
  }

  #ace {
    left: -4%;
    top: 60%;
  }

  #ten {
    left: 0%;
    top: -10% !important;
    display: flex;
  }
  #chip500 {
    left: 20%;
    top: -10%;
  }
  #chip25 {
    left: -60%;
    top: 30%;
  }
  #chip1m {
    left: -35%;
    top: 44%;
    z-index: -1001;
  }
  #chip5 {
    left: 48%;
    top: 65%;
    z-index: -1001;
  }
  #chip10k {
    left: -21%;
    top: 32%;
    /* display: flex; */
  }
}

@media screen and (min-width: 700px) and (max-width: 799px) {
  h1 {
    top: 15%;
    text-align: center;
  }

  #play-btn {
    font-size: 1.8rem;
    width: 10rem;
    top: 75%;
    /* transform: translateX(-50%) scale(0.8); */
  }
  .card-scale {
    transform: scale(0.7);
  }

  #queen {
    left: 90%;
    top: 14%;
    z-index: -1;
  }

  #ace {
    left: -4%;
    top: 60%;
  }

  #ten {
    left: 0%;
    top: -10% !important;
    display: flex;
  }
  #chip500 {
    left: 5%;
    top: -10%;
  }
  #chip25 {
    left: -60%;
    top: 30%;
  }
  #chip1m {
    left: -35%;
    top: 44%;
    z-index: -1001;
  }
  #chip5 {
    left: 40%;
    top: 70%;
    z-index: -1001;
  }
  #chip10k {
    left: -27%;
    top: 30%;
    /* display: flex; */
  }
}

@media screen and (min-width: 600px) and (max-width: 699px) {
  h1 {
    top: 15%;
    text-align: center;
  }

  #play-btn {
    font-size: 1.8rem;
    width: 10rem;
    top: 75%;
    /* transform: translateX(-50%) scale(0.8); */
  }
  .card-scale {
    transform: scale(0.75);
  }

  #queen {
    left: 90%;
    top: 14%;
    z-index: -1;
  }

  #ace {
    left: -4%;
    top: 60%;
  }

  #ten {
    left: 0%;
    top: -10% !important;
    display: flex;
  }
  #chip500 {
    left: 20%;
    top: -10%;
  }
  #chip25 {
    left: -60%;
    top: 30%;
  }
  #chip1m {
    left: -35%;
    top: 44%;
    z-index: -1001;
  }
  #chip5 {
    left: 33%;
    top: 65%;
    z-index: -1001;
  }
  #chip10k {
    left: -7%;
    top: 22%;
    display: flex;
  }
}

@media screen and (min-width: 500px) and (max-width: 599px) {
  h1 {
    top: 15%;
    text-align: center;
  }

  #play-btn {
    font-size: 1.8rem;
    width: 10rem;
    top: 83%;
    transform: translateX(-50%) scale(0.8);
  }

  .card-scale {
    transform: scale(0.4);
  }

  #queen {
    left: 100%;
    top: -14%;
    z-index: -1;
  }

  #ace {
    left: -35%;
    top: 90%;
  }

  #ten {
    left: -35%;
    top: -50%;
    display: flex;
  }

  .welcome-chips {
    transform: scale(0.8);
  }
  #chip500 {
    left: -64%;
    top: 1%;
  }
  #chip25 {
    left: -60%;
    top: 0;
  }
  #chip1m {
    left: -67%;
    top: 34%;
    z-index: -1001;
  }
  #chip5 {
    left: 23%;
    top: 75%;
    z-index: -1001;
  }
  #chip10k {
    left: -70%;
    top: 27%;
    display: flex;
  }
}

/****************** PHONE *******************/

@media screen and (min-width: 400px) and (max-width: 499px) {
  h1 {
    top: 15%;
    text-align: center;
  }

  #play-btn {
    font-size: 1.8rem;
    width: 10rem;
    top: 83%;
    transform: translateX(-50%) scale(0.8);
  }

  .card-scale {
    transform: scale(0.4);
  }

  #queen {
    left: 100%;
    top: -14%;
    z-index: -1;
  }

  #ace {
    left: -35%;
    top: 90%;
  }

  #ten {
    left: -35%;
    top: -50%;
    display: flex;
  }

  .welcome-chips {
    transform: scale(0.8);
  }
  #chip500 {
    left: -84%;
    top: 8%;
  }
  #chip25 {
    left: -60%;
    top: 0;
  }
  #chip1m {
    left: -67%;
    top: 44%;
    z-index: -1001;
  }
  #chip5 {
    left: 23%;
    top: 75%;
    z-index: -1001;
  }
  #chip10k {
    left: -88%;
    top: 29%;
    display: flex;
  }
}
@media screen and (max-width: 399px) {
  h1 {
    top: 20%;
  }
  #queen {
    left: 110%;
    top: -10%;
    z-index: -1;
  }
  #ace {
    left: -50%;
    top: 67%;
  }
  #ten {
    left: -35%;
    top: -50%;
    display: flex;
  }
  .card-scale {
    transform: scale(0.4);
  }
  #play-btn {
    font-size: 1.8rem;
    width: 10rem;
    top: 83%;
    transform: translateX(-50%) scale(0.8);
  }
  .welcome-chips {
    transform: scale(0.75);
  }
  #chip500 {
    left: -80%;
    top: 2%;
  }
  #chip25 {
    left: -70%;
    top: 0;
  }
  #chip1m {
    left: -75%;
    top: 37%;
  }
  #chip5 {
    left: 13%;
    top: 63%;
    z-index: -1001;
  }
  #chip10k {
    left: -110%;
    top: 28%;
    /* display: flex; */
  }
}
</style>
