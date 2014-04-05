<?php

require "/home/mandel/public_html/lib/scripts/lib.php";

$LIKE_QUERIES = Array(
	"add" => "INSERT INTO `:table_name`
	(`type`, `id`)
	VALUES
	(:type, :user_id)",
	"find" => "SELECT *
	FROM `:table_name`
	WHERE `id`=:user_id AND `type`=:type",
	"select" => "SELECT `:table_name`, `likes`, `dislikes`
	FROM `Ideas`
	WHERE `name`=:idea_name",
	"get" => "SELECT `ID`
	FROM `wp_users`
	WHERE `user_login`=:user_name",
	"updated" => "SELECT `likes`, `dislikes`
	FROM `Ideas`
	WHERE `name`=:idea_name",
	);

function like() {
	// "Likes" the idea
	global $REQUEST_ARGS, $LIKE_QUERIES, $NOT_FOUND;
	$requestParameters = $REQUEST_ARGS;
	$authCode = getFromArray($requestParameters, "auth", "null");
	extract($requestParameters);
	if (!validAuth(null, $authCode, 108553, 287239), !validateAll(Array($user, $idea, $type))) {
		die("Invalid Input or Malformed HTTP Request!");
		}
	$wp_database = connectToDB("mandel_wp73", "mandel_innovator", "4A7i3v6V0ICtOvyAKKdc");
	$idQuery = $wp_database->prepare($LIKE_QUERIES["get"]);
	$idQuery->bindValue(":user_name", $user, PDO::PARAM_STR);
	$idQuery->execute();
	$id = getFromDatabase($idQuery)["ID"];
	$database = connectToDB("mandel_ideas", "mandel_innovator", "4A7i3v6V0ICtOvyAKKdc");
	$selectQuery = $database->prepare($LIKE_QUERIES["select"]);
	$selectQuery->bindValue(":idea_name", $idea, PDO::PARAM_STR);
	$selectQuery->execute();
	$ideaData = getFromDatabase($selectQuery);
	$table_name = $ideaData["table_name"];
	$findQuery = $database->prepare(str_replace(":table_name", $table_name, $LIKE_QUERIES["find"]));
	$findQuery->bindValue(":user_id", $id, PDO::PARAM_INT);
	$findQuery->bindValue(":type", $type, PDO::PARAM_INT)
	$findQuery->execute();
	if (getFromDatabase($findQuery) != $NOT_FOUND) {
		// need to get previous likes/dislikes
		die(json_encode(Array("success" => false, "message" => "User has already liked", "likes" => $ideaData["likes"], "dislikes" => $ideaData["dislikes"])));
		}
	else {
		$addQuery = $database->prepare(str_replace(":table_name", $table_name, $LIKE_QUERIES["add"]));
		$addQuery->bindValue(":user_id", $id, PDO::PARAM_INT);
		$addQuery->bindValue(":type", $type, PDO::PARAM_INT);
		$addQuery->execute();
		$updateQuery = $database->prepare($LIKE_QUERIES["updated"]);
		$updateQuery->bindValue(":idea_name", $idea, PDO::PARAM_STR);
		$updateQuery->execute()l
		$ideaValues = getFromDatabase($updateQuery);
		echo json_encode(Array("success" => true, "message" => "Successfully liked", "likes" => $ideaValues["likes"], "dislikes" => $ideaValues["dislikes"]));
		}
	}
	
like();	

?>