<script setup lang="ts"></script>

<template>
  <div class="card-container">
    <div class="card">
      <span class="club-circle" />
      <span class="club-circle c2" />
      <span class="club-circle c3" />
      <span class="vline" />
      <span class="bg-square" />
      <span class="triangle ltriangle" />
      <span class="triangle rtriangle" />
    </div>
  </div>
</template>

<style scoped>
.card-container {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 60%;
}
.card {
  height: 22rem;
  width: 15rem;
  border: 2px solid white;
  border-radius: 25px;
  background-color: rgb(255, 255, 255, 0.25);
  display: flex;
  position: relative;
}
.club-circle {
  height: 3rem;
  width: 3rem;
  background-color: blueviolet;
  border-radius: 50%;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateX(-50%);
}
.c2 {
  top: 46%;
  left: 40%;
}
.c3 {
  top: 46%;
  left: 60%;
}
.vline {
  width: 0.5rem;
  height: 3.5rem;
  background-color: blueviolet;
  position: absolute;
  top: 48%;
  left: 50%;
  transform: translateX(-50%);
}
.bg-square {
  width: 1rem;
  height: 1rem;
  background-color: blueviolet;
  position: absolute;
  top: 48%;
  left: 50%;
  transform: translateX(-50%);
}
.triangle {
  width: 2rem;
  height: 2rem;
  background-color: blueviolet;
  position: absolute;
  top: 54.75%;
  left: 36.75%;
}
.ltriangle {
  clip-path: shape(from 0% 100%, curve to 100% 0% with 90% 90%, line to 100% 100%, close);
}
.rtriangle {
  left: 50%;
  clip-path: shape(from 0% 0%, curve to 100% 100% with 10% 90%, line to 0% 100%, close);
}
</style>
