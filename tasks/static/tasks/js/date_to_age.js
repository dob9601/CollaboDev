var scriptTag = document.getElementsByTagName('script')
var target = scriptTag[scriptTag.length - 1].parentNode.children[7]

var publishDate = document.currentScript.getAttribute('task-publish-date')
var dateDifference = Math.abs(new Date(publishDate).getTime() - new Date().getTime())

if (dateDifference > 172800000) {
  target.innerHTML = String(Math.ceil(dateDifference / (1000 * 60 * 60 * 24))) + ' Days'
} else if (dateDifference > 3600000) {
  target.innerHTML = String(Math.ceil(dateDifference / (1000 * 60 * 60))) + ' Hours'
} else if (dateDifference > 60000) {
  target.innerHTML = String(Math.ceil(dateDifference / (1000 * 60))) + ' Minutes'
} else if (dateDifference < 60000) {
  target.innerHTML = 'New'
}
