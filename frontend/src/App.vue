<script setup lang="ts">
// import ChipsView from "./components/ChipsView.vue";
import OneDeckGame from "./components/GameModes/OneDeckGame.vue";
import TableView from "./components/TableView.vue";
// import WelcomeScreen from "./components/WelcomeScreen.vue";
// import TestView from "./components/TestView.vue";
</script>

<template>
  <TableView />
  <OneDeckGame ?></OneDeckGame>
  <!-- <WelcomeScreen /> -->
  <!-- <ChipsView /> -->
  <!-- <TestView /> -->
  <RouterView />
</template>

<style scoped></style>
