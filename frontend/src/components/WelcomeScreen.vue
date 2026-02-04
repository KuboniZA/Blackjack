<script lang="ts" setup></script>

<template>
  <div class="welcome-container">
    <h1>Welcome to</h1>
    <button>Play</button>
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
  background: linear-gradient(to right, rgb(247, 210, 2), rgb(1, 202, 182));
  background-clip: text;
  font-size: 8rem;
  left: 50%;
  top: 5%;
  transform: translateX(-50%);
}
button {
  font-size: 4rem;
  padding: 1rem;
  width: 15rem;
  position: absolute;
  top: 70%;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 1000px;
}
</style>
