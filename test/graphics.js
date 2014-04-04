// graphics.js
// Rushy Panchal
// Copyright 2014
// Models Python's graphics.py

var FILL = "fill";
var STROKE = "stroke";

function GraphWin(id, userOptions) {
	// Creates a GraphWin Object
	options = {
		background: "black",
		};
	for (var option in userOptions) {
		options[option] = userOptions[option];
		}
	var canvas = document.getElementById(id);
	var graph = {
		canvas: canvas,
		draw: canvas.getContext("2d"),
		width: canvas.width,
		height: canvas.height,
		colors: {
			"black": "#000000",
			"white": "#FFFFFF",
			},
			
		setColor: function(color, method) {
			// Sets the current drawing color
			method = is_null(method) ? FILL: method;
			var hexColorAttempt = this.colors[color];
			var hexColor = is_null(hexColorAttempt) ? color: hexColorAttempt;
			if (method == FILL) {
				this.draw.fillStyle = is_null(hexColor) ? this.draw.fillStyle: hexColor;
				}
			else {
				this.draw.strokeStyle = is_null(hexColor) ? this.draw.strokeStyle: hexColor;
				}
			return hexColor;
			},
		
		setBackground: function(color) {
			// Changes the background color --- this will delete everything on the canvas
			this.setColor(color);
			this.draw.fillRect(0, 0, this.canvas.width, this.canvas.height);
			},
			
		clear: function () {
			// Clears the canvas
			this.draw.clearRect(0, 0, this.canvas.width, this.canvas.height);
			this.setBackground("white");
			},
			
		plot: function(x, y, color) {
			// Colors the pixel (x, y) a specific color
			this.setColor(color);
			this.draw.fillRect(x, y, 1, 1);
			},
			
		getHeight: function() {
			// Returns the height of the GraphWin
			return this.canvas.height;
			},
			
		getWidth: function() {
			// Returns the width of the GraphWin
			return this.canvas.width;
			},
			
		setHeight: function(height) {
			// Sets the GraphWin's height
			height = is_null(height) ? canvas.height: height;
			this.canvas.height = height;
			this.height = height;
			return height;
			},
			
		setWidth: function(width) {
			// Sets the GraphWin's width
			width = is_null(width) ? canvas.width: width;
			this.canvas.width = width;
			this.width = width;
			return width;
			},
		};
	
	graph.setBackground(options.background);
	graph.setWidth(options.width);
	graph.setHeight(options.height);
	
	return graph;
	}

function is_null(x) {
	// Checks whether or not the variable is null
	return x == null || x == "undefined";
	}
