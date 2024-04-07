var audio = document.getElementById("audioPlayer");
const seekbar = document.getElementById("seekbar");
const volumebar = document.getElementById("volumebar");
const playButton = document.getElementById("controller-b");
const volumeButton = document.getElementById("controller-v");
const currentTime = document.getElementById("currentTime");
const fullTime = document.getElementById("fullTime");
const Multiplier = 1000;
var vv = 0;
volumebar.setAttribute("max", Multiplier);
volumebar.setAttribute("value", Multiplier);
audio.addEventListener("loadedmetadata", () => {
  seekbar.setAttribute("max", audio.duration * Multiplier);
  fullTime.textContent = formatTime(audio.duration);
});

seekbar.addEventListener("input", () => {
  smoothSeek(seekbar.value);
});

function smoothSeek(value) {
  const originalTime = value / Multiplier;
  audio.currentTime = originalTime;
}

audio.addEventListener("timeupdate", () => {
  seekbar.value = audio.currentTime * Multiplier;
  currentTime.textContent = formatTime(audio.currentTime);
});

volumebar.addEventListener("input", () => {
  audio.volume = volumebar.value / Multiplier;
  if (volumeButton.classList.contains("fa-volume-mute")) {
    volumeButton.className = "fas fa-volume-up";
  } else if (
    volumeButton.classList.contains("fa-volume-up") &&
    audio.volume === 0
  ) {
    volumeButton.className = "fas fa-volume-mute";
  }
});

volumeButton.addEventListener("click", () => {
  if (audio.volume === 0 && vv === 0) {
    audio.volume = 0.8;
    volumebar.value = 800;
    volumeButton.className = "fas fa-volume-up";
  } else if (audio.volume === 0) {
    audio.volume = vv / Multiplier;
    volumebar.value = vv;
    vv = 0;
    volumeButton.className = "fas fa-volume-up";
  } else {
    vv = volumebar.value;
    audio.volume = 0;
    volumebar.value = 0;
    volumeButton.className = "fas fa-volume-mute";
  }
});

playButton.addEventListener("click", () => {
  if (audio.paused) {
    audio.play();
    playButton.className = "fas fa-pause";
  } else {
    audio.pause();
    playButton.className = "fas fa-play";
  }
});

function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.floor(seconds % 60);
  return `${minutes < 10 ? "0" : ""}${minutes}:${
    remainingSeconds < 10 ? "0" : ""
  }${remainingSeconds}`;
}
