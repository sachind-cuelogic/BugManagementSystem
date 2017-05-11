$(document).ready(function(){
	if(document.getElementById('message')!==null)
	{
		console.log("inside message")
		$.notify.defaults({ className: "success" })
		$.notify( 
			"You have successfully registered.",
			{ position:"top center" }
			);
	}
});
