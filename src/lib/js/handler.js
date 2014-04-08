/*
Rushy Panchal
handler.js --- handles various event calls
*/

// Constants

var ICONS = {
	loading: "iconfont-20 ionicons ion-loading-c",
	down: "iconfont-40 ionicons ion-ios7-arrow-down",
	up: "iconfont-40 ionicons ion-ios7-arrow-up"
	}
	
// Classes

function Slides(ids, next, prev) {
	// Creates a new Slides object
	var slides = {
		active: 0,
		slides: ids,
		next: next,
		prev: prev,
		add: function(ids) {
			// Adds an id to the list
			return (typeof ids == "string") ? this.slides.push(ids): this.slides.extend(ids);
			},
		};
	getElem(prev).disabled = true;
	return slides;
	}

function CAGrid(width, height, css_class) {
	// Creates a CAGrid object
	var grid = {
		width: width,
		height: height,
		css_class: css_class,
		elements: [],
		draw: function() {
			// Draws the elements to the document
			for (var h = 0; h < this.height; h ++) {
				for (var w = 1; w <= this.width; w ++) {
					var id = 'button-grid-object-' + this.css_class + '-' + ((h * this.width) + w);
					document.write('<button class = "{class}" id = {id} onclick = "ca_button_click(this);" buttonclicked="false"></button>'.replace('{id}', id).replace('{class}', this.css_class));
					this.elements.push(document.getElementById(id));
					}
				document.write('<br/>');
				}
			},
		clicked: function() {
			// Gets the clicked items
			return this.elements.filter(
				function(elem, index, elem_array) {
					return elem.getAttribute('buttonclicked') == "true";
				});
			},
		};
	return grid;
	}

// Functions

function ca_button_click(elem) {
		// "Clicks" the element
		elem.setAttribute('buttonclicked', elem.getAttribute('buttonclicked') == "false")
		}

function add_elements(page) {
	// Adds the element to the title
	document.title = DATA.title;
	if (page == "index") {
		}
	else if (page == "start") {
		}
	else if (page == "automata") {
		}
	return true;
	}

function httpGet(url) {
	// Gets data from a url
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", url, false);
	xmlHttp.send(null);
	return xmlHttp.responseText;
	}
	
function httpPost(url, parameters) {
	// Posts data to the url
	var form = document.createElement("form");
	form.setAttribute("method", "post");
	form.setAttribute("action", url);
	for (var key in parameters) {
		var field = document.createElement("input");
		field.setAttribute("type", "hidden");
		field.setAttribute("name", key);
		field.setAttribute("value", parameters[key]);
		form.appendChild(field);
		}
	document.body.appendChild(form);
	form.submit();
	}
	
function slideDiv(id) {
	// Slides a div up or down
	var divElem = getElem(id);
	if (divElem == null || divElem === "undefined") {
		return null;
		}
	var divElemOn = divElem.style.display != "none";
	divElemOn ? jQuery(divElem).slideUp(): jQuery(divElem).slideDown();
	return !divElemOn;
	}
	
function slideOptions(id) {
	// Slides the options menu
	var menu = getElem(id);
	menu.style.left = (parseInt(menu.style.left) < 0) ? 0: -400;
	return menu.style.left;
	}

function showGrouping(id) {
	// Shows the grouping
	var slided = slideDiv(id);
	var arrow = getElem(id + "-icon");
	arrow.className = slided ? ICONS.up: ICONS.down;
	}

function moveSlide(elements, delta) {
	// Shows the next slide
	var current = elements.active;
	var new_slide = (current + delta);
	var length = elements.slides.length ;
	getElem(elements.prev).disabled = (new_slide == 0);
	getElem(elements.next).disabled = (new_slide == length - 1);
	var new_id = elements.slides.get(new_slide % length);
	jQuery(getElem(elements.slides.get(current).elem)).slideUp(250, function() {
		jQuery(getElem(new_id.elem)).slideDown(250);
		});
	new_id.initialize();
	elements.active = new_slide;
	return new_slide;
	}

function addHint(text) {
	// Adds a hint around an icon
	document.write('<span class = "hint--rounded hint--top" data-hint = "' + text + '">\
		<i class = "iconfont-20 ionicons ion-help-circled"></i></span>');
	}

function getElem(id) {
	// Returns the element by its id
	return document.getElementById(id);
	}

function getOptions() {
	// Gets the user's options
	var options = {};
	var elements = document.getElementsByClassName("ca-opt");
	for (var index in elements) {
		var element = elements[index];
		options[element.name] = element.value;
		}
	return options;
	}

function drawCA() {
	// Draws the Cellular Automata
	var options = getOptions();
	}

function replaceAll(string, substring, repl) {
	// Replaces all occurences of the substring with repl in string
	var re = new RegExp(substring, 'g');
	return string.replace(re, repl);
	}
	
Array.prototype.get = function(index) {
	// Allows for index wrapping
	var length = this.length;
	var index = index % length;
	return index < 0 ? this[length + index]: this[index];
	}

Array.prototype.append = function(elem) {
	// Mocks Python's list.append
	return this.push(elem);
	}

Array.prototype.extend = function(new_array) {
	// Extends this array with new_array's items
	for (var index in new_array) {
		var elem = new_array[index];
		this.push(elem);
		}
	}
	
String.prototype.repeat = function(n) {
	// Repeats a string "n" times
	return new Array(n + 1).join(this);
	}
	
function copy(from, to) {
	// Copies the attributes in "from" and "to"
	for (var key in from) {
		if (from.hasOwnProperty(key) && exists(from[key])) {
			to[key] = from[key];
			}
		}
	return to;
	}
		
function hex(n) {
	// Returns the hex representation of decimal n
	return Number(n).toString(16);
	}

function is_null(x) {
	// Checks whether or not the variable is null
	return (x == null || x == "undefined");
	}

function exists(x) {
	// Checks whether or not the value exists
	return (x != null && x != "undefined");
	}