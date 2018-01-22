var script_tag=document.getElementsByTagName('script');
var target=script_tag[script_tag.length - 1].parentNode.children[5];


var int_size = target.innerHTML;
if (int_size=="1") {
	var size = "XXS";
}
else if (int_size=="2") {
	var size = "XS";
}
else if (int_size=="3") {
	var size = "S";
}
else if (int_size=="4") {
	var size = "M";
}
else if (int_size=="5") {
	var size = "L";
}
else if (int_size=="6") {
	var size = "XL";
}
else if (int_size=="7") {
	var size = "XXL";
}
target.innerHTML = size;
