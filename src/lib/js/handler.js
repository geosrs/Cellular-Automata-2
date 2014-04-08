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
		move: function(delta) {
			// Moves the slides by "delta" amount
			var current = this.active;
			var new_slide = (current + delta);
			var length = this.slides.length;
			getElem(this.prev).disabled = (new_slide == 0);
			getElem(this.next).disabled = (new_slide == length - 1);
			var new_id = this.slides.get(new_slide % length);
			jQuery(getElem(this.slides.get(current).elem)).slideUp(250, function() {
				jQuery(getElem(new_id.elem)).slideDown(250);
				});
			new_id.initialize();
			this.active = new_slide;
			return new_slide;
			},
		};
	getElem(prev).disabled = true;
	return slides;
	}

function CAGrid(width, height, css_class) {
	// Creates a CAGrid object
	var grid = {
		hash: Date.now().toString(36),
		width: width,
		height: height,
		css_class: css_class,
		elements: new Array(),
		draw: function(id) {
			// Draws the elements to the document (or id's innerHTML)
			var elem = document.getElementById(id);
			var writeText = (exists(id) && exists(elem)) ? function(text) {elem.innerHTML += text;}: function(text) {document.write(text);}
			for (var h = 0; h < this.height; h ++) {
				for (var w = 1; w <= this.width; w ++) {
					var name = ((h * this.width) + w);
					var id = ["button", "grid", "object", this.hash, this.css_class, name].join("-");
					writeText(['<button class = ', this.css_class, ' id = ', id, ' name = ',  name, ' onclick = "ca_button_click(this);" buttonclicked="false"></button>'].join(""));
					this.elements.push(document.getElementById(id));
					}
				writeText('<br/>');
				}
			},
		clicked: function() {
			// Gets the clicked items
			var clicked_elems = this.elements.filter(
				function(elem, index, elem_array) {
					return elem.getAttribute('buttonclicked') == "true";
				});
			return clicked_elems.map(function(elem) {return parseInt(elem.name);});
			},
		};
	return grid;
	}

// Functions

function ca_button_click(elem) {
		// "Clicks" the element
		elem.setAttribute('buttonclicked', elem.getAttribute('buttonclicked') == "false");
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
	var options = {
		interest: ca_interest_grid.clicked(),
		};
	var elements = [].slice.call(document.getElementsByClassName('ca-opt'));
	elements.forEach(
		function(element, index, array) {
			options[(element.name != "") ? element.name: element.id] = element.value;
		});
	return options;
	}

function drawCA() {
	// Draws the Cellular Automata
	var options = getOptions();
	console.log(options);
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
	
String.prototype.replaceAll = function(substring, repl) {
	// Replaces "substring" with "repl" for all occurences of substring
	var pattern = new RegExp(substring, "g");
	return this.replace(pattern, repl);
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

function int(n) {
	// Extracts the integer number from n
	return parseInt(n.match(/\d+/)[0]);
	}

function float(n) {
	// Extracts a floating-pont number from n
	return parseFloat(n.match(/[0-9.]+\.[0-9]+/)[0]);
	}

function is_null(x) {
	// Checks whether or not the variable is null
	return (x == null || x == "undefined");
	}

function exists(x) {
	// Checks whether or not the value exists
	return (x != null && x != "undefined");
	}