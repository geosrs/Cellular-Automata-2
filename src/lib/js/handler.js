/*
Rushy Panchal
handler.js --- handles various event calls
*/

var ICONS = {
	loading: "iconfont-20 ionicons ion-loading-c",
	down: "iconfont-40 ionicons ion-ios7-arrow-down",
	up: "iconfont-40 ionicons ion-ios7-arrow-up"
	}
	
function httpGet(url) {
	// Gets data from a url
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", url, false);
	xmlHttp.send(null);
	return xmlHttp.responseText;
	}
	
function userLike(idea, auth, type) {
	httpPost(LIKE_URL, {
		idea: idea,
		auth: auth,
		user: 'test', // need to get WP user name somehow
		type: (type == "like") ? 1: 0,
		});
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
	var divElem = document.getElementById(id);
	if (divElem == null || divElem === "undefined") {
		return null;
		}
	var divElemOn = divElem.style.display != "none";
	divElemOn ? jQuery(divElem).slideUp(): jQuery(divElem).slideDown();
	return !divElemOn;
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
	
String.prototype.repeat = function(n) {
	// Repeats a string "n" times
	return new Array(n + 1).join(this);
	}
	