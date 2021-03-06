<?php

// functions.php --- contains common functions

?>

<script type = "text/javascript">
	var DATA = <?php echo file_get_contents("lib/data.json"); ?>
</script>

<?php

$TITLE = "Cellular Automata Project";
$HOME_DIR = "http://mandeltech.com";

$HTML_LINKS = Array(
	"{main}" => "http://mandeltech.com",
	);

$PAGE_COLORS = Array(
	);
	
function get_element($element, $selector = null) {
	// Returns the specific element
	global $HTML_ELEMENTS, $PAGE_COLORS;
	$elementHTML = $HTML_ELEMENTS[$element];
	if (!is_null($selector)) {
		$page_colors = $PAGE_COLORS[$selector];
		echo $elementHTML.str_replace(
			Array('{selector}', '{primary-color}', '{secondary-color}'),
			Array($selector, $page_colors["primary"], $page_colors["secondary"]),
			'<style type = "text/css">
			.btn-custom {
				color: {primary-color};
				border-color: {primary-color};
				background: {secondary-color};
				}
			.btn-custom:hover {
				color: {secondary-color};
				background: {primary-color};
				}
		</style>');
		}
	else {
		echo $elementHTML;
		}
	}

function formatHTML($string) {
	// Formats the HTML
	global $HTML_LINKS;
	return str_replace(array_keys($HTML_LINKS), array_values($HTML_LINKS), $string);
	}

$HTML_HEADER = formatHTML(file_get_contents("lib/header.html"));
$HTML_NAV = formatHTML(file_get_contents("lib/nav.html"));
$HTML_NAV = ""; // no navigation menu for now
$HTML_FOOTER = formatHTML(file_get_contents("lib/footer.html"));

$HTML_ELEMENTS = Array(
	"header" => $HTML_HEADER,
	"nav" => $HTML_NAV,
	"footer" => $HTML_FOOTER,
	"title" => $TITLE,
	);

function getFromArray($array, $key, $default) {
	// Attempts to retrieve a value from an array, resorting to default if it does not exist
	return array_key_exists($key, $array) ? $array[$key]: $default;
	}

function create_buttons($classes) {
	// Automatically creates button styles
	$styles = "";
	foreach ($classes as $name => $options) {
		$primary = getFromArray($options, "primary", "black");
		$secondary = getFromArray($options, "secondary", "white");
		$styles .= ".$name, .$name:focus {
			color: $primary;
			border-color: $primary;
			background: $secondary;
			outline-color: $primary;
			}
			.$name:hover {
				color: $secondary;
				background: $primary;
				}
		";
		}
	echo $styles;
	}

?>