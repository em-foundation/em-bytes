window.onload = function() {
    let elist = document.querySelectorAll('.md-nav__title[for="__toc"]')
    elist.forEach(e => e.textContent = e.textContent.replace("Table of contents", "Articles"))
}
