

$(document).ready(function(){
  

$(function() {
    $(document).on(
        'click',
        '[data-role="dynamic-fields"] > .form-inline [data-role="remove"]',
        function(e) {
            e.preventDefault();
            $(this).closest('.form-inline').remove();
            disableCross();
        }
    );

    var disableCross = function(){ 
    console.log("inside disable function", $('[data-role="dynamic-fields"] > .form-inline').length);  

        if ($('[data-role="dynamic-fields"] > .form-inline').length == 1) {

           /* console.log("inside length 1");*/
           $('[data-role="dynamic-fields"] > .form-inline:first-child [data-role="remove"]').prop("disabled", true);
        } 
        else 
        {
            $('[data-role="dynamic-fields"] > .form-inline:first-child [data-role="remove"]').prop("disabled", true);
           /* console.log("inside enable button");*/
            $("#modalbody .form-inline button").prop("disabled", false); 
        }
    };

    disableCross();

    $('.adduser').on('click', function() {

            var container = $('[data-role="dynamic-fields"]').closest('[data-role="dynamic-fields"]');
            new_field_group = container.children().filter('.form-inline:first-child').clone();
            new_field_group.find('input').each(function(){
                $(this).val('');
            });
            container.append(new_field_group);
            
            console.log(disableCross());
           /* console.log("after function call");*/
        }

    );
});

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
