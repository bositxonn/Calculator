// static/js/main.js
// Umumiy JavaScript - 1-kishi (Shamsiddin) yozadi

// Flash xabarlarini 4 soniyadan keyin avtomatik yashirish
document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelectorAll('.message');
    messages.forEach(function (msg) {
        setTimeout(function () {
            msg.style.opacity = '0';
            msg.style.transition = 'opacity 0.5s';
            setTimeout(function () { msg.remove(); }, 500);
        }, 4000);
    });
});
