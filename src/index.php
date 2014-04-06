<?php

// index.php

require "functions.php";

?>

<html>
	<head>
		<title><?php echo get_element("title"); ?></title> 
		<?php get_element("header"); ?>
	</head>
	<?php get_element("nav"); ?>
	<body>
		<div class = "margin-body" id = "body-div">
			<!-- Content goes here -->
		</div>
	</body>
	<?php get_element("footer"); ?>
</html>
