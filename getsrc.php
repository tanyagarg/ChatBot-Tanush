<?php
session_start();
	$var=$_SESSION['user_source'];
	//$var="hello";
	echo json_encode($var);
?>