<?php
session_start();
$output=array();
#$message="e_block to library";
$message = $_SESSION['varname'];
$message=str_replace(' ', ';', $message);
//exec('D:\movies\ana\python.exe D:\project_with_chitti\scripts\b.py'.$message);
$message=exec("D:\movies\ana\python.exe D:\project_with_chitti\scripts\b.py $message");
//$x=exec('D:\movies\ana\python.exe D:\project_with_chitti\scripts\b.py',$message);
//echo ($message);
//echo ($message[0]);
//echo ($message[0]);
//echo "hiiiii";
$src="";
$dst="";
$chk="";
if($message[0]=='1')
{
	$i=2;
	$chk=1;
	
	while($message[$i]!=';')
	{
		$src=$src.$message[$i];
		$i++;
	}
	$i++;
	while($message[$i]!=';')
	{
		$dst=$dst.$message[$i];
		$i++;
	}
	$_SESSION['user_source']=$src;
	$_SESSION['user_dest']=$dst;
	
}
else if($message=="cafee" || $message=="admin" || $message=="rest" || $message=="hostels" || $message=="lib")	
{
	$chk=1;
	$_SESSION['user_dest']=$message;	
	$_SESSION['user_source']='1';
}
else
{
	$chk=0;
	$_SESSION['user_source']='1';
	$_SESSION['user_dest']='1';
}
$_SESSION['check_src_dest']=$chk;
echo json_encode("hiii");
//echo $_SESSION['user_source'];
//if($_SESSION['user_source']=='1') echo "hoiii";
//echo $_SESSION['user_dest']; 
//echo $_SESSION['check_src_dest'];
 
?>