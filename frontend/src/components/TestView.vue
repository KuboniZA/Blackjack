<template>
  <div class="square-container">
    <span class="sq"> </span>
  </div>
</template>

<style scoped>
.square-container {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
}
.sq {
  width: 30rem;
  height: 30rem;
  background-color: rgba(0, 0, 255, 0.489);
  backdrop-filter: blur(3px);
  /* clip-path: shape(from 0% 100%, curve to 100% 0% with 90% 90%, line to 100% 100%, close); */
  clip-path: shape(from 0% 0%, curve to 100% 100% with 10% 90%, line to 0% 100%, close);
}
</style>
