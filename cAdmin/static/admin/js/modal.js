function show_modal(data, type) {
	const modal_box = document.getElementsByClassName('modal-box')[0];
	const modal_text = modal_box.children[0].children[1];

	if (type == 'new-user') {
		modal_text.innerHTML = '<h3>Create User</h3>' +
				       '<form action="create/" method="post">' +
				       '<input type="hidden" name="csrfmiddlewaretoken" value="'+data+'">' +
				       '<label>Username</label><input type="text" name="username" id="username" autocomplete="off"><br>' +
				       '<label>First Name</label><input type="text" name="first_name" id="first_name" autocomplete="off"><br>' +
				       '<label>Last Name</label><input type="text" name="last_name" id="last_name" autocomplete="off"><br>' +
				       '<label>Email Address</label><input type="text" name="email" id="email" autocomplete="off"><br>' +
				       '<input type="submit" value="Create User" id="create-user-button">' +
				       '</form>';
	}
	else if (type == 'show-pass') {
		modal_text.innerHTML = '<h2>Temporary password for new user:</h2>' +
				       '<p class="temp-pword">'+data+'</p>';
	}
	modal_box.style.display = 'block';
}


var modal = document.getElementsByClassName('modal-box')[0];
window.onclick = function(event) {
	if (event.target == modal) {
	        modal.style.display = 'none';
	}
};
