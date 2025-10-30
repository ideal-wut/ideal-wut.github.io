// Carousel functionality
let currentSlideIndex = 1;

function moveCarousel(n) {
    showSlide(currentSlideIndex += n);
}

function currentSlide(n) {
    showSlide(currentSlideIndex = n);
}

function showSlide(n) {
    const slides = document.querySelectorAll('.carousel-item');
    const indicators = document.querySelectorAll('.indicator');

    if (slides.length === 0) return;

    if (n > slides.length) { currentSlideIndex = 1 }
    if (n < 1) { currentSlideIndex = slides.length }

    slides.forEach(slide => slide.classList.remove('active'));
    indicators.forEach(indicator => indicator.classList.remove('active'));

    slides[currentSlideIndex - 1].classList.add('active');
    if (indicators.length > 0) {
        indicators[currentSlideIndex - 1].classList.add('active');
    }
}

// Auto-advance carousel
function autoAdvanceCarousel() {
    const carousel = document.querySelector('.carousel');
    if (carousel) {
        setInterval(() => {
            moveCarousel(1);
        }, 5000);
    }
}

// Mobile navigation toggle
function toggleNav() {
    const navMenu = document.querySelector('.nav-menu');
    navMenu.classList.toggle('active');
}

// Highlight active navigation item
function highlightActiveNav() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-item a');

    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (currentPath === linkPath || (currentPath.startsWith(linkPath) && linkPath !== '/')) {
            link.classList.add('active');
        }
    });
}

// Add image captions based on alt text
function addImageCaptions() {
    const images = document.querySelectorAll('img[alt]');
    
    images.forEach((img, index) => {
        if (img.alt && img.alt.trim() !== '') {
            // Check if caption already exists
            const nextElement = img.nextElementSibling;
            if (!nextElement || !nextElement.classList.contains('image-caption')) {
                const caption = document.createElement('div');
                caption.className = 'image-caption';
                caption.textContent = img.alt;
                
                // Insert after the image
                img.parentNode.insertBefore(caption, img.nextSibling);
            }
        }
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    showSlide(currentSlideIndex);
    autoAdvanceCarousel();
    highlightActiveNav();
    addImageCaptions();
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});
