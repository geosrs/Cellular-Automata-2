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
		<button class = "btn btn-custom" onclick = 'slideOptions("options-sidebar")'><i class = "iconfont-40 ionicons ion-ios7-arrow-back"></i></button>
		<div class = "options-sidebar" id = "options-sidebar">
			<h2 class = "center" style = "color: blue;">Options</h2>
			<hr/>
			<div class = "options-pane">
				<div class = "center options-page" id = "options-page-cellspace" style = "display: inline;">
					<h3 class = "center opt-page-title">Cellspace</h3>
					<br/>
					<h4 class = "center">Width: <script type = "text/javascript"> addHint(DATA.options.width); </script></h4>
					<input type = "number" class = "ca-opt fixed-input form-control" name = "width" id = "options-cellspace-width" min = "1" value = "10"/>
					<br/>
					<h4 class = "center">Height: <script type = "text/javascript"> addHint(DATA.options.height); </script></h4>
					<input type = "number" class = "ca-opt fixed-input form-control" name = "height" id = "options-cellspace-height" min = "1" value = "1"/>
				</div>
				<div class = "center options-page" id = "options-page-neighborhood" style = "display: none;">
					<h3 class = "center opt-page-title">Cell Neighborhood</h3>
					<br/>
					<input type = "number" class = "fixed-input form-control" id = "options-neighborhood-size"/>
				</div>
				<div class = "center options-page" id = "options-page-interest" style = "display: none;">
					<h3 class = "center opt-page title">Cell of Interest <script type = "text/javascript"> addHint(DATA.options.interest); </script></h3>
					<br/>
					<div class = "center" id = "options-interest-grid">
					</div>
					<script type = "text/javascript">
						// need to preserve previous input (maybe have a way to dynamically turn on cells)
						// or maybe edit the height if the height changes
						function drawInterestGrid() {
							getElem('options-interest-grid').innerHTML = '';
							var cellspace_height = getElem('options-cellspace-height').value;
							window.ca_interest_grid = new CAGrid(3, (cellspace_height == 1) ? 1: 3, "ca-cell-button");
							ca_interest_grid.draw('options-interest-grid', ca_interest_grid.clicked(true));
							};
						drawInterestGrid();
					</script>
				</div>
				<div class = "center options-page" id = "options-page-rules" style = "display: none;">
					<h3 class = "center opt-page title">Rules <script type = "text/javascript"> addHint(DATA.options.rules); </script></h3>
					<br/>
					<button class = "center btn btn-custom" id = "options-new-rule" onclick = "addNewRule('options-rules');">Add Rule</button>
					<br/><br/>
					<iframe id = 'options-rules' class = "center" frameborder = "0" seamless>
					</iframe>
				</div>
			</div>
			<br/>
			<button class = "btn btn-previous" onclick = "pages.move(-1);" id = "opt-prev-button" style = "float: left;"><i class = "iconfont-20 ionicons ion-arrow-left-a"></i> Previous
			</button>
			<button class = "btn btn-next" onclick = "pages.move(1);" id = "opt-next-button" style = "float: right;">Next
			<i class = "iconfont-20 ionicons ion-arrow-right-a"></i>
			</button>
			<br/><br/>
			<center><button class = "btn btn-submit" onclick = "drawCA();" id = "opt-submit-button">Draw!</button></center>
			<script type = "text/javascript">
				var pageInits = {
					// Initializes a page as it loads
					cellspace: function() {
						getElem("options-cellspace-width").max = jQuery(window).width();
						getElem("options-cellspace-height").max = jQuery(window).height();
						},
					neighborhood: function() {
						},
					interest: function() {
						},
					rules: function() {
						document.maxCAHeight = getElem("options-cellspace-height").value;
						},
					};

				var pages = new Slides([
					{elem: "options-page-cellspace", initialize: pageInits.cellspace},
					// {elem: "options-page-neighborhood", initialize: pageInits.neighborhood},
					{elem: "options-page-interest", initialize: pageInits.interest},
					{elem: "options-page-rules", initialize: pageInits.rules},
					], "opt-next-button", "opt-prev-button");
			</script>
		</div>
		<div class = "margin-body" id = "body-div">
			<!-- Content goes here -->
		</div>
	</body>
	<script type = "text/javascript"> add_elements("automata"); </script>
	<?php get_element("footer"); ?>
</html>