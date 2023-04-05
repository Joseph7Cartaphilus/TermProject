const soundButtons = document.querySelectorAll('.soundbutton');
const audioElements = document.querySelectorAll('.audio');
const headings = document.querySelectorAll('h4');
const subheadings = document.querySelectorAll('h5');
const slider = document.querySelector('.slider');

let currentTrack = null;

soundButtons.forEach((soundButton, index) => {
    soundButton.addEventListener('click', e => {
        // check if another track is playing and pause it
        if (currentTrack && currentTrack.index !== index) {
            currentTrack.pause();
            headings[currentTrack.index].textContent = "Music";
            subheadings[currentTrack.index].textContent = "Music";
            soundButtons[currentTrack.index].classList.add('paused');
        }

        // play selected track
        if (audioElements[index].paused) {
            audioElements[index].play();
            headings[index].textContent = "Playing";
            subheadings[index].textContent = "Playing";
            soundButton.classList.remove('paused');
            currentTrack = audioElements[index];
            currentTrack.index = index;
        } else {
            audioElements[index].pause();
            headings[index].textContent = "Music";
            subheadings[index].textContent = "Music";
            soundButton.classList.add('paused');
            currentTrack = null;
        }
    })
});

slider.addEventListener('input', function() {
  let volume = this.value / 100;

  // проходимся по всем аудио элементам и устанавливаем им громкость
  audioElements.forEach(audio => {
    audio.volume = volume;
  });
});
