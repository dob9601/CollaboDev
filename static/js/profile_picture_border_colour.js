const profilePicture = document.getElementById('profile-picture')
const level = document.currentScript.getAttribute('tasks-completed')
const userLevel = Math.floor(parseInt(level) / 10)

switch (userLevel) {
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
