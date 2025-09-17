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