<script lang="ts" setup></script>

<template>
  <div class="chips-container">
    <div class="container-mask" />

    <div id="rand1">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">1</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.chips-container {
  position: relative;
  width: 45rem;
  height: 15rem;
  top: 45rem;
  left: 3rem;
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.8);
  /*border: 1px solid black;*/
  border-radius: 25px;
}
.container-mask {
  width: 20rem;
  height: 2rem;
  position: absolute;
  right: 0;
  /*border: 1px solid black;*/
  border-top-right-radius: 25px;
  border-bottom-left-radius: 25px;
  box-shadow: inset 4px -4px 8px rgba(0, 0, 0, 0.4);
}
#rand1 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 1.5rem;
  top: 3rem;
  background-color: greenyellow;
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
.inner-mask {
  height: 3.5rem;
  width: 3.5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background-color: white;
  box-shadow: inset -2px 4px 8px rgba(0, 0, 0, 0.4);
  z-index: 5;
}
.chip {
  font-size: 2rem;
  font-weight: bold;
}
.horizontal-line {
  position: absolute;
  width: 5rem;
  height: 0.5rem;
  background-color: black;
}
.vertical-line {
  position: absolute;
  width: 0.5rem;
  height: 5rem;
  background-color: black;
}
.left-leaning-line {
  position: absolute;
  width: 0.5rem;
  height: 7.07rem;
  border-radius: 25px;
  background-color: black;
  transform: rotate(-45deg);
}
.right-leaning-line {
  position: absolute;
  width: 0.5rem;
  height: 7.07rem;
  border-radius: 25px;
  background-color: black;
  transform: rotate(45deg);
}
</style>
