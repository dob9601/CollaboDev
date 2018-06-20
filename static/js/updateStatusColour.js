/* exported updateStatusColour */
/* global CSRF_TOKEN */

function updateStatusColour (userID, target) {
	var request = new XMLHttpRequest()
	request.open('POST', '/accounts/user_status/')
	request.setRequestHeader('X-CSRFToken', CSRF_TOKEN)
	request.onreadystatechange = function () {
		if (request.readyState === 4 && request.status === 200) {
			var response = JSON.parse(request.responseText)['status']

			if (response === true) {
				target.style.boxShadow = '0 0 0 3px #01FF70'
			} else {
				target.removeAttribute('style')
			}
		}
	}
	request.send('R@' + userID)
}
