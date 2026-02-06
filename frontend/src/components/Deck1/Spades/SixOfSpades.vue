<script setup lang="ts">
import { ref } from "vue";
const spade6 = ref(false);
</script>

<template>
  <div class="card-container" v-if="spade6">
    <div class="card">
      <div id="number-content">
        <span class="number">6</span>
        <div id="diamond-content-ratio">
          <span class="diamond cr" />
        </div>
        <span class="vline" />
        <span class="triangle ltriangle" />
        <span class="triangle rtriangle" />
      </div>

      <div id="number-content2">
        <span class="number">6</span>
        <div id="diamond-content-ratio">
          <span class="diamond cr" />
        </div>
        <span class="vline lineR" />
        <span class="triangle ltriangle lt-ratio" />
        <span class="triangle rtriangle rt-ratio" />
      </div>

      <div id="diamond-content">
        <span class="diamond" />
      </div>
      <span class="vline lineR" />
      <span class="triangle ltriangle lt-ratio" />
      <span class="triangle rtriangle rt-ratio" />
    </div>
  </div>
</template>

<style scoped>
.card-container {
  position: absolute;
  left: 51%;
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
.diamond {
  height: 6rem;
  width: 6rem;
  background-color: blueviolet;
  position: absolute;
  top: 0%;
  left: 50%;
  transform: translateX(-50%);
}
#diamond-content {
  width: 5rem;
  height: 6rem;
  position: absolute;
  top: 32%;
  left: 50%;
  transform: translateX(-50%) rotate(180deg);
  clip-path: shape(from 50% 91%, line to 90% 50%, arc to 50% 9% of 1%, arc to 10% 50% of 1%);
  /* clip-path: shape(from 0% 50%, curve to 50% 0% with 40% 40%, line to 0% 100%, close); */
}
.number {
  font-size: 2rem;
  font-weight: bold;
  position: absolute;
  left: 1.05rem;
  top: 0.75rem;
  color: blueviolet;
}
#diamond-content-ratio {
  transform: scale(0.25);
  position: relative;
  left: 1.2rem;
  top: 2.2rem;
}
.cr {
  top: 3rem;
  left: -1.5rem;
  clip-path: shape(from 50% 91%, line to 90% 50%, arc to 50% 9% of 1%, arc to 10% 50% of 1%);
  transform: rotate(180deg);
}
#number-content2 {
  position: absolute;
  left: 14.5rem;
  top: 98%;
  transform: rotate(180deg);
}
.triangle {
  width: 2rem;
  height: 2rem;
  background-color: blueviolet;
  position: absolute;
  top: 55%;
  left: 36.75%;
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
.ltriangle {
  clip-path: shape(from 0% 100%, curve to 100% 0% with 90% 90%, line to 100% 100%, close);
}
.rtriangle {
  left: 50%;
  clip-path: shape(from 0% 0%, curve to 100% 100% with 10% 90%, line to 0% 100%, close);
}
.lineR {
  transform: scale(0.22);
  top: 2.4rem;
  left: 1.3rem;
}
.lt-ratio {
  transform: scale(0.25);
  top: 3.5rem;
  left: 0.27rem;
}
.rt-ratio {
  transform: scale(0.25);
  top: 3.5rem;
  left: 0.77rem;
}
</style>
