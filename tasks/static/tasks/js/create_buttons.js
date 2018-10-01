const taskList = document.getElementsByClassName('open-task')
const userAdmin = document.getElementById('user-info').getAttribute('is_admin')
const currentUser = document.getElementById('user-info').getAttribute('username')

for (var i = 0; i < taskList.length; i++) {
  var currentTask = taskList[i]

  var taskOwner = currentTask.getElementsByClassName('task-owner')[0].innerHTML

  var claimButton = currentTask.getElementsByClassName('claim-button')[0]
  var closeButton = currentTask.getElementsByClassName('close-button')[0]
  var unclaimButton = currentTask.getElementsByClassName('unclaim-button')[0]

  if (taskOwner !== 'None') {
    claimButton.style.backgroundColor = '#ff851b'
    claimButton.style.cursor = 'not-allowed'
    claimButton.disabled = true
    if (taskOwner === currentUser) {
      claimButton.value = 'Claimed by you'

      unclaimButton.parentNode.style = 'display: inline'
      unclaimButton.style.backgroundColor = '#AAAAAA'
      unclaimButton.style.cursor = 'pointer'

      closeButton.parentNode.style = 'display: inline'
      closeButton.style.backgroundColor = '#2ECC40'
      closeButton.style.cursor = 'pointer'

      closeButton.style.borderRadius = '0'

      if (!userAdmin) {
        unclaimButton.style.borderRadius = '0 0 8px 8px'
      } else {
        unclaimButton.style.borderRadius = '0'
      }
    } else {
      claimButton.value = 'Claimed by ' + taskOwner
      if (userAdmin) {
        claimButton.style.borderRadius = '8px 8px 0 0'
      }
    }
  }
}
