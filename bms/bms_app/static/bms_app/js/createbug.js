/*$('#project_name').change(function() {
	var e = document.getElementById("ddlViewBy");
	var project_id = e.options[e.selectedIndex].value;
    var project_id = $(this).val();
    console.log(project_id);
    window.location = "/create_bug/?pid="+project_id;
});
*/

/*$(document).ready(function() {
	$("#project_name").on("change", function() {
  	var project_id = $(this).val();
  	window.location = "/create_bug/?pid="+project_id;
  });
});
*/

window.onload = function() {
    var selItem = sessionStorage.getItem("SelItem");  
    $('#project_name').val(selItem);
    }
    $('#project_name').change(function() { 
        var project_id = $(this).val();
        sessionStorage.setItem("SelItem", project_id);
        window.location = "/create_bug/?pid="+project_id;
    });