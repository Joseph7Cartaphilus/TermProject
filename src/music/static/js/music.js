let soundButtons = document.querySelectorAll('.soundbutton'),
    audioElements = document.querySelectorAll('.audio'),
    headings = document.querySelectorAll('h4'),
    subheadings = document.querySelectorAll('h5');

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