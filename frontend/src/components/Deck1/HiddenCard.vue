<script setup lang="ts">
defineProps({
  club1: Boolean,
});
</script>

<template>
  <div class="card-container">
    <div class="card">
      <div class="inner-card">
        <div class="lines line1" />
        <div class="lines line2" />
        <div class="lines line3" />
        <div class="lines line4" />
        <div class="lines line5" />
        <div class="lines line6" />
        <div class="lines line7" />
        <div class="lines line8" />
        <div class="lines line9" />
        <div class="lines line10" />
        <div class="lines line11" />
        <div class="lines line12" />
        <div class="lines line13" />
        <div class="lines line14" />
        <div class="lines line15" />
        <div class="lines line16" />
        <div class="lines line17" />
        <div class="lines line18" />
        <div class="lines line19" />
        <div class="lines line20" />
        <div class="lines line21" />
        <div class="lines line22" />
        <div class="lines line23" />
        <div class="lines line24" />
        <div class="lines line25" />
        <div class="lines line26" />

        <h2 class="hr">
          <span id="h" data-text="H">H</span><br /><span id="r" data-text="R">R</span>
        </h2>
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
.inner-card {
  height: 20rem;
  width: 13rem;
  border: 2px solid white;
  border-radius: 25px;
  background-color: grey;
  backdrop-filter: blur(3px);
  display: flex;
  position: absolute;
  align-self: center;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  justify-content: center;
  overflow: hidden;
}
.hr {
  font-size: 7rem;
  align-self: center;
  color: transparent;
  background: linear-gradient(to bottom right, red, rgb(230, 238, 1));
  background-clip: text;
  -webkit-background-clip: text;
  margin: 0;
}
#h::before {
  content: attr(data-text);
  position: absolute;
  transform: translate(-2px, 2px);
  z-index: -1;
  color: rgba(0, 0, 0, 0.7);
}
#r::before {
  content: attr(data-text);
  position: absolute;
  transform: translate(-2px, 2px);
  z-index: -1;
  color: rgba(0, 0, 0, 0.7);
}
.lines {
  position: absolute;
  width: 20rem;
  height: 0.15rem;
  background-color: white;
  z-index: -1;
}
.line1,
.line3,
.line5,
.line7,
.line9,
.line11,
.line13,
.line15,
.line17,
.line19,
.line21,
.line23,
.line25 {
  transform: rotate(45deg);
}
.line2,
.line4,
.line6,
.line8,
.line10,
.line12,
.line14,
.line16,
.line18,
.line20,
.line22,
.line24,
.line26 {
  transform: rotate(-45deg);
}
.line1,
.line2 {
  top: 50%;
}
.line3,
.line4 {
  top: 25%;
}
.line5,
.line6 {
  top: 75%;
}
.line7,
.line8 {
  top: 12.5%;
}
.line9,
.line10 {
  top: 37.5%;
}
.line11,
.line12 {
  top: 62.5%;
}
.line13,
.line14 {
  top: 87.5%;
}
.line15,
.line16 {
  top: 1%;
}
.line17,
.line18 {
  top: 99%;
}
.line19,
.line20 {
  top: -10%;
}
.line21,
.line22 {
  top: 110%;
}
.line23,
.line24 {
  top: -20%;
}
.line25,
.line26 {
  top: 120%;
}
</style>
