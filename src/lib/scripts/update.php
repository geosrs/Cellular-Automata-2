<?php

// Updates an idea in the database

require "/home/mandel/public_html/lib/scripts/lib.php";
	
$ACCEPTED_ATTRS = Array("name", "short_description", "description", "share_email", "notify_user");
	
function update() {
	// Updates the idea in the database
	global $REQUEST_ARGS, $ACCEPTED_ATTRS;
	$requestParameters = $REQUEST_ARGS;
	$authCode = getFromArray($requestParameters, "auth", null);
	if (!validAuth(null, $authCode, 73237, 287549) | !validString($idea_name)) {
		die("Invalid Input or Malformed HTTP Request!");
		}
	extract($REQUEST_ARGS);
	if (in_array($attribute, $ACCEPTED_ATTRS)) {
		$db = connectToDB("mandel_ideas", "mandel_innovator", "4A7i3v6V0ICtOvyAKKdc");
		$updateQuery = $db->prepare("UPDATE `Ideas` SET `$attribute`=:value WHERE `$search_attr`=:search_value");
		$updateQuery->bindValue(":value", $value, (is_string($value) ? PDO::PARAM_STR: PDO::PARAM_INT));
		$updateQuery->bindValue(":search_value", $search_value, PDO::PARAM_STR);
		$updateQuery->execute();
		echo "Updated!";
		}
	else {
		die("Attribute: $attribute cannot be updated!");
		}
	}
	
update();
	
?>