<?php

// Adds an idea to the database

require "/home/mandel/public_html/lib/scripts/lib.php";

$ADD_QUERIES = Array(
	"add" => "INSERT INTO `Ideas`
	(`name`, `table_name`, `user`, `short_description`, `description`, `creation_time`, `share_email`, `notify_user`)
	VALUES
	(:idea_name,:table_name,:user_name,:short_desc,:long_desc,:creation_time,:share_email,:notify_user)",
	"create" => "CREATE TABLE :table_name (type TINYINT(1) DEFAULT 0, user VARCHAR(1000) DEFAULT NULL)",
	"select" => "SELECT `name` FROM `Ideas` WHERE `name`=:idea_name"
	);

function add() {
	// Adds the idea to the database
	global $REQUEST_ARGS, $ADD_QUERIES, $NOT_FOUND;
	$requestParameters = $REQUEST_ARGS;
	$authCode = getFromArray($requestParameters, "auth", "null");
	extract($REQUEST_ARGS);
	if (!validAuth(null, $authCode, 108803, 120563) | !validString($idea_name)) {
		die("Invalid Input or Malformed HTTP Request!");
		}
	$table_name = "IDEA_".str_replace(" ", "_", validateString($idea_name));
	$db = connectToDB("mandel_ideas", "mandel_innovator", "4A7i3v6V0ICtOvyAKKdc");
	$selectQuery = $db->prepare($ADD_QUERIES["select"]);
	$selectQuery->execute(Array(":idea_name" => $idea_name));
	if (getFromDatabase($selectQuery) === $NOT_FOUND) {
		$insertQuery = $db->prepare($ADD_QUERIES["add"]);
		$insertQuery->bindValue(":idea_name", $idea_name, PDO::PARAM_STR);
		$insertQuery->bindValue(":table_name", $table_name, PDO::PARAM_STR);
		$insertQuery->bindValue(":user_name", $user_name, PDO::PARAM_STR);
		$insertQuery->bindValue(":short_desc", $short_desc, PDO::PARAM_STR);
		$insertQuery->bindValue(":long_desc", $long_desc, PDO::PARAM_STR);
		$insertQuery->bindValue(":creation_time", date('m-d-Y H:i:s'), PDO::PARAM_STR);
		$insertQuery->bindValue(":share_email", intval($share_email), PDO::PARAM_INT);
		$insertQuery->bindValue(":notify_user", intval($notify_user), PDO::PARAM_INT);
		$insertQuery->execute();
		$createQuery = $db->prepare(str_replace(":table_name", $table_name, $ADD_QUERIES["create"]));
		$createQuery->execute();
		echo "Success";
		}
	else {
		die("Idea already exists!");
		}
	}
	
add();
	
?>