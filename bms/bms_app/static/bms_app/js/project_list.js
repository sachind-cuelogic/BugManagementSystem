function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
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

    $('.delete-project-confirm').on('click', function(event) {
        event.preventDefault();
        var del_proj_id = $(this).attr('id');   
        var row = $(this).closest("tr");
        var confirmation = confirm("are you sure you want to remove the item?");

        if (confirmation) {
            $.ajax({
                data:{ del_proj_id: del_proj_id},  
                dataType: "JSON",
                type: 'POST',
                url: "../delete_project/",
                success: function(result) 
                {   

                     if (result.success)
                     {
                        
                         row.remove();
                     }
                     else
                     {   alert("You don't have rights to delete project.");
                         
                     }
                  }
            });
        }
    });
});
