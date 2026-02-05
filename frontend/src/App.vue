<script setup lang="ts">
// import ChipsView from "./components/ChipsView.vue";
import QueenOfHearts from "./components/Hearts/QueenOfHearts.vue";
import TableView from "./components/TableView.vue";
import WelcomeScreen from "./components/WelcomeScreen.vue";
// import TestView from "./components/TestView.vue";
</script>

<template>
  <TableView />
  <QueenOfHearts />
  <WelcomeScreen />
  <!-- <ChipsView /> -->
  <!-- <TestView /> -->
  <RouterView />
</template>

<style scoped></style>
