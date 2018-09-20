var scriptTag = document.getElementsByTagName('script')
var target = scriptTag[scriptTag.length - 1].parentNode.children[8].children[0].children[2]
var taskOwner = document.currentScript.getAttribute('task-owner')
var currentUser = document.currentScript.getAttribute('current-user')
var userAdmin = document.currentScript.getAttribute('user-admin')

if (taskOwner === 'None') {
    target.value = 'Claim'
    target.style.backgroundColor = '#2ECC40'
    target.style.cursor = 'pointer'
    if (userAdmin) {
        target.style.borderRadius = '8px 8px 0 0'
    }
} else {
    target.style.backgroundColor = '#FF851B'
    target.style.cursor = 'not-allowed'
    target.disabled = true
    if (taskOwner === currentUser) {
        target.value = 'Claimed by you'

        const unclaimElements = document.getElementsByClassName('unclaim')
        const unclaim = unclaimElements[unclaimElements.length - 1]
        const closeElements = document.getElementsByClassName('close-task')
        const close = closeElements[closeElements.length - 1]
        unclaim.parentNode.style = 'display: inline'
        unclaim.style.backgroundColor = '#AAAAAA'
        unclaim.style.cursor = 'pointer'

        close.parentNode.style = 'display: inline'
        close.style.backgroundColor = '#2ECC40'
        close.style.cursor = 'pointer'

        target.style.borderRadius = '8px 8px 0 0'
        close.style.borderRadius = '0'

        if (!userAdmin) {
            unclaim.style.borderRadius = '0 0 8px 8px'
        }
        else {
            unclaim.style.borderRadius = '0'
        }
    } else {
        target.value = 'Claimed by ' + taskOwner
        if (userAdmin) {
            target.style.borderRadius = '8px 8px 0 0'
        }
    }
}
