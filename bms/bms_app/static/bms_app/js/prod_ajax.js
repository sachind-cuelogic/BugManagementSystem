function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#submit-data').on('click', function(event) {
        event.preventDefault();
        user_data = []

        for (i = 0; i <= $('.user-name').length; i++) {
            user_data.push({
                'user_id': $('.user-name').eq(i).val(),
                'user_role': $('.user-role').eq(i).val()
            })
        }

        var data = {
            'prod_name': $('#prod_name').val(),
            'prod_type': $('#producttype').val(),
            'prod_ver': $('#prod_version').val(),
            'prod_desc': $('#prod_description').val(),
            'prod_file': $('#prod_file').val(),
            'prod_user_data' : user_data
        }

        $.ajax({
            data: data,
            type: 'POST',
            dataType: 'json',
            url: "create_product/",
            success: function(result) {
                $("#output-text").html(result['response']);
                console.log(data);
            }
        });
    });
});



/*			'prod_name':$('#prod_name').val(),
			'prod_type':$('#producttype').val(),
			'data': $('#sample-data').val(),
			'user': $('#sample-users').val(),
			'prod_ver':$('#prod_version').val(),
			'prod_desc':$('#prod_description').val(),
			'prod_file':$('#prod_file').va*/
