$(document).ready(function(){
	if(document.getElementById('message')!==null){
		$.notify.defaults({ className: "success" })
		$.notify( 
			"You have successfully created bug",
			{ position:"top center" }
			);
	}
});
