<?php
include_once("partnerconnect.php");
session_start();
$output=null;
$a=exec('D:\movies\ana\python.exe C:\xampp\htdocs\Chat\dijk.py',$output);


$arr=array("g_block"=>"1", "f_block"=>"2", "cos"=>"3","garden"=>"4", "lib_canteen"=>"5", "lib_gate"=>"6","workshop"=>"7", "library"=>"8", "e_block"=>"9");
$brr=array();
$i=1;
foreach ($output as $key) 
{
	$brr[$i]= $arr[$key];
	$i++;
}
$i=1;
$arr=array();
$all=[];
foreach($brr as $index)
{
	$qry = "SELECT  pth,name FROM place where id=$index";
	$records = mysql_query($qry);
	while($row=mysql_fetch_array($records))
	{
	$all[]=$row;
	//echo $row;
	}
	//echo 
	/*while ($row = mysql_fetch_assoc($records)) 
	{
    $arr[$i]=$row['pth'];
    $i++;
    }*/
    //echo $row['lastname'];
    //echo $row['address'];
    //echo $row['age'];
}
//$all=array_reverse($all);
$_SESSION['arr']=$all;

echo json_encode($all);
//echo json_encode($arr);
	//echo $records;
	//$i=mysql_num_rows($records);
	//echo $i;
	//$cc=mysqli_fetch_assoc($result);
    //echo $cc["name"];
	//$arr = array();
	//$arr[] = mysql_fetch_array($records);
	/*if (mysql_num_rows($result)>0) 
	{
    	while($row = $result->fetch_assoc()) 
    	{
        	header("Content-type: image/jpg");
        	echo " " . $row["image"]. "<br>";
    	}
	} */
	


?>