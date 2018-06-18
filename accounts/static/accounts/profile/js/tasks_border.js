/* global csrf_token */

const profilePicture = document.getElementById('profile-picture')
const userId = document.currentScript.getAttribute('uid')

var userStatusRequest = new XMLHttpRequest()
userStatusRequest.open('POST', '/accounts/user_status/')
userStatusRequest.setRequestHeader('X-CSRFToken', csrf_token)
userStatusRequest.onreadystatechange = function () {
	if (userStatusRequest.readyState === 4 && userStatusRequest.status === 200) {
		var responseData = JSON.parse(userStatusRequest.responseText)
		var userStatus = responseData['status']

		if (userStatus === false) {
			profilePicture.removeAttribute('style')
		} else {
			profilePicture.style.boxShadow = '0 0 0 3px #01FF70'
		}
	}
}
userStatusRequest.send('R@' + userId)
setInterval(function () {
	var userStatusRequest = new XMLHttpRequest()
	userStatusRequest.open('POST', '/accounts/user_status/')
	userStatusRequest.setRequestHeader('X-CSRFToken', csrf_token)
	userStatusRequest.onreadystatechange = function () {
		if (userStatusRequest.readyState === 4 && userStatusRequest.status === 200) {
			var responseData = JSON.parse(userStatusRequest.responseText)
			var userStatus = responseData['status']

			if (userStatus === false) {
				profilePicture.removeAttribute('style')
			} else {
				profilePicture.style.boxShadow = '0 0 0 3px #01FF70'
			}
		}
	}
	userStatusRequest.send('R@' + userId)
}, 60000)
