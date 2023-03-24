let soundButtons = document.querySelectorAll('.soundbutton'),
    audioElements = document.querySelectorAll('.audio'),
    subheadings = document.querySelectorAll('h5'),
    headings = document.querySelectorAll('h4');

let currentTrack = null;

soundButtons.forEach((soundButton, index) => {
    soundButton.addEventListener('click', e => {
        soundButton.classList.toggle('paused')
        if (audioElements[index].paused) {
            audioElements[index].play();
            headings[index].textContent = "Playing";
            subheadings[index].textContent = "Playing";
        } else {
            audioElements[index].pause();
            subheadings[index].textContent = "Music";
            headings[index].textContent = "Music";
        }
    })
});