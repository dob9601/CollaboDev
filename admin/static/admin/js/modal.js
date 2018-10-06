/* exported showModal */

function showModal (data, type) {
  const modalBox = document.getElementsByClassName('modal-box')[0]
  const modalText = modalBox.children[1]

  document.body.style.position = 'fixed'
  document.body.style.overflowY = 'scroll'

  if (type === 'new-user') {
    modalText.innerHTML = '<h3>Create User</h3><hr>' +
                          '<form action="create/" method="post">' +
                          '<input type="hidden" name="csrfmiddlewaretoken" value="' + data + '">' +
                          '<label>Username</label><input type="text" name="username" id="username" autocomplete="off"><br>' +
                          '<label>First Name</label><input type="text" name="first_name" id="first_name" autocomplete="off"><br>' +
                          '<label>Last Name</label><input type="text" name="last_name" id="last_name" autocomplete="off"><br>' +
                          '<label>Email Address</label><input type="text" name="email" id="email" autocomplete="off"><br>' +
                          '<input type="submit" value="Create User" id="create-user-button">' +
                          '</form>'
  } else if (type === 'show-pass') {
    modalText.innerHTML = '<div class="pword-content"><h3>Temporary password for new user:</h3><hr>' +
                          '<b><p class="temp-pword">' + data + '</p></b>' +
                          '<p>Take note of this now, it will not be shown again.</p></div>'
  } else if (type === 'reset') {
    modalText.innerHTML = '<h3>Reset CollaboDev</h3><hr>' +
                          '<p>Are you sure you want to reset CollaboDev? (THIS ACTION CANNOT BE UNDONE)</p>' +
                          '<form action="/admin/reset_collabodev/" method="post">' +
                          '<input type="hidden" name="csrfmiddlewaretoken" value="' + data + '">' +
                          '<input type="submit" value="Yes">' +
                          '<input type="button" value="No" onclick="document.getElementsByClassName(\'modal-box\')[0].children[0].click()">' +
                          '</form>'
  } else if (type === 'update') {
    modalBox.children[0].style.display = 'hidden'
    modalText.innerHTML = '<h3>Updating CollaboDev</h3><hr>' +
                          '<img class="loading-image" src="/static/images/loading.gif">' +
                          '<p id="response-paragraph">Hang tight! CollaboDev is currently being updated</p>'

    var responseParagraph = document.getElementById('response-paragraph')

    var request = new XMLHttpRequest()
    request.open('POST', '/admin/update/')
    request.setRequestHeader('X-CSRFToken', data)
    request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        var response = JSON.parse(request.responseText)['response']
        if (response === 1) {
          responseParagraph.innerHTML = 'CollaboDev has been successfully updated. Please restart the server.'
          modalText.children[0].innerHTML = 'Updated CollaboDev'
        } else if (response === 2) {
          responseParagraph.innerHTML = 'CollaboDev is already running on the latest version.'
          modalBox.children[0].style.visibility = 'visible'
          modalText.children[0].innerHTML = 'Update Failed'
        } else if (response === -1) {
          responseParagraph.innerHTML = 'Could not reach the GitHub repository. Please try again later'
          modalBox.children[0].style.visibility = 'visible'
          modalText.children[0].innerHTML = 'Update Failed'
        }
        modalText.children[2].src = '/static/images/collabodev_logo.png'
      }
    }
    request.send()
  }
  modalBox.style.display = 'block'
}
