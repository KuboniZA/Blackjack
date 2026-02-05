<script lang="ts" setup>
defineProps({
  rand1: Boolean,
  rand5: Boolean,
  rand10: Boolean,
  rand25: Boolean,
  rand50: Boolean,
  rand100: Boolean,
  rand500: Boolean,
  rand1k: Boolean,
  rand10k: Boolean,
  rand50k: Boolean,
  rand100k: Boolean,
  rand500k: Boolean,
  rand1m: Boolean,
  rand10m: Boolean,
  rand100m: Boolean,
});
</script>

<template>
  <div class="chips-container">
    <div id="rand1" class="chips shimmer" v-if="rand1">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in1" class="inner-mask">
        <div id="i-dash1" class="inner-mask inner-dash">
          <span class="chip">1</span>
        </div>
      </div>
    </div>

    <div id="rand5" class="chips shimmer" v-if="rand5">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in5" class="inner-mask">
        <div id="i-dash5" class="inner-mask inner-dash">
          <span class="chip">5</span>
        </div>
      </div>
    </div>

    <div id="rand10" class="chips shimmer" v-if="rand10">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in10" class="inner-mask">
        <div id="i-dash10" class="inner-mask inner-dash">
          <span class="chip">10</span>
        </div>
      </div>
    </div>

    <div id="rand25" class="chips shimmer" v-if="rand25">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in25" class="inner-mask">
        <div id="i-dash25" class="inner-mask inner-dash">
          <span class="chip">25</span>
        </div>
      </div>
    </div>

    <div id="rand50" class="chips shimmer" v-if="rand50">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in50" class="inner-mask">
        <div id="i-dash50" class="inner-mask inner-dash">
          <span class="chip">50</span>
        </div>
      </div>
    </div>

    <div id="rand100" class="chips shimmer" v-if="rand100">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in100" class="inner-mask">
        <div id="i-dash100" class="inner-mask inner-dash">
          <span class="chip">100</span>
        </div>
      </div>
    </div>

    <div id="rand500" class="chips shimmer" v-if="rand500">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in500" class="inner-mask">
        <div id="i-dash500" class="inner-mask inner-dash">
          <span class="chip">500</span>
        </div>
      </div>
    </div>

    <div id="rand1000" class="chips shimmer" v-if="rand1k">
      <div class="horizontal-line" />
      <div class="vertical-line" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in1k" class="inner-mask">
        <div id="i-dash1000" class="inner-mask inner-dash">
          <span class="chip">1000</span>
        </div>
      </div>
    </div>

    <div id="rand10000" class="chips shimmer" v-if="rand10k">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in10k" class="inner-mask">
        <div id="i-dash10000" class="inner-mask inner-dash">
          <span class="chip c10k">10K</span>
        </div>
      </div>
    </div>

    <div id="rand50000" class="chips shimmer" v-if="rand50k">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in50k" class="inner-mask">
        <div id="i-dash50000" class="inner-mask inner-dash">
          <span class="chip c10k">50K</span>
        </div>
      </div>
    </div>

    <div id="rand100000" class="chips shimmer" v-if="rand100k">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in100k" class="inner-mask">
        <div id="i-dash100000" class="inner-mask inner-dash">
          <span class="chip c100k">100K</span>
        </div>
      </div>
    </div>

    <div id="rand500000" class="chips shimmer" v-if="rand500k">
      <div class="horizontal-line length10k" />
      <div class="vertical-line vlength10k" />
      <div class="left-leaning-line line30" />
      <div class="right-leaning-line line-30" />
      <div class="left-leaning-line line60" />
      <div class="right-leaning-line line-60" />
      <div id="in500k" class="inner-mask">
        <div id="i-dash500000" class="inner-mask inner-dash">
          <span class="chip c100k">500K</span>
        </div>
      </div>
    </div>

    <div id="rand1000000" class="chips shimmer" v-if="rand1m">
      <div class="horizontal-line length1M" />
      <div class="vertical-line vlength1M" />
      <div class="left-leaning-line line30 dlength1M" />
      <div class="right-leaning-line line-30 dlength1M" />
      <div class="left-leaning-line line60 dlength1M" />
      <div class="right-leaning-line line-60 dlength1M" />
      <div id="in1m" class="inner-mask">
        <div id="i-dash1000000" class="inner-mask inner-dash">
          <span class="chip c1M">1M</span>
        </div>
      </div>
    </div>

    <div id="rand10M" class="chips shimmer" v-if="rand10m">
      <div class="horizontal-line length1M" />
      <div class="vertical-line vlength1M" />
      <div class="left-leaning-line line30 dlength1M" />
      <div class="right-leaning-line line-30 dlength1M" />
      <div class="left-leaning-line line60 dlength1M" />
      <div class="right-leaning-line line-60 dlength1M" />
      <div id="in10m" class="inner-mask">
        <div id="i-dash10M" class="inner-mask inner-dash">
          <span class="chip c1M">10M</span>
        </div>
      </div>
    </div>

    <div id="rand100M" class="chips shimmer" v-if="rand100m">
      <div class="horizontal-line length1M" />
      <div class="vertical-line vlength1M" />
      <div class="left-leaning-line line30 dlength1M" />
      <div class="right-leaning-line line-30 dlength1M" />
      <div class="left-leaning-line line60 dlength1M" />
      <div class="right-leaning-line line-60 dlength1M" />
      <div id="in100m" class="inner-mask">
        <div id="i-dash100M" class="inner-mask inner-dash">
          <span class="chip c1M">100M</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.chips-container {
  position: relative;
  /* width: 45rem;
  height: 20rem;
  top: 38rem;
  left: 3rem;
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.8);

  border-radius: 25px; */
}

/* .chips-container {
  position: relative;
  width: 60rem;
  height: 40rem;
  top: 20rem;
  left: 3rem;
  border-radius: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(6px);
  border: 2px solid white;
  box-shadow:
     1px -1px 8px rgba(255, 255, 255, 1), inset 4px -4px 8px rgba(0, 0, 0, 0.4);
} */
#rand1 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 1.5rem;
  top: 3rem;
  background-color: rgb(199, 109, 52);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
.inner-mask {
  height: 6.5rem;
  width: 6.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background-color: white;
  /* box-shadow: -2px 4px 8px rgba(0, 0, 0, 0.4); */
  z-index: 5;
}
.inner-dash {
  height: 5.5rem;
  width: 5.5rem;
  box-shadow: none;
}
#i-dash1 {
  border: 1px dashed rgb(199, 109, 52);
  color: rgb(199, 109, 52);
}
#i-dash5 {
  border: 1px dashed rgb(57, 96, 137);
  color: rgb(57, 96, 137);
}
#i-dash10 {
  border: 1px dashed rgb(203, 83, 175);
  color: rgb(203, 83, 175);
}
#i-dash25 {
  border: 1px dashed rgb(68, 169, 61);
  color: rgb(68, 169, 61);
}
#i-dash50 {
  border: 1px dashed rgb(136, 19, 19);
  color: rgb(136, 19, 19);
}
#i-dash100 {
  border: 1px dashed rgb(57, 31, 189);
  color: rgb(57, 31, 189);
}
#i-dash500 {
  border: 1px dashed rgb(104, 7, 86);
  color: rgb(104, 7, 86);
}
#i-dash1000 {
  border: 1px dashed rgb(29, 104, 102);
  color: rgb(29, 104, 102);
}
#i-dash10000 {
  border: 1px dashed rgb(121, 120, 20);
  color: rgb(121, 120, 20);
}
#i-dash50000 {
  border: 1px dashed rgb(153, 130, 162);
  color: rgb(153, 130, 162);
}
#i-dash100000 {
  border: 1px dashed rgb(18, 98, 57);
  color: rgb(18, 98, 57);
}
#i-dash500000 {
  border: 1px dashed rgb(95, 56, 7);
  color: rgb(95, 56, 7);
}
#i-dash1000000 {
  border: 1px dashed rgb(87, 2, 116);
  color: rgb(87, 2, 116);
}
#i-dash10M {
  border: 1px dashed rgb(21, 3, 93);
  color: rgb(21, 3, 93);
}
#i-dash100M {
  border: 1px dashed rgb(166, 189, 18);
  color: rgb(166, 189, 18);
}
.chip {
  font-size: 2rem;
  font-weight: bold;
}
.horizontal-line {
  position: absolute;
  width: 8.5rem;
  height: 1rem;
  background-color: white;
}
.vertical-line {
  position: absolute;
  width: 1rem;
  height: 8.5rem;
  background-color: white;
}
.left-leaning-line {
  position: absolute;
  width: 1rem;
  height: 12.02rem;
  background-color: white;
}
.right-leaning-line {
  position: absolute;
  width: 1rem;
  height: 12.02rem;
  background-color: white;
}
.line30 {
  transform: rotate(30deg);
}
.line-30 {
  transform: rotate(-30deg);
}
.line60 {
  transform: rotate(60deg);
}
.line-60 {
  transform: rotate(-60deg);
}

#rand5 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 13rem;
  top: 3rem;
  background-color: rgb(57, 96, 137);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand10 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 24rem;
  top: 3rem;
  background-color: rgb(203, 83, 175);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand25 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 36.25rem;
  top: 3rem;
  background-color: rgb(68, 169, 61);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand50 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 48rem;
  top: 3rem;
  background-color: rgb(136, 19, 19);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand100 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 1.5rem;
  top: 16rem;
  background-color: rgb(57, 31, 189);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand500 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 13rem;
  top: 16rem;
  background-color: rgb(104, 7, 86);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand1000 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 24rem;
  top: 16rem;
  background-color: rgb(29, 104, 102);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}

#rand10000 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 36.25rem;
  top: 16rem;
  background-color: rgb(121, 120, 20);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand50000 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 48rem;
  top: 16rem;
  background-color: rgb(153, 130, 162);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}

#rand100000 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 1.5rem;
  top: 28rem;
  background-color: rgb(18, 98, 57);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand500000 {
  height: 8.5rem;
  width: 8.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 13rem;
  top: 28rem;
  background-color: rgb(95, 56, 7);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand1000000 {
  height: 8.5rem;
  width: 8.5rem;
  /* border: 2px solid black; */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 24rem;
  top: 28rem;
  background-color: rgb(133, 1, 177);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand10M {
  height: 8.5rem;
  width: 8.5rem;
  /* border: 2px solid black; */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 36.25rem;
  top: 28rem;
  background-color: rgb(21, 3, 93);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#rand100M {
  height: 8.5rem;
  width: 8.5rem;
  /* border: 2px solid black; */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  position: absolute;
  left: 48rem;
  top: 28rem;
  background-color: rgb(166, 189, 18);
  box-shadow: -4px 4px 8px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
#in1 {
  border: 0.5rem solid rgb(179, 105, 59);
}
#in5 {
  border: 0.5rem solid rgb(45, 75, 107);
}
#in10 {
  border: 0.5rem solid rgb(172, 70, 148);
}
#in25 {
  border: 0.5rem solid rgb(54, 134, 48);
}
#in50 {
  border: 0.5rem solid rgb(103, 14, 14);
}
#in100 {
  border: 0.5rem solid rgb(49, 27, 154);
}
#in500 {
  border: 0.5rem solid rgb(73, 5, 61);
}
#in1k {
  border: 0.5rem solid rgb(20, 72, 70);
}
#in10k {
  border: 0.5rem solid rgb(88, 87, 15);
}
#in50k {
  border: 0.5rem solid rgb(115, 97, 122);
}
#in100k {
  border: 0.5rem solid rgb(12, 65, 37);
}
#in500k {
  border: 0.5rem solid rgb(60, 35, 4);
}
#in1m {
  border: 0.5rem solid rgb(87, 2, 116);
}
#in10m {
  border: 0.5rem solid rgb(14, 2, 62);
}
#in100m {
  border: 0.5rem solid rgb(128, 146, 13);
}

.chips:hover {
  cursor: pointer;
  /* transform: scale(1.1); */
}

.shimmer::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;

  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.35) 50%,
    rgba(255, 255, 255, 0) 100%
  );

  opacity: 0;
  pointer-events: none;
}

.chips.shimmer::before {
  animation: shimmer-sweep 3s ease-out infinite;
}

@keyframes shimmer-sweep {
  0% {
    transform: translateX(0);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  50% {
    transform: translateX(200%);
    opacity: 1;
  }
  100% {
    transform: translateX(200%);
    opacity: 0;
  }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  .chips:hover.shimmer::before {
    animation: none;
  }
}
</style>
