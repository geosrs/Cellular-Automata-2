// graphics.js
// Rushy Panchal
// Copyright 2014
// Models Python's graphics.py

function GraphWin(id, options) {
	// Creates a GraphWin Object
	canvas = document.getElementById(id);
	canvas.width = is_null(options.width) ? canvas.width: options.width;
	canvas.height = is_null(options.height) ? canvas.height: options.height;
	return {
		canvas: canvas,
		draw: this.canvas.getContext("2d"),
		setColor: function(color) {
			this.draw.fillStyle = color;
			}
		setBackground: function(color) {
			// Changes the background color
			this.setColor(color);
			this.draw.fillRect(0, 0, this.canvas.width, this.canvas.height);
			},
		plot: function(x, y, color) {
			// Colors the pixel (x, y) a specific color
			this.setColor(color);
			this.draw.fillRect(x, y, 1, 1);
			}
		};
	}

function is_null(x) {
	// Checks whether or not the variable is null
	return x == null || x == "undefined";
	}
