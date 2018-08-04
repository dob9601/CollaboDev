/* exported show_modal */

// eslint-disable-next-line camelcase
function show_modal (dataType, data) {
	const modalBox = document.getElementsByClassName('modal-box')[0]
	const modalText = modalBox.children[1]

	document.body.style.overflowY = 'hidden'

	if (dataType === 'task_data') {
		var taskStatus
		if (document.getElementById(data).children[7].innerHTML === 'True') {
			taskStatus = 'Open'
		} else {
			taskStatus = 'Closed'
		}
		modalText.innerHTML = '<h3 class="modal-header">' + document.getElementById(data).children[0].innerHTML + '</h3><hr>' +
					'<b>Description: </b>' + document.getElementById(data).children[1].innerHTML + '<br>' +
					'<b>Owner: </b>' + document.getElementById(data).children[2].innerHTML + '<br>' +
					'<b>Priority: </b>' + document.getElementById(data).children[3].innerHTML + '<br>' +
					'<b>Deadline: </b>' + document.getElementById(data).children[4].innerHTML + '<br>' +
					'<b>Size: </b> ' + document.getElementById(data).children[5].innerHTML + '<br>' +
					'<b>Age: </b>' + document.getElementById(data).children[6].innerHTML + '<br>' +
					'<b>Status: </b> ' + taskStatus + '<br>'
	} else if (dataType === 'create_task') {
		modalText.innerHTML = '<h3 class="modal-header">Create Task</h3><hr>' +
					'<form action="/tasks/submit/" method="post">' +
					'<input type="hidden" name="csrfmiddlewaretoken" value="' + data + '">' +
					'<label>Task Name: </label><br><input type="text" name="task_name" id="task_name" autocomplete="off"><br>' +
					'<label>Task Description: </label><br><input type="text" name="task_description" id="task_description" autocomplete="off"><br>' +
					'<label>Task Owner: </label><br><input type="text" name="task_owner" id="task_owner" autocomplete="off"><br>' +
					'<label>Task Priority: </label><br><select name="task_priority" id="task_priority" autocomplete="off">' +
					'	<option value="1">1</option>' +
					'	<option value="2">2</option>' +
					'	<option value="3">3</option>' +
					'	<option value="4">4</option>' +
					'	<option value="5" selected="selected">5</option>' +
					'	<option value="6">6</option>' +
					'	<option value="7">7</option>' +
					'	<option value="8">8</option>' +
					'	<option value="9">9</option>' +
					'	<option value="10">10</option>' +
					'</select><br>' +
					'<label>Task Size: </label><br><select name="task_size" id="task_size" autocomplete="off">' +
					'	<option value="1">XXS</option>' +
					'	<option value="2">XS</option>' +
					'	<option value="3">S</option>' +
					'	<option value="4" selected="selected">M</option>' +
					'	<option value="5">L</option>' +
					'	<option value="6">XL</option>' +
					'	<option value="7">XXL</option>' +
					'</select><br>' +
					'<label>Deadline: </label><br><input type="date" name="deadline_date" id="deadline_date" autocomplete="off"><br>' +
					'<input id="create-task-button" type="submit" value="Create" />' +
					'</form>'
	} else if (dataType === 'confirmation') {
		modalText.innerHTML = '<div class="buttons"><p>' + data[2] + '</p>' +
					'<button class="yes-button" onclick="document.getElementById(' + data[0] + ').children[8].children[' + data[1] + '].submit()">Yes</button>' +
					'<button class="no-button" onclick="document.getElementsByClassName(\'modal-box\')[0].style.display = \'none\'">No</button></div>'
	}
	modalBox.style.display = 'block'
}

var modal = document.getElementsByClassName('modal-box')[0]
