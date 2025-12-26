<script setup lang="ts">
  import { ref, onMounted, onUnmounted } from 'vue';

  const asciiColour = ref<string>('black');
  const asciiColour1 = ref<string>('black');
  const asciiColour2 = ref<string>('black');
  const asciiColour3 = ref<string>('black');
  const asciiColour4 = ref<string>('black');

  const colours: string[] = ['red', 'green', 'blue', 'purple', 'orange', 'black'];
  const colours1: string[] = ['green', 'blue', 'purple', 'orange', 'black', 'red'];
  const colours2: string[] = ['blue', 'purple', 'orange', 'black', 'red', 'green'];
  const colours3: string[] = ['purple', 'orange', 'black', 'red', 'green', 'blue'];
  const colours4: string[] = ['orange', 'black', 'red', 'green', 'blue', 'purple'];

  let colourIndex = 0;
  let intervalId: number | undefined;

  const changeColour = (): void => {
    asciiColour.value = colours[colourIndex]!;
    colourIndex = (colourIndex + 1) % colours.length

    asciiColour1.value = colours1[colourIndex]!;
    colourIndex = (colourIndex + 1) % colours1.length

    asciiColour2.value = colours2[colourIndex]!;
    colourIndex = (colourIndex + 1) % colours2.length

    asciiColour3.value = colours3[colourIndex]!;
    colourIndex = (colourIndex + 1) % colours3.length

    asciiColour4.value = colours4[colourIndex]!;
    colourIndex = (colourIndex + 1) % colours4.length
  };

  onMounted (() => {
    intervalId = window.setInterval(changeColour, 1000)
  })

  onUnmounted(() => {
    if (intervalId !== undefined) {
      clearInterval(intervalId);
    }
  });

</script>

<template>
  <div class="main-container" />
  <div class="logo-container">
    <pre class="cards" id="card1">
    .------.
    |      |
    |      .-----.
    |     |      |
    |     |      |
    `-----|      |
          |      |
          `------'
    </pre>
    <pre class="cards" id="card2">

     A_  _
     ( \/ )
      \  /
       \/



    </pre>
    <pre class="cards" id="card3">



           K /\
            /  \
            \  /
             \/ K

    </pre>
    <pre class="character" id="b1" :style="{ color: asciiColour }">
       _
      | |
      | |__
      | '_ \
      | |_) |
      |_.__/
    </pre>
    <pre class="character" id="l" :style="{ color: asciiColour1 }">
       _
      | |
      | |
      | |
      | |
      |_|
    </pre>
    <pre class="character" id="a1" :style="{ color: asciiColour2 }">



      __ _
     / _` |
    | (_| |
     \__,_|
    </pre>
    <pre class="character" id="c1" :style="{ color: asciiColour3 }">



       ___
      / __|
     | (__
      \___|
    </pre>
    <pre class="character" id="k1" :style="{ color: asciiColour4 }">
       _
      | |
      | | __
      | |/ /
      |   <
      |_|\_\
    </pre>
    <pre class="character" id="j" :style="{ color: asciiColour3 }">
         _
        (_)
         _
        | |
        | |
        | |
       _/ |
      |__/
    </pre>
    <pre class="character" id="a2" :style="{ color: asciiColour2 }">



      __ _
     / _` |
    | (_| |
     \__,_|
    </pre>
    <pre class="character" id="c2" :style="{ color: asciiColour1 }">



       ___
      / __|
     | (__
      \___|
    </pre>
    <pre class="character" id="k2" :style="{ color: asciiColour }">
       _
      | |
      | | __
      | |/ /
      |   <
      |_|\_\
    </pre>
  </div>
</template>

<style scoped>
  .main-container { height: 10rem; width: 100%; background-color: darkgrey; position: absolute; left: 0; top: 0; box-shadow: 0 5px 12px 0.3px black;}
  .logo-container {
    height: 9rem;
    width: 50%;
    left: 25%;
    display: grid;
    grid-template-columns: 2fr 2fr repeat(9, 1fr);
    position: absolute;
    justify-content: center;
    align-items: center;
  }
  .character {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    position: absolute;
    font-weight: bold;
  }
  .cards {position: absolute; left: 2rem; }
  #b1 { left: 12rem; }
  #l { left: 16rem; }
  #a1 { left: 19rem; }
  #c1 { left: 22.5rem; }
  #k1 { left: 25.75rem; }
  #j { left: 29rem; top: 0.5rem; }
  #a2 { left: 33rem; }
  #c2 { left: 36.5rem; }
  #k2 { left: 40rem; color: }
  #card1 { top: -0.75rem; }
  #card2 { top: -1rem; color: red; }
  #card3 { top: -0.7rem; color: red; }
</style>
