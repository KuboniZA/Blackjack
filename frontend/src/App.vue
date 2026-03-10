<script setup lang="ts">
import { ref } from "vue";

// import ChipsView from "./components/ChipsView.vue";
import OneDeckGame from "./components/GameModes/OneDeckGame.vue";
import TableView from "./components/TableView.vue";
import WelcomeScreen from "./components/WelcomeScreen.vue";
import GameModes from "./components/GameModes/GameModes.vue";
// import TestView from "./components/TestView.vue";

type GameState = "welcome" | "modeSelect" | "betting" | "playing";

const state = ref<GameState>("welcome");

function startGame() {
  state.value = "modeSelect";

  const track = playlist.value[currentTrackIndex.value];

  if (audioPlayer.value && track) {
    audioPlayer.value.src = track.src;
    audioPlayer.value.play();
  }

  revealSpeaker();
  ToggleMute();
}
function selectOneDeck() {
  state.value = "betting";
}
function beginRound() {
  state.value = "playing";
}
function resetGame() {
  state.value = "welcome";
}

const audioPlayer = ref<HTMLAudioElement | null>(null);
const volume = ref(0.5);
const isMuted = ref<boolean>(true);

const playlist = ref([
  { title: "Claim To Fame", src: "/ClaimToFame-TheGreyRoom_ClarkSims.mp3" },
  { title: "In The Morning", src: "/InTheMorning-TheGreyRoom_ClarkSims.mp3" },
]);

const currentTrackIndex = ref(0);

const nextTrack = () => {
  if (!audioPlayer.value) return;

  currentTrackIndex.value = (currentTrackIndex.value + 1) % playlist.value.length;

  const track = playlist.value[currentTrackIndex.value];

  if (audioPlayer.value && track) {
    audioPlayer.value.src = track.src;
    audioPlayer.value.play();
  }
};

const updateVolume = () => {
  if (audioPlayer.value) {
    audioPlayer.value.volume = volume.value;
    if (isMuted.value && volume.value > 0) {
      isMuted.value = false;
      audioPlayer.value.muted = false;
    }
  }
};

const ToggleMute = () => {
  if (audioPlayer.value) {
    isMuted.value = !isMuted.value;
    audioPlayer.value.muted = isMuted.value;
  }
};

const showSpeaker = ref<boolean>(false);
const revealSpeaker = () => {
  showSpeaker.value = true;
};
</script>

<template>
  <div class="audio-control_container">
    <audio ref="audioPlayer" autoplay @ended="nextTrack"></audio>
    <button class="speaker" :class="{ 'hide-speaker': !showSpeaker }" @click="ToggleMute">
      {{ isMuted ? "🔇" : "🔊" }}
    </button>
  </div>

  <TableView />
  <OneDeckGame
    v-if="state === 'betting' || state === 'playing'"
    :playing="state === 'playing'"
    @betPlaced="beginRound"
    @roundOver="state = 'betting'"
    @reset="resetGame"
  />
  <WelcomeScreen v-if="state === 'welcome'" @play="startGame" />
  <GameModes v-if="state === 'modeSelect'" @oneDeck="selectOneDeck" @back="resetGame" />
  <!-- <ChipsView /> -->
  <!-- <TestView /> -->
  <RouterView />
</template>

<style scoped>
.speaker {
  position: absolute;
  font-size: 1.5rem;
  left: 4%;
  top: 5%;
  width: 3rem;
  height: 3rem;
  background: rgba(255, 255, 255, 0.606);
  border-radius: 50%;
  border: 2px solid white;
  z-index: 1000;
}
.speaker:hover {
  transform: scale(1.02);
  background: grey;
  cursor: pointer;
}
.hide-speaker {
  display: none;
}
</style>
