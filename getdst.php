<?php
session_start();
	$var=$_SESSION['user_dest'];
	echo json_encode($var);
?>