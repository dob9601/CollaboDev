const completedTasks = parseInt(document.currentScript.getAttribute('tasks-completed'))
const level = Math.floor(completedTasks / 10)
const progressBar = document.getElementsByClassName('progress-bar')[0]

switch (level) {
case 0:
	progressBar.style.backgroundColor = '#9E9E9E'
	progressBar.parentNode.style.backgroundColor = '#F1F1F1'
	break
case 1:
	progressBar.style.backgroundColor = '#A0B0BF'
	progressBar.parentNode.style.backgroundColor = '#DDEEFF'
	break
case 2:
	progressBar.style.backgroundColor = '#7A3BE3'
	progressBar.parentNode.style.backgroundColor = '#B082FF'
	break
case 3:
	progressBar.style.backgroundColor = '#C01FD0'
	progressBar.parentNode.style.backgroundColor = '#F489FF'
	break
default:
	progressBar.style.backgroundColor = '#D44040'
	progressBar.parentNode.style.backgroundColor = '#FF9B9B'
	break
}

progressBar.style.width = String(((completedTasks % 10) / 10) * 100) + '%'
