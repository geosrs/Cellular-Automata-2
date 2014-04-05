<?php

// Gets ideas from the database

require "/home/mandel/public_html/lib/scripts/lib.php";

$GET_QUERIES = Array(
	"get" => "SELECT
	`name`, `likes`, `dislikes`, `short_description`
	FROM `Ideas`
	WHERE `reserved`=0
	ORDER BY `:attribute` :order",
	"find" => "SELECT *
	FROM `Ideas`
	WHERE `:name` LIKE :value"
	);

function get() {
	// Gets ideas from the database
	global $REQUEST_ARGS, $GET_QUERIES;
	$requestParameters = $REQUEST_ARGS;
	$authCode = getFromArray($requestParameters, "auth", "null");
	if (!validAuth(null, $authCode, 78101, 168029) | !validString($idea_name)) {
		die("Invalid Input or Malformed HTTP Request!");
		}
	extract($REQUEST_ARGS);
	$db = connectToDB("mandel_ideas", "mandel_innovator", "4A7i3v6V0ICtOvyAKKdc");
	if ($action == "get") {
		$order = strtoupper($order);
		if ((in_array($attribute, Array("name", "likes", "dislikes"))) and (in_array($order, Array("DESC", "ASC"))) and (validateAll(Array($attribute, $order)))) {
			$queryString = str_replace(Array(":attribute", ":order"), Array($attribute, $order), $GET_QUERIES["get"]);
			if (!is_null($stop)) {
				$limit = intval($stop) - intval($start);
				$queryString.= " LIMIT $limit OFFSET $start";
				}
			$getQuery = $db->prepare($queryString);
			$getQuery->execute();
			echo json_encode($getQuery->fetchAll(PDO::FETCH_ASSOC));
			return true;
			}
		else {
			die("Sorting parameter: $attribute or direction: $order not supported!");
			}
		}
	else if ($action == "find") {
		if (validateAll(Array($name, $value))) {
			$addOn = is_string($value) ? "'": "";
			$addOn = ($exact != "true") ? $addOn."%": $addOn;
			$value = $addOn.$value.strrev($addOn);
			$queryString = str_replace(Array(":name", ":value"), Array($name, $value), $GET_QUERIES["find"]);
			$findQuery = $db->prepare($queryString);
			$findQuery->execute();
			$ideaData = $findQuery->fetch(PDO::FETCH_ASSOC);
			$keysToDelete = Array("share_email", "notify_user", "reserved", "table_name", "url");
			if (!$ideaData["share_email"]) {
				$keysToDelete[] = "user";
				}
			foreach ($keysToDelete as $index => $key) {
				unset($ideaData[$key]);
				}
			echo json_encode($ideaData);
			return true;
			}
		else {
			die("Invalid or malformed HTTP Request!");
			}
		}
	else {
		die("Action: $action not supported!");
		}
	echo "Success";
	}
	
get();

?>