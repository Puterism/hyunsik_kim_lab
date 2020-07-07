window.addEventListener('scroll', toggleScrolledHeader);
window.addEventListener('load', toggleScrolledHeader);

function toggleScrolledHeader() {
    const header = document.querySelector('header');
    if (window.scrollY > 250) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
}


const menuToggleEl = document.querySelector('#menu-toggle');
const headerEl = document.querySelector('header');
const headerMiddleEl = document.querySelector('.header-middle');

menuToggleEl.onclick = function () {
    if (headerMiddleEl.classList.contains('menu-opened')) {
        headerMiddleEl.classList.remove('menu-opened');
        headerEl.classList.remove('menu-opened');
    } else {
        headerMiddleEl.classList.add('menu-opened');
        headerEl.classList.add('menu-opened');
    }
}
