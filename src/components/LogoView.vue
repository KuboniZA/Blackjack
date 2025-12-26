<script setup lang="ts">

</script>

<template>
  <div class="logo-container">
    <pre class="cards" id="card1">
    .------.
    |      |
    |      .-----.
    |     |K /\  |
    |     | /  \ |
    `-----| \  / |
          |  \/ K|
          `------'
    </pre>
    <pre class="cards" id="card2">

     A_  _
     ( \/ )
      \  /
       \/



    </pre>
    <pre class="character" id="b1">
       _
      | |
      | |__
      | '_ \
      | |_) |
      |_.__/
    </pre>
    <pre class="character" id="l">
       _
      | |
      | |
      | |
      | |
      |_|
    </pre>
    <pre class="character" id="a1">



      __ _
     / _` |
    | (_| |
     \__,_|
    </pre>
    <pre class="character" id="c1">



       ___
      / __|
     | (__
      \___|
    </pre>
    <pre class="character" id="k1">
       _
      | |
      | | __
      | |/ /
      |   <
      |_|\_\
    </pre>
    <pre class="character" id="j">
         _
        (_)
         _
        | |
        | |
        | |
       _/ |
      |__/
    </pre>
    <pre class="character" id="a2">



      __ _
     / _` |
    | (_| |
     \__,_|
    </pre>
    <pre class="character" id="c2">



       ___
      / __|
     | (__
      \___|
    </pre>
    <pre class="character" id="k2">
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
  #b1 { left: 12rem; color: purple; }
  #l { left: 16rem; }
  #a1 { left: 19rem; }
  #c1 { left: 22.5rem; }
  #k1 { left: 25.75rem; color: purple;}
  #j { left: 29rem; top: 0.5rem; }
  #a2 { left: 33rem; }
  #c2 { left: 36.5rem; }
  #k2 { left: 40rem; color: purple;}
  #card1 { top: -0.75rem; }
  #card2 { top: 0; color: red; }
</style>
