var instanse = false;
var state;
var mes;
var file;
var src;
var dst;
var cafe=[];
var admin=[];
var hostel=[];
var rest=[];
var stdy=[];
var chkpth;
function Chat () {
	alert('helo! Welcome');
    this.update = updateChat;
    this.send = sendChat;
	this.getState = getStateOfChat;
}

//gets the state of the chat
function getStateOfChat(){
	if(!instanse){
		 instanse = true;
		 $.ajax({
			   type: "POST",
			   url: "process.php",
			   data: {  
			   			'function': 'getState',
						'file': file
						},
			   dataType: "json",
			
			   success: function(data){
			  	   state = data.state;
				   instanse = false;
			   },
			});
	}	 
}

//Updates the chat
function updateChat(){
	
	 if(!instanse){
		 instanse = true;
	     $.ajax({
			   type: "POST",
			   url: "process.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success: function(data){

				   if(data.text){
				   	
						for (var i = 0; i < data.text.length; i++) {

							 $('#chat-area').append($("<p>"+ data.text[i] +"</p>"));
                        }								  
				   }
				   document.getElementById('chat-area').scrollTop = document.getElementById('chat-area').scrollHeight;
				   instanse = false;
				   state = data.state;
			   },
			});
	 }
	 else {
		 setTimeout(updateChat, 1500);
	 }
	
}
function getChat(){
	//alert("ummmmmmm");
		 instanse = true;
	     $.ajax({
	     	
			   type:"POST",
			   url: "execfunc2.php",
			   
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		//alert(data);
			   		//alert("ummmmmmmm");
			   		$('#chat-area').append($("<span>"+"Tanush" +"</span>"));
			   		getusersrc();
			   		getuserdst();
			   		getuserpth();
			   		alert('Your guide is here');
			   		//	alert("illll");
				   		if(src!='1' && dst!='1' && src!=1 && dst!=1)
				   		{
					   		alert("Your path is");
				   		djkproc(src,dst);
				   		//window.open('displyimage.php', "_blank");
				   		}
				   		else if(src=='1')
			   			{
			   				if(dst=="cafee")
			   				{

			   					$('#chat-area').append("The places for which you requested are:" );
				   				cafeproc();
				   				alert("u seem hungry");
				   				for(var i=0;i<cafe.length;i++)
				   				$('#chat-area').append($("<p>" + cafe[i] +"</p>")); 
				   			    //alert("kkk");
				   		    }
				   			else if(dst=="rest")
			   				{
			   					$('#chat-area').append("The places for which you requested are:" );
				   				restproc();
				   				alert("u seem tired");
				   				for(var i=0;i<rest.length;i++)
				   				$('#chat-area').append($("<p>" + rest[i] +"</p>")); 
			   				}
				   			else if(dst=="hostels")
			   				{
			   					$('#chat-area').append("The places for which you requested are:" );
				   				hostelproc();
				   				alert("u seem to be new");
				   				for(var i=0;i<hostel.length;i++)
				   				$('#chat-area').append($("<p>" + hostel[i] +"</p>")); 
			   				}
				   			else if(dst=="lib")
			   				{
			   					$('#chat-area').append("The places for which you requested are:" );
			   					
				   				stdyproc();
				   				alert("wow! u want to study");
				   				for(var i=0;i<stdy.length;i++)
				   				$('#chat-area').append($("<p>" + stdy[i] +"</p>")); 
			   				}
				   			else if(dst=="admin")
			   				{
			   					$('#chat-area').append("The places for which you requested are:" );
				   				adminproc();
				   				//alert("admin");
				   				for(var i=0;i<admin.length;i++)
				   				$('#chat-area').append($("<p>" + admin[i] +"</p>")); 
			   				}
			   				else
			   				 indproc();
			   			
			   			//	else $('#chat-area').append("Please enter a valid query?");
			   			}
			   		
			   			else
			   				 indproc();
			   				 document.getElementById('chat-area').scrollTop = document.getElementById('chat-area').scrollHeight;
			     	         instanse = false;
			   			  //var obj=data.split('_');
      					  //for(var i=0;i<obj.length;i++)
      					// { $('#chat-area').append($("<p>" + obj[i] +"</p>"));
      					 //}		 
			   },
			});
}
/*document.getElementById("demo").onmouseover = function() {mouseOver()};
function mouseOver() {
    document.getElementById("demo").style.color = "red";
}*/
function indproc()
				{
					//alert(src);
					//alert(dst);
					$.ajax({
						type:"GET",dataType:"JSON",url:"ind.php",
						contentType:"application/json;charset=utf-8",success: function(data)
						{
							//alert("hii");
							alert('Welcome at the official Thapar Guide');
							$('#chat-area').append(data );
						}
					});
				}
function djkproc(src,dst)
				{
					//alert(src);
					//alert(dst);
					$.ajax({
						type:"GET",dataType:"JSON",url:"path_index.php?src="+src+"dst="+dst,
						contentType:"application/json;charset=utf-8",success: function(data)
						{
							//alert("okk");
							$('#chat-area').append("The path you need to follow in sequence is" );
							for(i=0;i<data.length;i++)
							{
							//	alert(data[i].name);
								$('#chat-area').append($("<p>"+i+".) " + data[i].name +"</p>")); 
							}
							
							//$("#andhera").fadeIn(500);
							//$("#popup").show(500);

						}
					});
				}
//$('p').hover(pop);
/*function pop()
{
$("p").hover(function(){
	alert("pppp");
	$("#andhera").fadeIn(500);
    $("#popup").show(500);
    //$(this).css("background-color", "#9CF");
});
}
$("#andhera").click(dohide);
				function dohide()
				{
					
					$("#andhera").fadeOut(500);
					$("#popup").hide(500);

				}
*/
function adminproc()
{
	     $.ajax({
			   type:"POST",
			   url: "adminprocess.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		admin=data;
			   },
			});
}
function hostelproc()
{
	     $.ajax({
			   type:"POST",
			   url: "hostelprocess.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		hostel=data;
			   },
			});
}
function restproc()
{
	     $.ajax({
			   type:"POST",
			   url: "restprocess.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		rest=data;
			   },
			});
}

function cafeproc()
{
	//alert("llllll");
	     $.ajax({
			   type:"POST",
			   url: "cafeprocess.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		cafe=data;
			   },
			});
}
function stdyproc()
{
	//alert("okkk");
	     $.ajax({
			   type:"POST",
			   url: "stdyprocess.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		stdy=data;
			   },
			});
}
function getusersrc()
{
	//alert("getusrsrc");
	     $.ajax({
			   type:"POST",
			   url: "getsrc.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		src=data;
			   		//alert(src);
			   },
			});
}
function getuserdst()
{
	//alert("getusrdst");
	     $.ajax({
			   type:"POST",
			   url: "getdst.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){

			   		dst=data; 
			   },
			});
}
function getuserpth()
{
	     $.ajax({
			   type:"POST",
			   url: "getpth.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   	chkpth=data;
			   	//alert(chkpth);
			   },
			});
}
/*function getdjkstra()
{
	     $.ajax({
			   type:"POST",
			   url: "abc.php",
			   data: {  
			   			'function': 'update',
						'state': state,
						'file': file
						},
			   dataType: "json",
			   success:function(data){
			   		$('#chat-area').append($("<span>"+"Tanya" +"</span>"));
			   		
			   	$('#chat-area').append($("<p>" + "hii" +"</p>"));
				   document.getElementById('chat-area').scrollTop = document.getElementById('chat-area').scrollHeight;
			   },
			});
	
}*/
//send the message
function sendChat(message, nickname)
{       
    //updateChat();
     $.ajax({
		   type: "POST",
		   url: "process.php",
		   data: {  
		   			'function': 'send',
					'message': message,
					'nickname': nickname,
					'file': file
				 },
		   dataType: "json",
		   //alert(data);
		  // alert("hnn");
		   success: function(data){
			   updateChat();
			    getChat();
		   },
		});
}
