const slider = document.querySelector('.slider');
const slidesContainer = document.querySelector('.slides-container');
const images = slidesContainer.querySelectorAll('img');
const slideWidth = images[0].clientWidth;
const totalSlides = images.length;

// Optional: If you want to pause the slider when the user hovers over it.
slider.addEventListener('mouseenter', () => {
  slider.style.animationPlayState = 'paused';
});

slider.addEventListener('mouseleave', () => {
  slider.style.animationPlayState = 'running';
});

// Stop the animation after the last image in the original set
slider.addEventListener('animationiteration', () => {
  const currentTranslateX = parseFloat(window.getComputedStyle(slidesContainer).getPropertyValue('transform').split(',')[4]);
  const distanceToEnd = slideWidth * totalSlides - Math.abs(currentTranslateX);
  
  if (distanceToEnd < slideWidth) {
    // Reset the slider to the beginning
    slidesContainer.style.animation = 'none';
    slidesContainer.offsetHeight; // Trigger reflow to reset the animation
    slidesContainer.style.animation = 'scrollImages 20s linear infinite';
  }
});
