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

    <div id="rand5">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">5</span>
      </div>
    </div>

    <div id="rand10">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">10</span>
      </div>
    </div>

    <div id="rand25">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">25</span>
      </div>
    </div>

    <div id="rand50">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">50</span>
      </div>
    </div>

    <div id="rand100">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">100</span>
      </div>
    </div>

    <div id="rand500">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">500</span>
      </div>
    </div>

    <div id="rand1000">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask">
        <span class="chip">1000</span>
      </div>
    </div>

    <div id="rand10000">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask in10k">
        <span class="chip c10k">10 000</span>
      </div>
    </div>

    <div id="rand100000">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask in10k">
        <span class="chip c100k">100 000</span>
      </div>
    </div>

    <div id="rand500000">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask in10k">
        <span class="chip c100k">500 000</span>
      </div>
    </div>

    <div id="rand1000000">
      <div class="horizontal-line length1M" />
      <div class="vertical-line vlength1M" />
      <div class="left-leaning-line" />
      <div class="right-leaning-line" />
      <div class="inner-mask in1M">
        <span class="chip c1M">1 000 000</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.chips-container {
  position: relative;
  width: 45rem;
  height: 20rem;
  top: 38rem;
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
  font-size: 1.5rem;
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

#rand5 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 9rem;
  top: 3rem;
  background-color: rgb(99, 172, 250);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand10 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 16.5rem;
  top: 3rem;
  background-color: rgb(249, 90, 212);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand25 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 24rem;
  top: 3rem;
  background-color: rgb(68, 169, 61);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand50 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 31.5rem;
  top: 3rem;
  background-color: rgb(175, 24, 24);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand100 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 38rem;
  top: 3rem;
  background-color: rgb(57, 31, 189);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand500 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 1.5rem;
  top: 11rem;
  background-color: rgb(103, 3, 84);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand1000 {
  height: 5rem;
  width: 5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 9rem;
  top: 11rem;
  background-color: rgb(50, 180, 176);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}

#rand10000 {
  height: 5.5rem;
  width: 5.5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 16.25rem;
  top: 11rem;
  background-color: rgb(186, 184, 19);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
.length10k {
  width: 5.5rem;
}
.vlength10k {
  height: 5.5rem;
}
.in10k {
  height: 4rem;
  width: 4rem;
}
.c10k {
  font-size: 1.25rem;
}

#rand100000 {
  height: 5.5rem;
  width: 5.5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 23.5rem;
  top: 11rem;
  background-color: rgb(18, 98, 57);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
.c100k {
  font-size: 1.1rem;
}
#rand500000 {
  height: 5.5rem;
  width: 5.5rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 30.75rem;
  top: 11rem;
  background-color: rgb(249, 137, 0);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand1000000 {
  height: 6rem;
  width: 6rem;
  border: 2px solid black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 37.75rem;
  top: 11rem;
  background-color: rgb(190, 3, 252);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
.length1M {
  width: 6rem;
}
.vlength1M {
  height: 6rem;
}
.in1M {
  height: 4.5rem;
  width: 4.5rem;
}
.c1M {
  font-size: 1rem;
}
</style>
