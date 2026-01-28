<script lang="ts" setup></script>

<template>
  <div class="chips-container">
    <div class="container-mask" />
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
</style>
