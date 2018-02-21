function show_modal(data_type, data) {
	const modal_box = document.getElementsByClassName('modal-box')[0];
	const modal_text = modal_box.children[0].children[1];

	if (data_type == 'task_data') {
		if (document.getElementById(data).children[7].innerHTML == 'True') {
			task_status = "Open";
		}
		else {
			task_status = "Closed";
		}
		modal_text.innerHTML = '<h3 class="modal-header">'+document.getElementById(data).children[0].innerHTML+'</h3><br>' + 
					  '<b>Description: </b>'+document.getElementById(data).children[1].innerHTML+'<br>' +
					  '<b>Owner: </b>'+document.getElementById(data).children[2].innerHTML+'<br>' +
					  '<b>Priority: </b>'+document.getElementById(data).children[3].innerHTML+'<br>' +
	  				  '<b>Deadline: </b>'+document.getElementById(data).children[4].innerHTML+'<br>' +
	  				  '<b>Size: </b> '+document.getElementById(data).children[5].innerHTML+'<br>' +
				 	  '<b>Age: </b>'+document.getElementById(data).children[6].innerHTML+'<br>' +
				  	  '<b>Status: </b> '+task_status+'<br>';
	}
	else if(data_type == 'create_task') {
		modal_text.innerHTML = '<h3>Create Task</h3>' +		
					  '<form action="/tasks/submit/" method="post">' +
					  '<input type="hidden" name="csrfmiddlewaretoken" value="'+data+'">' +
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
			  		  '</form>';
	}
	else if(data_type == 'confirmation') {
		modal_text.innerHTML = '<div class="buttons"><p>'+data[2]+'</p>' +
				       '<button class = "yes-button" onclick="document.getElementById('+data[0]+').children[8].children['+data[1]+'].submit()">Yes</button>' +
				       '<button class = "no-button" onclick="document.getElementsByClassName(\'modal-box\')[0].style.display = \'none\'">No</button></div>';
	}
	modal_box.style.display = 'block';
}

var modal = document.getElementsByClassName('modal-box')[0];
window.onclick = function(event) {
	if (event.target == modal) {
	        modal.style.display = 'none';
	}
};
