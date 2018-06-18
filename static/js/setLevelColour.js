function setLevelColour (level) {
	const userLevel = Math.floor(parseInt(level) / 10)

	switch (userLevel) {
	case 0:
		return '#9E9E9E'
	case 1:
		return '#A0B0BF'
	case 2:
		return '#7A3BE3'
	case 3:
		return '#C01FD0'
	default:
		return '#D44040'
	}
}
