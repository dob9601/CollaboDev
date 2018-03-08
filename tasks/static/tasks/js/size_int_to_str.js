var scriptTag = document.getElementsByTagName('script')
var target = scriptTag[scriptTag.length - 1].parentNode.children[5]

var intSize = target.innerHTML
var size

if (intSize === '1') {
	size = 'XXS'
} else if (intSize === '2') {
	size = 'XS'
} else if (intSize === '3') {
	size = 'S'
} else if (intSize === '4') {
	size = 'M'
} else if (intSize === '5') {
	size = 'L'
} else if (intSize === '6') {
	size = 'XL'
} else if (intSize === '7') {
	size = 'XXL'
}
target.innerHTML = size
