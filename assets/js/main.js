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
    // 只在研究方向文章页面中为图片添加标题
    const researchContainer = document.querySelector('.research-article-container');
    if (!researchContainer) {
        return; // 如果不是研究方向文章页面，直接返回
    }
    
    // 只查找研究文章容器内的图片
    const images = researchContainer.querySelectorAll('img[alt]');
    
    images.forEach(img => {
        if (img.alt && img.alt.trim() !== '') {
            const caption = document.createElement('div');
            caption.className = 'image-caption';
            caption.textContent = img.alt;
            
            img.parentNode.insertBefore(caption, img.nextSibling);
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
