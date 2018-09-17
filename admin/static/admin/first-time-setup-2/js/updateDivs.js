/* exported updateDivs */

const form = document.getElementById('main-form')
const divCount = form.children.length - 1
const progressBar = document.getElementsByClassName('prog-bar-inner')[0]

progressBar.style.width = String((1 / divCount) * 100) + '%'

function updateDivs (relativeDistance) {
  const form = document.getElementById('main-form')
  var currentPosition

  for (var i = 1; i < form.children.length; i++) {
    if (form.children[i].style.display !== 'none') {
      if ((i + relativeDistance < 1) || (i + relativeDistance > form.children.length - 1)) {
        return false
      }

      const nextButton = document.getElementsByClassName('buttons')[0].children[1]
      if (i + relativeDistance === form.children.length - 1) {
        nextButton.innerHTML = 'Submit'
        nextButton.onclick = function () {
          document.getElementById('main-form').submit()
        }
      } else {
        nextButton.innerHTML = 'Next'
        nextButton.onclick = function () {
          updateDivs(1)
        }
      }
      currentPosition = i
      progressBar.style.width = String(((currentPosition + relativeDistance) / divCount) * 100) + '%'
    }
    form.children[i].style.display = 'none'
  }
  form.children[currentPosition + relativeDistance].style.display = 'block'
}
