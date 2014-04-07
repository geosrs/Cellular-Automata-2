<?php

// Automata

require "functions.php";

?>

<html>
	<head>
		<title><?php echo get_element("title"); ?></title> 
		<?php get_element("header"); ?>
	</head>
	<style type = "text/css">
		<?php create_buttons(Array(
				"btn-next" => Array("primary" => "green"),
				"btn-previous" => Array("primary" => "red"),
				"btn-submit" => Array("primary" => "blue"),
			)); 
		?>
	</style>
	<?php get_element("nav"); ?>
	<body>
		<button class = "btn btn-custom" onclick = 'var x = jQuery("#options-sidebar")[0]; x.style.left = (parseInt(x.style.left) < 0) ? 0: -400;'><i class = "iconfont-40 ionicons ion-ios7-arrow-back"></i></button>
		<div class = "options-sidebar" id = "options-sidebar">
			<h2 class = "center" style = "color: blue;">Options</h2>
			<hr/>
			<div class = "options-pane">
				<div class = "options-page" id = "options-page-cellspace" style = "display: inline;">
					<h3 class = "center opt-page-title">Cellspace</h3>
					<br/>
					<h4 class = "center">Width: <script type = "text/javascript"> addHint("This is the width (in rows) of the Cellular Automata grid"); </script></h4>
					<input type = "number" class = "fixed-input form-control" id = "options-cellspace-width" min = "1" value = "10"/>
					<br/>
					<h4 class = "center">Height: <script type = "text/javascript"> addHint("This is the height (in columns) of the Cellular Automata grid --- set the height to 1 for 1-dimensional Cellular Automata"); </script></h4>
					<input type = "number" class = "fixed-input form-control" id = "options-cellspace-height" min = "1" value = "1"/>
				</div>
				<div class = "options-page" id = "options-page-neighborhood" style = "display: none;">
					<h3 class = "center opt-page-title">Cell Neighborhood </h3>
					<br/>
					<input type = "number" class = "fixed-input form-control" id = "options-neighborhood-size"/>
				</div>
			</div>
			<script type = "text/javascript">
				function initPage(id) {
					// Initializes a page as it loads
					if (id == "cellspace") {
						getElem("options-cellspace-width").max = jQuery(window).width();
						getElem("options-cellspace-height").max = jQuery(window).height();
						}
					else if (id == "neighborhood") {
						}
					}

				var pages = new Slides([
					{"elem": "options-page-cellspace", "initialize": function() {initPage('cellspace')}},
					{"elem": "options-page-neighborhood", "initialize": function() {initPage('neighborhood')}},
					], "opt-next-button", "opt-prev-button");
			</script>
			<br/>
			<button class = "btn btn-previous" onclick = "moveSlide(pages, -1);" id = "opt-prev-button" style = "float: left;" disabled><i class = "iconfont-20 ionicons ion-arrow-left-a"></i> Previous
			</button>
			<button class = "btn btn-next" onclick = "moveSlide(pages, 1);" id = "opt-next-button" style = "float: right;">Next
			<i class = "iconfont-20 ionicons ion-arrow-right-a"></i>
			</button>
			<br/><br/>
			<center><button class = "btn btn-submit" onclick = "drawCA();" id = "opt-submit-button">Draw!</button></center>
		</div>
		<div class = "margin-body" id = "body-div">
			<!-- Content goes here -->
		</div>
	</body>
	<?php get_element("footer"); ?>
</html>