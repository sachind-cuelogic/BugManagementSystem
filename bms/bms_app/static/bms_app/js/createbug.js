    $('#project_name').change(function() { 
        var project_id = $(this).val();
        window.location = "/create_bug/?pid="+project_id;
    });