<?php
session_start();
$var=$_SESSION['check_src_dest'];
echo json_encode($var);
?>