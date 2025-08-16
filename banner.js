const slides = document.querySelectorAll('.banner-slide');
let current = 0;

function showSlide(index) {
  slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
}

function nextSlide() {
  current = (current + 1) % slides.length;
  showSlide(current);
}

// Show first slide immediately
showSlide(current);

// Rotate every 4 seconds
setInterval(nextSlide, 4000);
