$(document).ready(function(){


function alignModal(){
    var modalDialog = $(this).find(".modal-dialog");
    
    modalDialog.css("margin-top", Math.max(0, 
                        ($(window).height() - modalDialog.height()) / 2));
}
$(".modal").on("shown.bs.modal", alignModal);

$(window).on("resize", function(){
    $(".modal:visible").each(alignModal);
}); 

});
