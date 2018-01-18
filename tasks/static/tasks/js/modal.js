function show_modal(data_type, data) {
	const modal_box = document.getElementsByClassName('modal-box')[0];
	const modal_text = modal_box.children[0].children[1];
	if (data_type == 'task_data') {
		if (data[6] == 'True') {
			task_status = "Open";
		}
		else {
			task_status = "Closed";
		}
		modal_text.innerHTML = '<h3 class="modal-header">'+data[1]+'</h3><br>' + 
					  '<b>Description: </b>'+data[2]+'<br>' +
					  '<b>Owner: </b>'+data[3]+'<br>' +
					  '<b>Priority: </b>'+data[4]+'<br>' +
	  				  '<b>Size: </b> '+document.getElementById(data[0]).children[3].innerHTML+'<br>' +
				 	  '<b>Age: </b>'+document.getElementById(data[0]).children[4].innerHTML+'<br>' +
	  				  '<b>Deadline: </b>'+data[5]+'<br>' +
				  	  '<b>Status: </b> '+task_status+'<br>'
		modal_box.style.display = 'block';
	}
	else if(data_type == 'create_task') {
		modal_text.innerHTML = '<h3>Create Task</h3>' +		
					  '<form action="/tasks/submit/" method="post">' +
					  "{% csrf_token %}" +
					  '<label>Task Name: </label><input type="text" name="task_name" id="task_name" autocomplete="off"><br>' +
					  '<label>Task Description: </label><input type="text" name="task_description" id="task_description" autocomplete="off"><br>' +
					  '<label>Task Owner: </label><input type="text" name="task_owner" id="task_owner" autocomplete="off"><br>' +
					  '<label>Task Priority: </label><select name="task_priority" id="task_priority" autocomplete="off">' +
					  '	<option value="1">1</option>' +
					  '	<option value="2">2</option>' +
					  '	<option value="3">3</option>' +
					  '	<option value="4">4</option>' +
					  '	<option value="5">5</option>' +
					  '	<option value="6">6</option>' +
					  '	<option value="7">7</option>' +
					  '	<option value="8">8</option>' +
					  '	<option value="9">9</option>' +
					  '	<option value="10">10</option>' +
					  '</select><br>' +
					  '<label>Task Size: </label><select name="task_size" id="task_size" autocomplete="off">' +
					  '	<option value="1">XXS</option>' +
					  '	<option value="2">XS</option>' +
					  '	<option value="3">S</option>' +
					  '	<option value="4" selected="selected">M</option>' +
					  '	<option value="5">L</option>' +
					  '	<option value="6">XL</option>' +
					  '	<option value="7">XXL</option>' +
					  '</select><br>' +
					  '<label>Deadline: </label><input type="date" name="deadline_date" id="deadline_date" autocomplete="off"><br>' +
					  '<input id="create-task-button" type="submit" value="Create" />' +
			  		  '</form>'
		modal_box.style.display = 'block';
	}
}

var modal = document.getElementsByClassName('modal-box')[0];
window.onclick = function(event) {
	if (event.target == modal) {
	        modal.style.display = "none";
	}
}
