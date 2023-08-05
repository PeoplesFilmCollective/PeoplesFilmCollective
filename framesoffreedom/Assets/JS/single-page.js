const slider = document.querySelector('.slider');
const slidesContainer = document.querySelector('.slides-container');

// Duplicate images to create the infinite loop
slidesContainer.innerHTML += slidesContainer.innerHTML;

// Optional: If you want to pause the slider when the user hovers over it.
slider.addEventListener('mouseenter', () => {
  slider.style.animationPlayState = 'paused';
});

slider.addEventListener('mouseleave', () => {
  slider.style.animationPlayState = 'running';
});
