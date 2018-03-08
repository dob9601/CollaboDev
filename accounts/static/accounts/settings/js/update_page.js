// eslint-disable-next-line no-unused-vars, camelcase
function update_page (slide) {
	const profile = document.getElementById('settings-profile')
	const account = document.getElementById('settings-account')
	const notifications = document.getElementById('settings-notifications')

	account.style.display = 'none'
	notifications.style.display = 'none'
	profile.style.display = 'none'

	document.getElementById(slide).style.display = 'table-cell'
}
