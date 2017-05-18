
if(document.getElementById('message')!==null)
{
	$.notify.defaults({ className: "success" })
	$.notify( 
		"You have successfully registered.",
		{ position:"top center" }
		);
}

