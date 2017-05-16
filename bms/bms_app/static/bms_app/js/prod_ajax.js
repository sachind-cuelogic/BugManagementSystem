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

        console.log("inside submit function");

        if($('.user-name').length){

            console.log("inside if username ");
            
            var htmlUser = "";
        
            for (i = 0; i <= ($('.user-name').length-1); i++) {
                    
                console.log("inside for loop");
                
                var user_name = $(".user-name option:selected").eq(i).text();
                var user_role = $(".user-role option:selected").eq(i).text(); 

                console.log("username==>",user_name);
                console.log("role ==>",user_role);

                htmlUser += "<div>";
                htmlUser += "<span>"+user_name+" - "+"</span>";
                htmlUser += "<span>"+user_role+"</span>";
                htmlUser += "</div>";
            }   

            $("#user_info").show();
            $("#user_info").html(htmlUser);
        }
    });

    $('#file-form').on('submit', function(event) {
        event.preventDefault();
        user_data = []
        if($('.user-name').length){
            for (i = 0; i <= ($('.user-name').length-1); i++) {
                user_data.push({
                    'user_id': $('.user-name').eq(i).val(),
                    'user_role': $('.user-role').eq(i).val()
                })
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
