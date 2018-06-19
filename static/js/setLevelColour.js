/* exported setLevelColour */

function setLevelColour (level) {
	const userLevel = Math.floor(parseInt(level) / 10)

	switch (userLevel) {
	case 0:
		return ['#9e9e9e', '#f1f1f1']
	case 1:
		return ['#a0b0Bf', '#ddeeff']
	case 2:
		return ['#7a3be3', '#b082ff']
	case 3:
		return ['#c01fd0', '#f489ff']
	default:
		return ['#d44040', '#ff9b9b']
	}
}
