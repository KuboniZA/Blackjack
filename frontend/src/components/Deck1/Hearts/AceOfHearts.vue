<script setup lang="ts">
defineProps({
  heart1: Boolean,
});
</script>

<template>
  <div class="card-container" v-if="heart1">
    <div class="card">
      <div id="number-content">
        <span class="number">A</span>
        <div id="diamond-content-ratio">
          <span class="diamond cr" />
        </div>
      </div>

      <div id="number-content2">
        <span class="number">A</span>
        <div id="diamond-content-ratio">
          <span class="diamond cr" />
        </div>
      </div>

      <div id="diamond-content">
        <span class="diamond" />
      </div>
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
  height: 6.5rem;
  width: 6.5rem;
  background-color: red;
  position: absolute;
  top: 0%;
  left: 50%;
  transform: translateX(-50%);
}
#diamond-content {
  width: 5.5rem;
  height: 6.5rem;
  border: 1px solid purple;
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translateX(-50%);
  clip-path: shape(from 50% 91%, line to 90% 50%, arc to 50% 9% of 1%, arc to 10% 50% of 1%);
  /* clip-path: shape(from 0% 50%, curve to 50% 0% with 40% 40%, line to 0% 100%, close); */
}
.number {
  font-size: 2rem;
  font-weight: bold;
  position: absolute;
  left: 0.85rem;
  top: 0.75rem;
  color: red;
}
#diamond-content-ratio {
  transform: scale(0.3);
  position: relative;
  left: 1.2rem;
  top: 2.2rem;
}
.cr {
  top: 3rem;
  left: 1.2rem;
  clip-path: shape(from 50% 91%, line to 90% 50%, arc to 50% 9% of 1%, arc to 10% 50% of 1%);
}
#number-content2 {
  position: absolute;
  left: 14.5rem;
  top: 98%;
  transform: rotate(180deg);
}
</style>
