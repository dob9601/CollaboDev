// eslint-disable-next-line no-unused-vars, camelcase
function update_page (slide) {
	const settingsForm = document.getElementsByClassName('settings-form')[0]
	const children = settingsForm.children

	for (var i = 0; i < children.length - 1; i++) {
		if (children[i].nodeName === 'DIV') {
			children[i].style.display = 'none'
		}
	}

	document.getElementById(slide).style.display = 'table-cell'
}
