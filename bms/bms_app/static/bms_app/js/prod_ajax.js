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

    var getuser = $('#get_username').text();

    var select=document.getElementById('user-name');
    console.log("length==>",select.length)

    for (i=0;i<select.length; i++) {
       if (select.options[i].value==getuser) {
         select.remove(i);
       }
    }

    $("#submit-sample-data").on("click", function () {

        var htmlUser = "";
        var user_name = $(".user-name option:selected").text();
        var user_id = $(".user-name option:selected").val();
        var user_role = $(".user-role option:selected").text(); 
        var user_role_id = $(".user-role option:selected").val(); 
        htmlUser += "<div id='user-count'>";
        htmlUser += "<span class='selected-user-name'>"+user_name+"</span>";        
        htmlUser += "<span class='selected-user-id' style='display: none;'>"+user_id+"</span>";
        htmlUser += "<span id='dash'> : </span>";
        htmlUser += "<span class='selected-user-role'>"+user_role+"</span>";
        htmlUser += "<span class='selected-role-id' style='display: none;'>"+user_role_id+"</span>";
        htmlUser += "<span class='remove pull-right close' id='removeBtn aria-label='Close''>" + "<span class='glyphicon glyphicon-remove'></span>" + "</span>";
        htmlUser += "</div>";

        $("#user_info").append(htmlUser);

        $('#user-name').each(function() {
            $('option[value=' + $(this).val() + ']').remove();
        });

});

    $(".selected-user-role").on("click", ".remove", function(){
        var removeUser = $(this).siblings(".selected-user-name").text();
        var removeUserId = $(this).siblings(".selected-user-id").text();
        $(this).parent().remove();

        $('#user-name').append($('<option>', {
            value: removeUserId,
            text: removeUser
        }));

    });

    $('#file-form').on('submit', function(event) {
        event.preventDefault();
        user_data = []
        if($('.selected-user-role div').length){
            for (i = 0; i <= ($('.selected-user-role div').length-1); i++) {
                user_data.push({
                    'user_id': $('.selected-user-id').eq(i).text(),
                    'user_role': $('.selected-role-id').eq(i).text()
                })
            }
        }
        else{
            
        }
        var ptype = $('#producttype').val()
        formdata = new FormData(this);
         if($("#prod_file")[0].files.length>0)
       		formdata.append("prod_file",$("#prod_file")[0].files[0]);
       	formdata.append('user_data',(JSON.stringify(user_data)))
        formdata.append('ptype',(ptype))

        $.ajax({
            data:formdata,  
            dataType: "JSON",
            processData: false,
            contentType: false,
            type: 'POST',
            url: "create_project/",
            success: function(result) 
            {
                if(result['success']) 
                {
                    $("#output-text").html(result['response']);
                    window.location.href = "/project_list/"
                }
            }
        });
    });
});

