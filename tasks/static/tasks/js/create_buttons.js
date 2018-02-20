var script_tag=document.getElementsByTagName('script');
var target=script_tag[script_tag.length - 1].parentNode.children[8].children[0].children[2];
var task_owner = document.currentScript.getAttribute('task-owner');
var current_user = document.currentScript.getAttribute('current-user');

if (task_owner=="") {
	target.value="Claim";
	target.style.backgroundColor="#2ECC40";
	target.style.cursor = 'pointer';
}
else {
	target.style.backgroundColor="#FF851B";
	target.style.cursor="not-allowed";
	target.disabled = true;
	if(task_owner == current_user) {
		target.value='Claimed by you';

		const unclaim_elements = document.getElementsByClassName('unclaim');
		const unclaim = unclaim_elements[unclaim_elements.length-1];
		const close_elements = document.getElementsByClassName('close-task');
		const close = close_elements[close_elements.length-1];
		unclaim.parentNode.style = 'display: inline';
		unclaim.style.backgroundColor = '#AAAAAA';
		unclaim.style.cursor = 'pointer';

		close.parentNode.style = 'display: inline';
		close.style.backgroundColor = '#2ECC40';
		close.style.cursor = 'pointer';

		target.style.webkitBorderRadius = '8px 8px 0 0';
		target.style.MozBorderRadius = '8px 8px 0 0';
		target.style.borderRadius = '8px 8px 0 0';

		unclaim.style.webkitBorderRadius = '0 0 8px 8px';
		unclaim.style.MozBorderRadius = '0 0 8px 8px';
		unclaim.style.borderRadius = '0 0 8px 8px';

		close.style.webkitBorderRadius = '0';
		close.style.MozBorderRadius = '0';
		close.style.borderRadius = '0';
	}
	else {
		target.value="Claimed by "+task_owner;
	}
}
