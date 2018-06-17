const profilePicture = document.getElementById('profile-picture')
const user_id = document.currentScript.getAttribute('uid')

switch (level) {
	case 0:
		profilePicture.style.borderColor = '#9E9E9E'
		break
	case 1:
		profilePicture.style.borderColor = '#A0B0BF'
		break
	case 2:
		profilePicture.style.borderColor = '#7A3BE3'
		break
	case 3:
		profilePicture.style.borderColor = '#C01FD0'
		break
	default:
		profilePicture.style.borderColor = '#D44040'
		break
}

var userStatusRequest = new XMLHttpRequest()
userStatusRequest.open("POST", "/accounts/user_status/")
userStatusRequest.setRequestHeader("X-CSRFToken", csrf_token)
userStatusRequest.onreadystatechange = function() {
	if (userStatusRequest.readyState === 4 && userStatusRequest.status === 200) {
		var responseData = JSON.parse(userStatusRequest.responseText)
		var userStatus = responseData["status"]

		if (userStatus === false) {
			profilePicture.removeAttribute("style")
		}
		else {
			profilePicture.style.boxShadow = "0 0 0 3px #01FF70"
		}
	}
}
userStatusRequest.send("R@"+user_id)
setInterval(function() {
	let userStatusRequest = new XMLHttpRequest()
	userStatusRequest.open("POST", "/accounts/user_status/")
	userStatusRequest.setRequestHeader("X-CSRFToken", csrf_token)
	userStatusRequest.onreadystatechange = function() {
		if (userStatusRequest.readyState === 4 && userStatusRequest.status === 200) {
			var responseData = JSON.parse(userStatusRequest.responseText)
			var userStatus = responseData["status"]

			if (userStatus === false) {
				profilePicture.removeAttribute("style")
			}
			else {
				profilePicture.style.boxShadow = "0 0 0 3px #01FF70"
			}
		}
	}
	userStatusRequest.send("R@"+user_id)
}, 60000)
