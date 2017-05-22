
$(document).on('click', '#close-preview', function(){ 
    $('.image-preview').popover('hide');
    // Hover befor close the preview    
});

$(function() {
    // Create the close button
    var closebtn = $('<button/>', {
        type:"button",
        text: 'x',
        id: 'close-preview',
        style: 'font-size: initial;',
    });
    closebtn.attr("class","close pull-right");

    // Clear event
    $('.image-preview-clear').click(function(){
        $('.image-preview').attr("data-content","").popover('hide');
        $('.image-preview-filename').val("");
        $('.image-preview-clear').hide();
        $('.image-preview-input input:file').val("");
        $(".image-preview-input-title").text("Browse"); 
    }); 
    // Create the preview image
    $(".image-preview-input input:file").change(function (){     
        var img = $('<img/>', {
            id: 'dynamic',
            width:200,
            height:150
        });      
        var file = this.files[0];
        var reader = new FileReader();
        // Set preview image into the popover data-content
        reader.onload = function (e) {
            $(".image-preview-input-title").text("Change");
            $(".image-preview-clear").show();
            $(".image-preview-filename").val(file.name);
        }        
        reader.readAsDataURL(file);
    });  
});

$(document).ready(function () {
    $('#name-of-file').bootstrapValidator({
        live: 'enabled',
        feedbackIcons: {

        },
        fields: {
            prod_file: {
                validators: {
                    file: {
                        extension: 'doc,docx,pdf,jpg,png,jpeg,xls,txt,xlsx',
                        type: 'application/pdf,application/msword,image/jpeg,image/png,image/jpg,application/vnd.ms-excel,text/plain',
                        maxSize: 1 * 1024 * 1024, // 5 MB
                        message: 'The selected file is not valid, it should be (doc,docx,pdf,jpg,png,jpeg,xls,txt,xlsx) and 5 MB at maximum.'
                    }
                }
            }
        }
    });

});