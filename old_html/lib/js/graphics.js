// graphics.js
// Rushy Panchal
// Copyright 2014
// Models Python's graphics.py

// Constants

var FILL = 0;
var STROKE = 1;
var RECT = 0;
var ARC = 1;
var TEXT = 2;
var LINE = 3;

// 140 Standard Web Colors + white + black
var COLORS = {gold: "#FFD700", firebrick: "#B22222", yellow: "#FFFF00", darkolivegreen: "#556B2F", 
	darkseagreen: "#8FBC8F", mediumvioletred: "#C71585", mediumorchid: "#BA55D3", chartreuse: 
	"#7FFF00", mediumslateblue: "#7B68EE", black: "#000000", springgreen: "#00FF7F", crimson: 
	"#DC143C", lightsalmon: "#FFA07A", brown: "#A52A2A", turquoise: "#40E0D0", olivedrab: 
	"#6B8E23", cyan: "#00FFFF", silver: "#C0C0C0", skyblue: "#87CEEB", gray: "#808080", darkturquoise:
	 "#00CED1", goldenrod: "#DAA520", darkgreen: "#006400", darkviolet: "#9400D3", darkgray: 
	"#A9A9A9", lightpink: "#FFB6C1", teal: "#008080", darkmagenta: "#8B008B", lightgoldenrodyellow: 
	"#FAFAD2", lavender: "#E6E6FA", yellowgreen: "#9ACD32", thistle: "#D8BFD8", violet: "#EE82EE", 
	navy: "#000080", orchid: "#DA70D6", blue: "#0000FF", ghostwhite: "#F8F8FF", honeydew: "#F0FFF0",
	 cornflowerblue: "#6495ED", darkblue: "#00008B", darkkhaki: "#BDB76B", indianred : "#CD5C5C", 
	mediumpurple: "#9370DB", cornsilk: "#FFF8DC", red: "#FF0000", bisque: "#FFE4C4", slategray: 
	"#708090", darkcyan: "#008B8B", khaki: "#F0E68C", wheat: "#F5DEB3", deepskyblue: "#00BFFF", 
	darkred: "#8B0000", steelblue: "#4682B4", aliceblue: "#F0F8FF", gainsboro: "#DCDCDC", 
	mediumturquoise: "#48D1CC", floralwhite: "#FFFAF0", coral: "#FF7F50", purple: "#800080", aqua: 
	"#00FFFF", lightcyan: "#E0FFFF", darksalmon: "#E9967A", beige: "#F5F5DC", azure: "#F0FFFF", 
	lightsteelblue: "#B0C4DE", oldlace: "#FDF5E6", greenyellow: "#ADFF2F", royalblue: "#4169E1", 
	lightseagreen: "#20B2AA", mistyrose: "#FFE4E1", sienna: "#A0522D", lightcoral: "#F08080", 
	orangered: "#FF4500", navajowhite: "#FFDEAD", lime: "#00FF00", palegreen: "#98FB98", burlywood:
	 "#DEB887", seashell: "#FFF5EE", mediumspringgreen: "#00FA9A", fuchsia: "#FF00FF", papayawhip: 
	"#FFEFD5", blanchedalmond: "#FFEBCD", peru: "#CD853F", aquamarine: "#7FFFD4", white: "#FFFFFF"
	, darkslategray: "#2F4F4F", tomato: "#FF6347", ivory: "#FFFFF0", dodgerblue: "#1E90FF", 
	lemonchiffon: "#FFFACD", chocolate: "#D2691E", orange: "#FFA500", forestgreen: "#228B22", 
	slateblue: "#6A5ACD", olive: "#808000", indigo  : "#4B0082", mintcream: "#F5FFFA", antiquewhite: 
	"#FAEBD7", darkorange: "#FF8C00", cadetblue: "#5F9EA0", moccasin: "#FFE4B5", limegreen: 
	"#32CD32", saddlebrown: "#8B4513", darkslateblue: "#483D8B", lightskyblue: "#87CEFA", deeppink:
	 "#FF1493", plum: "#DDA0DD", darkgoldenrod: "#B8860B", maroon: "#800000", sandybrown: 
	"#F4A460", magenta: "#FF00FF", tan: "#D2B48C", rosybrown: "#BC8F8F", pink: "#FFC0CB", lightblue:
	 "#ADD8E6", palevioletred: "#DB7093", mediumseagreen: "#3CB371", dimgray: "#696969", 
	powderblue: "#B0E0E6", seagreen: "#2E8B57", snow: "#FFFAFA", mediumblue: "#0000CD", 
	midnightblue: "#191970", paleturquoise: "#AFEEEE", palegoldenrod: "#EEE8AA", whitesmoke: 
	"#F5F5F5", darkorchid: "#9932CC", salmon: "#FA8072", lightslategray: "#778899", lawngreen: 
	"#7CFC00", lightgreen: "#90EE90", lightgray: "#D3D3D3", hotpink: "#FF69B4", lightyellow: "#FFFFE0"
	, lavenderblush: "#FFF0F5", linen: "#FAF0E6", mediumaquamarine: "#66CDAA", green: "#008000", 
	blueviolet: "#8A2BE2", peachpuff: "#FFDAB9", white: "#FFFFFF", black: "#000000"};

// Main classes
	
function GraphWin(id, userOptions) {
	/* GraphWin class
		Arguments:
			id - element ID of the canvas
			userOptions - object of options, supports:
				background (color of background)
	*/
	options = {
		background: "black",
		};
	var options = copy(userOptions, options);
	var canvas = document.getElementById(id);
	var graph = {
		id: id,
		canvas: canvas,
		context: canvas.getContext("2d"),
		config: {
			width: canvas.width,
			height: canvas.height,
			background: "#FFFFFF",
			font: "12px Calibri",
			fillStyle: "#000000",
			strokeStyle: "#000000",
			mouseX: 0,
			mouseY: 0,
			},
		transform: {
			exists: false,
			x1: 0,
			x2: 0,
			y1: 0,
			y2: 0,
			custom: function(x, y) {
				// Transforms pixels into custom coordinates
				return this.exists ? {
					x: (x / this.canvas.width) * (this.x2 - this.x1) + this.x1,
					y: (1 - y / this.canvas.height) * (this.y2 - this.y1) + this.y1,
					}: {x: x, y: y};
				},
			real: function(x, y) {
				// Transforms custom coordinates into real coordinates
				return this.exists ? {
					x: (x / (this.x2 - this.x1)) * this.canvas.width,
					y: (1 - y / (this.y2 - this.y1)) * this.canvas.height,
					}: {x: x, y: y};
				},
			distance: function(x1, y1, x2, y2) {
				// Returns the distance between two points (custom coordinates)
				return Math.sqrt((Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2)));
				},
			translate: function(width, height, radius) {
				// Translates width, height, and radius into real coordinates
				var transformed = this.real(radius, radius);
				return this.exists? {
					width: (this.x2 - this.x1) * width,
					height: (this.y2 - this.y1) * height,
					radius: this.distance(0, 0, transformed.x, transformed.y),
					}: {width: width, height: height, radius: radius};
				},
			},
		setCoords: function(x1, y1, x2, y2) {
			/* Sets the custom coordinates of the window, with (x1, y1) as the bottom left corner
			and (x2, y2) as the top right corner of the GraphWin
			*/
			this.transform.exists = true;
			this.transform.x1 = x1, this.transform.x2 = x2, this.transform.y1 = y1, this.transform.y2 = y2;
			this.transform.canvas = this.canvas;
			return this.transform;
			},
		resetCoords: function() {
			// Resets the custom coordinates to normal, pixel coordinates
			this.transform.exists = false;
			},
		setColor: function(color, method) {
			// Sets the current drawing color
			var method = exists(method) ? method: FILL;
			var hexColor = getColor(color);
			if (method == FILL) {
				var color = exists(hexColor) ? hexColor: this.context.fillStyle;
				this.context.fillStyle = color;
				this.config.fillStyle = color;
				}
			else {
				var color =  exists(hexColor) ? hexColor: this.context.strokeStyle;
				this.context.strokeStyle = color;
				this.config.strokeStyle = color;
				}
			return hexColor;
			},
		setFont: function(font, size) {
			// Sets the current font and size
			var font = size.toString() + "px " + font;
			this.context.font = font;
			this.config.font = font;
			return font;
			},
		setStyle: function(rule, value) {
			// Sets the CSS style of the GraphWin to value
			this.canvas.style[rule] = value;
			return value;
			},
		setBackground: function(color, force) {
			// Sets the background of the GraphWin
			var color = getColor(color);
			this.setStyle("background", color);
			this.config.background = color;
			(exists(force) && force) ? this.draw({x: 0, y: 0, width: this.getWidth(), 
				height: this.getHeight(), fill: color, outline: color, type: RECT}): null;
			return color;
			},
		getColor: function(type) {
			// Returns the current color
			return (type == FILL) ? this.context.fillStyle: this.context.strokeStyle;
			},
		clear: function () {
			// Clears the canvas
			this.context.clearRect(0, 0, this.config.width, this.config.height);
			this.setBackground(this.config.background);
			},
		plot: function(x, y, color) {
			// Colors the pixel (x, y) a specific color
			var color = exists(color) ? color: this.getColor(FILL);
			this.draw({x: x, y: y, width: 1, height: 1, type: RECT, fill: color, outline: color});
			},
		getHeight: function() {
			// Returns the height of the GraphWin
			return this.config.height;
			},
		getWidth: function() {
			// Returns the width of the GraphWin
			return this.config.width;
			},
		setHeight: function(height) {
			// Sets the GraphWin's height
			var height = exists(height) ? height: canvas.height;
			this.canvas.height = height;
			this.config.height = height;
			return height;
			},
		setWidth: function(width) {
			// Sets the GraphWin's width
			var width = exists(width) ? width: canvas.width;
			this.canvas.width = width;
			this.config.width = width;
			return width;
			},
		setMousePos: function(event) {
			// Gets the mouse position and sets it to the x and y coordinates
			var rect = this.canvas.getBoundingClientRect();
			this.config.mouseX = event.clientX - rect.left;
			this.config.mouseY = event.clientY - rect.top;
			return {
				x: this.config.mouseX,
				y: this.config.mouseY,
				};
			},
		getMouse: function() {
			// Gets the current mouse position
			var point = this.transform.custom(this.config.mouseX, this.config.mouseY);
			return {
				x: point.x,
				y: point.y,
				};
			},
		getData: function() {
			// Gets the Canvas data as a base64 encoded image
			return this.canvas.toDataURL("image/png");
			},
		setDownload: function(id) {
			// Sets the download link to the image data
			var elem = document.getElementById(id);
			elem.href = this.getData();
			return elem;
			},
		draw: function(obj) {
			// Draws the object to the GraphWin
			var type = obj.type;
			var point = this.transform.real(obj.x, obj.y);
			var transformed = this.transform.translate(obj.width, obj.height, obj.radius);
			if (type == RECT) {
				if (exists(obj.fill)) {
					this.setColor(obj.fill, FILL);
					this.context.fillRect(point.x, point.y, transformed.width, transformed.height);
					}
				if (obj.fill != obj.outline) {
					this.setColor(obj.outline, STROKE);
					this.context.strokeRect(point.x, point.y, transformed.width, transformed.height);
					}
				}
			else if (type == ARC) {
				if (exists(obj.fill)) {
					this.setColor(obj.fill, FILL);
					this.context.arc(point.x, point.y, transformed.radius, 0, 2 * Math.PI);
					this.context.fill();
					}
				if (obj.fill != obj.outline) {
					this.setColor(obj.outline, STROKE);
					this.context.arc(point.x, point.y, transformed.radius, 0, 2 * Math.PI);
					this.context.stroke();
					}
				}
			else if (type == TEXT) {
				this.setFont(obj.font, obj.size);
				if (exists(obj.fill)) {
					this.setColor(obj.fill, FILL);
					this.context.fillText(obj.text, point.x, point.y);
					}
				if (obj.fill != obj.outline) {
					this.setColor(obj.outline, STROKE);
					this.context.strokeText(obj.text, point.x, point.y);
					}
				}
			else if (type == LINE) {
				this.setColor(exists(obj.fill) ? obj.fill: obj.outline, STROKE);
				if (exists(obj.width)) {
					this.context.lineWidth = obj.width;
					}
				this.context.beginPath();
				this.context.moveTo(obj.x1, obj.y1);
				this.context.lineTo(obj.x2, obj.y2);
				this.context.stroke();
				this.context.closePath();
				}
			return obj;
			},
		};
	
	graph.setBackground(options.background);
	graph.setWidth(options.width);
	graph.setHeight(options.height);
	graph.canvas.addEventListener("mousemove", function(event) {
		graph.setMousePos(event);
		}, false);
	
	return graph;
	}
	
function GraphicsObject(options) {
	// Generic GraphicsObject (base for other classes)
	var obj = copy(options, {
		id: hex(Date.now()) + hex(Math.random().toString().replace('.', '')),
		graph: null,
		x: 0,
		y: 0,
		fill: null,
		outline: getColor("black"),
		draw: function(graphWin) {
			// Draws the object onto the graphWin
			graphWin.draw(this);
			this.graph = graph;
			},
		config: function(attribute, value) {
			// Sets the attribute to value
			this[attribute] = value;
			exists(this.graph) ? this.draw(this.graph): null;
			return value;
			},
		setFill: function(color) {
			// Sets the fill color of the object
			return this.config("fill", getColor(color));
			},
		setOutline: function(color) {
			// Sets the outline color of the object
			return this.config("outline", getColor(color));
			},
		});
	return obj;
	}
	
function Rectangle(x, y, width, height) {
	/* Rectangle class
	Options can be:
		x: left-most x value
		y: left-most y value
		width: width of rectangle
		height: height of rectangle
	*/
	var graphObj = new GraphicsObject({x: x, y: y, width: width, height: height});
	var rectangle = copy(graphObj, {
		type: RECT,
		width: 10,
		height: 10,
		});
	return rectangle;
	}
	
function Circle(x, y, radius) {
	/* Circle class
		options include:
			x - center of circle (x)
			y - center of circle (y)
			radius - radius of the circle
	*/
	var graphObj = new GraphicsObject({x: x, y: y, radius: radius});
	var circle = copy(graphObj, {
		type: ARC,
		radius: 10,
		});
	return circle;
	}
	
function Text(x, y, text, size, font) {
	/* Text class
		options include:
			x - left-most coordinate (x) of text
			y - left-most coordinate (y) of text
			text - text to display
			size - font size to display text in (in pixels)
			font - font family to use when displaying text
	*/
	var graphObj = new GraphicsObject({x: x, y: y, text: text, size: size, font: font});
	var text = copy(graphObj, {
		type: TEXT,
		text: "Hello, World!",
		size: 14,
		font: "Calibri",
		});
	return text;
	}
	
function Line(x1, y1, x2, y2) {
	/* Line class
		options include:
			x1 - x value of first coordinate
			y1 - y value of first coordinate
			x2 - x value of second coordinate
			y2 - y value of second coordinate
	*/
	var graphObj = new GraphicsObject({x1: x1, y1: y1, x2: x2, y2: y2});
	var line = copy(graphObj, {
		type: LINE,
		x1: 0,
		y1: 0,
		x2: 10,
		y2: 10,
		width: null,
		setWidth: function(width) {
			// Sets the width of the line
			return this.config("width", width);
			},
		});
	return line;
	}
	
// Miscellaneous functions
	
function color_rgb(r, g, b) {
	// Returns the color's (r, g, b) value in hex
	return (hex(r) + hex(g) + hex(b)).toUpperCase();
	}
	
function getColor(color) {
	// Attempts to get a color's hex value
	var hexColorAttempt = COLORS[color];
	var hexColor = exists(hexColorAttempt) ? hexColorAttempt: color;
	return hexColor;
	}
	