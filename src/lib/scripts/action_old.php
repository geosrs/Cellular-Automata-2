<?php

$FILE_LOCATIONS = Array(
	"lib" => "../lib/scripts/lib.php";
	)

require $FILE_LOCATIONS["lib"];

function main() {
	// Main function
	global $NOT_FOUND;
	$requestParameters = $_POST;
	$scriptName = getFromArray($requestParameters, "action", null);
	if (is_null($scriptName)) {
		$requestParameters = $_GET;
		$scriptName = getFromArray($requestParameters, "action", null);
		if (is_null($scriptName)) {
			die("No action provided!");
			}
		}
	$returnValue = call($scriptName, $requestParameters);
	if ($returnValue === $NOT_FOUND) {
		die("Action not found!");
		}
	else {
		if (is_array($returnValue)) {
			echo json_encode($returnValue);
			}
		else {
			echo $returnValue;
			}
		};
	return null;
	}
	
function call($script, $arguments) {
	// Calls the function with the provided arguments
	global $ACTION_FUNCTIONS, $NOT_FOUND;
	$functionName = $ACTION_FUNCTIONS[$script];
	if (is_null($functionName)) {
		return $NOT_FOUND;
		}
	else {
		foreach ($arguments as $arg => $value) {
			if (!validString(arg) | !validString(value)) {
				die("Invalid Input!");
				}
			}
		$db = connectToDB("mandel_ideahacker", "mandel_hackener", "IgTMijKvp2qAgr898qof"); // need to make a new user with a new password
		return $functionName($db, $arguments);
		}
	}

function addIdea($db, $arguments) {
	// Adds an idea to the database
	extract($arguments);
	$insertQuery = $db->prepare("INSERT INTO `Ideas`
	(`idea`, `user`, `short_description`, `description`, `likes`, `dislikes`, `creation_time`, `url`, `views`, `code`)
	VALUES
	(:idea_name,:user_name,:short_desc,:long_desc,0,0,:creation_time,:idea_url, 0,:code)");
	$insertQuery->execute(Array(
		":idea_name" => $idea_name, ":user_name" => $user_name, ":short_desc" => $short_desc,
		":long_desc" => $long_desc, ":creation_time" => date('m-d-Y H:i:s'), ":idea_url" => "", ":code" => ""));
	return true;
	}
	
function getIdeas($db, $arguments) {
	// Gets a specific range of ideas
	extract($arguments);
	$limit = $stop - $start;
	if ($limit == "all") {
		$selectQuery = $db->prepare("SELECT
		`idea`, `likes`, `dislikes`, `views`
		FROM `Ideas`
		WHERE `reserved` != 1
		ORDER BY `$attr` DESC");
		}
	else {
		$selectQuery = $db->prepare("SELECT
		`idea`, `short_description`, `likes`, `dislikes`, `views`
		FROM `Ideas`
		WHERE `reserved` != 1
		ORDER BY `$attr` DESC
		LIMIT $limit OFFSET $start");
		}
	$selectQuery->execute();
	return $selectQuery->fetchAll(PDO::FETCH_ASSOC);
	}
	
function findIdea($db, $arguments) {
	// Finds an idea from the database
	extract($arguments);
	$selectQuery = $db->prepare("SELECT * FROM `Ideas`
	WHERE `$name` LIKE :attr_value");
	$selectQuery->execute(Array(":attr_value" => "%".$value."%"));
	return $selectQuery->fetchAll(PDO::FETCH_ASSOC);
	}
	
function incrementIdea($db, $arguments) {
	// Increments data in the database
	extract($arguments);
	$updateQuery = $db->prepare("UPDATE `Ideas`
	SET `$attribute`=`$attribute`+1 WHERE `$search_attr`=:search_value");
	echo "UPDATE `Ideas`
	SET `$attribute`=`$attribute`+1 WHERE `$search_attr`=$search_value";
	$updateQuery->execute(Array(":search_value" => $search_value));
	}
	
function updateAttr($db, $arguments) {
	// Updates data in the database
	extract($arguments);
	$updateQuery = $db->prepare("UPDATE `Ideas`
	SET `$attribute`=$value WHERE `$search_attr`=:search_value");
	$updateQuery->execute(Array(":search_value" => $search_value));
	}
	
$ACTION_FUNCTIONS = Array(
	"add" => addIdea,
	"find" => findIdea,
	"get" => getIdeas,
	"update" => updateAttr,
	"increment" => incrementIdea
	);
	
main();

?>