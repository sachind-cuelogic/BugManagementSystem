

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

$(function() {
    $(document).on(
        'click',
        '[data-role="dynamic-fields"] > .form-inline [data-role="remove"]',
        function(e) {
            e.preventDefault();
            $(this).closest('.form-inline').remove();
        }
    );

    $('.adduser').on('click', function() {
            var container = $('[data-role="dynamic-fields"]').
                                        closest('[data-role="dynamic-fields"]');
            new_field_group = container.children().
                                    filter('.form-inline:first-child').clone();
            new_field_group.find('input').each(function(){
                $(this).val('');
            });
            container.append(new_field_group);
        }
    );
});

    
});
