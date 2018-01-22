var script_tag = document.getElementsByTagName('script');
var target = script_tag[script_tag.length - 1].parentNode.children[6];
var publish_date = document.currentScript.getAttribute('task-publish-date');

var dD=Math.abs(new Date(publish_date).getTime()-new Date().getTime());
if(dD>172800000){
  target.innerHTML = String(Math.ceil(dD/(1000*60*60*24)))+" Days";
}
else if(dD>3600000) {
  target.innerHTML = String(Math.ceil(dD/(1000*60*60)))+" Hours";
}
else if(dD>60000) {
  target.innerHTML = String(Math.ceil(dD/(1000*60)))+" Minutes";
}
else if(dD<60000){
  target.innerHTML = "New";
}
