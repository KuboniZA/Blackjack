<template>
  <div class="text-container">
    <h1 class="shimmer">
      <span class="text" id="row1">HIGH</span><span class="text" id="row2">ROLLER</span>
    </h1>
  </div>
</template>

<style scoped>
.text-container {
  width: 100%;
  height: 100dvh;
  display: grid;
  grid-template-columns: 2 (1fr);
  justify-content: center;
  place-items: center;
  z-index: -1000;
  position: absolute;
}
.shimmer {
  background: linear-gradient(to right, rgb(247, 210, 2), rgb(1, 202, 182));
  background-clip: text;
  color: transparent;
}
.text {
  font-size: clamp(5rem, 11vw + 1rem, 18rem);
  padding: 1.75rem;
  /* text-shadow: 0 4px 8px rgba(0, 0, 0, 0.6); */
}

@media screen and (width <= 900px) {
  .text-container {
    width: 100dvw;
    grid-template-rows: 2 (1fr);
  }
  .text {
    background: linear-gradient(to right, rgb(1, 202, 182), rgb(247, 210, 2));
    background-clip: text;
    color: transparent;
    justify-content: center;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    /* text-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7); */
  }
  #row1 {
    top: 35%;
  }
  #row2 {
    top: 45%;
    padding-top: 2rem;
  }
}
</style>
