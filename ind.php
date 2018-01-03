<?php
session_start();
$output=null;
$a = $_SESSION['varname'];
#$a=$_POST['name'];
#$a="can_i_get_loan_?";
$a=str_replace(" ","_",$a);

$a1=exec("D:\movies\ana\python.exe D:\project_with_chitti\scripts\ch.py $a",$output);
#echo $a1;
echo json_encode($a1);
#var_dump($output);
?>