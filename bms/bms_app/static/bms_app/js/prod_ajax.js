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

    $("#submit-sample-data").on("click", function () {

        
        var htmlUser = "";

        var user_name = $(".user-name option:selected").text();
        var user_id = $(".user-name option:selected").val();
        console.log("username==>",user_name,user_id);
        var user_role = $(".user-role option:selected").text(); 
        var user_role_id = $(".user-role option:selected").val(); 
        console.log("role==>",user_role,user_role_id);
        htmlUser += "<div>";
        htmlUser += "<span class='selected-user-name'>"+user_name+"</span>";
        htmlUser += "<span class='selected-user-id' style='display: none;'>"+user_id+"</span>";
        htmlUser += "<span> - </span>";
        htmlUser += "<span>"+user_role+"</span>";
        htmlUser += "<span class='remove pull-right'>" + "x" + "</span>";
        htmlUser += "</div>";
        
        $("#user_info").append(htmlUser);
        // $("#user_info").html(htmlUser);

        $('#user-name').each(function() {
            $(this).find(":selected").remove();
            $('option[value=' + $(this).val() + ']').remove();
        });
    });

    $(".selected-user-role").on("click", ".remove", function(){
        var removeUser = $(this).siblings(".selected-user-name").text();
        console.log("remove id==>",removeUser);
        var removeUserId = $(this).siblings(".selected-user-id").text();
        console.log("remove id==>",removeUserId);
        $(this).parent().remove();
        
        /*console.log(removeUser);*/

        $('#user-name').append($('<option>', {
            value: removeUserId,
            text: removeUser
        }));

    });

    $('#file-form').on('submit', function(event) {
        console.log("inside submit function");
        event.preventDefault();
        user_data = []
        if($('.user-name').length){
            console.log("inside length",($('.user-name').length));
            for (i = 0; i <= ($('.user-name').length-1); i++) {
                console.log("inside for loop");
                console.log("user id==>",$('.user-name').eq(i).val());
                console.log("user role==>",$('.user-role').eq(i).val());
                user_data.push({
                    'user_id': $('.user-name').eq(i).val(),
                    'user_role': $('.user-role').eq(i).val()
                })
                console.log("user data==>",user_data);
            }
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
