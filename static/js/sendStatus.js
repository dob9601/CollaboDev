/* global CSRF_TOKEN */

var sessionKey = document.currentScript.getAttribute('session-key')

function sendStatus () {
  var request = new XMLHttpRequest()
  request.open('POST', '/accounts/user_status/')
  request.setRequestHeader('X-CSRFToken', CSRF_TOKEN)
  request.send('U@' + sessionKey)
}

sendStatus()
setInterval(sendStatus, 30000)
