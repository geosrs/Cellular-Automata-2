<?php

// Program start page

require "functions.php";

?>

<html>
	<head>
		<title><?php echo get_element("title"); ?></title> 
		<?php get_element("header"); ?>
	</head>
	<?php get_element("nav"); ?>
	<body>
		<canvas id = "background-canvas" width = "200" height = "200" class = "canvas-back" >
		</canvas>
		<div class = "margin-body" id = "body-div">
			<!-- Content goes here -->
			<h2>Welcome to <?php echo $TITLE;?></h2>
			<br/>
			<a href = "index"><button class = "btn btn-custom">Home</button></a><br/><br/>
			<a href = "options"><button class = "btn btn-custom">
					Start&nbsp;&nbsp; <i class = "iconfont-20 fa fa-arrow-circle-o-right"></i>
			</button></a>
		</div>
	</body>
	<script type = "text/javascript">
		var graph = new GraphWin("background-canvas");
		graph.setBackground("white");
		graph.setWidth(jQuery(window).width());
		graph.setHeight(jQuery(window).height());
		graph.setColor(hex(Math.random()).substring(2, 8));
		var width = graph.getWidth();
		var height = graph.getHeight();
		var cellspace = "0".repeat(Math.floor(width / 2));
		cellspace = cellspace + "1" + cellspace;
		var y = 0;
		var pattern = new RegExp("100|010|001");
		var id = setInterval(function() {
			newcellspace = "";
			for (var x = 0; x <= width; x ++) {
				if (exists(cellspace.substring(x - 1, x + 2).match(pattern))) {
					graph.plot(x, y);
					newcellspace += "1";
					}
				else {
					newcellspace += "0";
					}
				}
			cellspace = newcellspace;
			if (y > height) {
				clearInterval(id);
				}
			else {
				y ++;
				}
			}, 1);
	</script>
	<?php get_element("footer"); ?>
</html>
