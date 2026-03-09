<script setup lang="ts">
import { ref } from "vue";

// import ChipsView from "./components/ChipsView.vue";
import OneDeckGame from "./components/GameModes/OneDeckGame.vue";
import TableView from "./components/TableView.vue";
import WelcomeScreen from "./components/WelcomeScreen.vue";
import GameModes from "./components/GameModes/GameModes.vue";
// import TestView from "./components/TestView.vue";

type GameState = "welcome" | "modeSelect" | "betting" | "playing";

const state = ref<GameState>("welcome");

function startGame() {
  state.value = "modeSelect";
}
function selectOneDeck() {
  state.value = "betting";
}
function beginRound() {
  state.value = "playing";
}
function resetGame() {
  state.value = "welcome";
}
</script>

<template>
  <TableView />
  <OneDeckGame
    v-if="state === 'betting' || state === 'playing'"
    :playing="state === 'playing'"
    @betPlaced="beginRound"
    @roundOver="state = 'betting'"
    @reset="resetGame"
  />
  <WelcomeScreen v-if="state === 'welcome'" @play="startGame" />
  <GameModes v-if="state === 'modeSelect'" @oneDeck="selectOneDeck" @back="resetGame" />
  <!-- <ChipsView /> -->
  <!-- <TestView /> -->
  <RouterView />
</template>

<style scoped></style>
