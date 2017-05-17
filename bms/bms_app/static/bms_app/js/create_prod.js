

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

        if ($('[data-role="dynamic-fields"] > .form-inline').length == 1) {

           /* console.log("inside length 1");*/
           $('[data-role="dynamic-fields"] > .form-inline:first-child button').prop("disabled", true);
           $('[data-role="dynamic-fields"] > .form-inline:first-child select').prop("disabled", true);
        } 
        else 
        {
            $('[data-role="dynamic-fields"] > .form-inline:first-child [data-role="remove"]').prop("disabled", false);
            $('[data-role="dynamic-fields"] > .form-inline:first-child select').prop("disabled", false);
           /* console.log("inside enable button");*/
           
        }
    };

    disableCross();
/*    var uname = $('#user-name').find(":selected").attr('disabled', 'disabled');*/
    $('.adduser').on('click', function() {

            var cloneCount = 1;

            var container = $('[data-role="dynamic-fields"]').closest('[data-role="dynamic-fields"]');
            new_field_group = container.children().filter('.form-inline:first-child').clone();

            // $('#user-name').attr('id', 'id'+ cloneCount++).insertAfter($('[id^=id]:last'));

            new_field_group.find('input').each(function(){

                $(this).val('');
            });
            /*var uname = $('#user-name').find(":selected").attr('disabled', 'disabled');*/
            container.prepend(new_field_group);
/*            $('#user-name option[value=' + $(this).val() + ']').attr('disabled', 'disabled');*/
            // var uname = $('#user-name').find(":selected").remove();



/*            $('#user-name').each(function() {
                $(this).find(":selected").remove();
                $('option[value=' + $(this).val() + ']').remove();
            });*/



            /*  console.log("selected value",uname);*/
            disableCross();
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
