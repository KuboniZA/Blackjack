<script setup lang="ts">
import { ref } from "vue";
const club9 = ref(false);
</script>

<template>
  <div class="card-container" v-if="club9">
    <div class="card">
      <div id="number-content">
        <span class="number">9</span>
        <div id="club-content-ratio">
          <span class="club-circle cr" />
          <span class="club-circle c2 c2r" />
          <span class="club-circle c3 c3r" />
          <span class="vline lineR" />
          <!-- <span class="bg-square bg-sq-R" /> -->
          <span class="triangle ltriangle lt-ratio" />
          <span class="triangle rtriangle rt-ratio" />
        </div>
      </div>

      <div id="number-content2">
        <span class="number">9</span>
        <div id="club-content-ratio">
          <span class="club-circle cr" />
          <span class="club-circle c2 c2r" />
          <span class="club-circle c3 c3r" />
          <span class="vline lineR" />
          <!-- <span class="bg-square bg-sq-R" /> -->
          <span class="triangle ltriangle lt-ratio" />
          <span class="triangle rtriangle rt-ratio" />
        </div>
      </div>

      <div id="club-content">
        <span class="club-circle" />
        <span class="club-circle c2" />
        <span class="club-circle c3" />
        <span class="vline" />
        <span class="bg-square" />
        <span class="triangle ltriangle" />
        <span class="triangle rtriangle" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-container {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 30%;
}
.card {
  height: 22rem;
  width: 15rem;
  border: 2px solid white;
  border-radius: 25px;
  background-color: rgb(255, 255, 255, 0.25);
  backdrop-filter: blur(2px);
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
  top: 55%;
  left: 36.75%;
}
.ltriangle {
  clip-path: shape(from 0% 100%, curve to 100% 0% with 90% 90%, line to 100% 100%, close);
}
.rtriangle {
  left: 50%;
  clip-path: shape(from 0% 0%, curve to 100% 100% with 10% 90%, line to 0% 100%, close);
}
#club-content {
  width: fit-content;
  height: fit-content;
}
.number {
  font-size: 2rem;
  font-weight: bold;
  position: absolute;
  left: 1rem;
  top: 0.75rem;
  color: blueviolet;
}
#club-content-ratio {
  transform: scale(0.3);
  position: relative;
  left: 1.2rem;
  top: 2.1rem;
}
.cr {
  top: 3rem;
  left: 1.1rem;
}
.c2r {
  top: 5.25rem;
}
.c3r {
  top: 5.25rem;
  left: 2.25rem;
}
.lineR {
  top: 6rem;
  left: 1.1rem;
}
.lt-ratio {
  top: 7.6rem;
  left: -1rem;
}
.rt-ratio {
  top: 7.6rem;
  left: 1rem;
}
#number-content2 {
  position: absolute;
  left: 14.75rem;
  top: 98%;
  transform: rotate(180deg);
}
</style>
