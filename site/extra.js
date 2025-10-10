window.onload = function() {
    let elist = document.querySelectorAll('.md-nav__title[for="__toc"]')
    elist.forEach(e => e.textContent = e.textContent.replace("Table of contents", "Contents"))
}

function screenSwap(curElem, newElem) {
    curElem.style.display = 'none'
    newElem.style.display = 'block'
    let newImg = newElem.querySelector('img')
    let newSrc = newImg.src
    newImg.src = ""
    newImg.src = newSrc
}

document.addEventListener('DOMContentLoaded', () => {
    const wrap = document.querySelector('.md-sidebar--primary .md-sidebar__scrollwrap')
    if (!wrap) return
    const logo = document.querySelector('a.md-header__button.md-logo')
    const href = logo ? logo.getAttribute('href') : '/'
    const div = document.createElement('div')
    div.className = 'emd-home'
    div.innerHTML = `<a class="emd-home__link" href="${href}">Home</a>`
    wrap.prepend(div)
})
