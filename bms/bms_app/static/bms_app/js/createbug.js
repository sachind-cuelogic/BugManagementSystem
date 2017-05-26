    $('#project_name').change(function() { 
        var project_id = $(this).val();
        window.location = "/create_bug/?pid="+project_id;
    });

    $(document).ready(function () {
    $('#nameoffile').bootstrapValidator({
        live: 'enabled',
        feedbackIcons: {

        },
        fields: {
            bug_file: {
                validators: {
                    file: {
                        extension: 'doc,docx,pdf,jpg,png,jpeg,xls,txt,xlsx',
                        type: 'application/pdf,application/msword,image/jpeg,image/png,image/jpg,application/vnd.ms-excel,text/plain',
                        maxSize: 5 * 1024 * 1024, // 5 MB
                        message: 'The selected file is not valid, it should be (doc,docx,pdf,jpg,png,jpeg,xls,txt,xlsx) and 5 MB at maximum.'
                    }
                }
            }
        }
    });

});

    $('#bug_type').change(function() {
    	if ($(this).children('option:first-child').is(':selected')) {
    		$(this).addClass('placeholder');
    	} else {
    		$(this).removeClass('placeholder');
    	}
    });

        $('#status').change(function() {
    	if ($(this).children('option:first-child').is(':selected')) {
    		$(this).addClass('placeholder');
    	} else {
    		$(this).removeClass('placeholder');
    	}
    });