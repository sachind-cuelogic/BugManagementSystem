$(document).ready(function(){
  if(document.getElementById('bug-message')!==null){
    $.notify.defaults({ className: "success" })
    $.notify( 
      "You have successfully created bug",
      { position:"top center" }
      );
  }
});

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

    $('.bug').on('click', function(event) {
        event.preventDefault();
        var bug_id = $(this).attr('id');
        var project_id = $('#project_id').val();


        $.ajax({
            data:{ bug_id: bug_id},  
            dataType: "JSON",
            type: 'POST',
            url: "bug_list/",
            success: function(result) 
            {

              jQuery('#comment-text').html('');
              for(var i = 0; i < result[1].length; i++) 
              {
                $("#comment-text").prepend('<div><b>' + result[1][i]['user__username']  +"</b>: "+result[1][i]['comment'] + '</div><hr>');

              }

              $("#title").text(result[0]['title']);
              $("#bug_type").text(result[0]['bug_type']);
              $("#status").text(result[0]['status']);
              $("#build_version").text(result[0]['build_version']);
              $("#sprint_no").text(result[0]['sprint_no']);
              $("#dependent_module").text(result[0]['dependent_module']);
              $("#description").text(result[0]['description']);
              $("#bug_owner").text(result[0]['bug_owner']);
              $("#bug_assign").text(result[0]['bug_assign']);

            }
        });
    });

/* pass comment to view */

    $('[name="comment-button"]').on('click', function(event) {
        event.preventDefault();
        var comment_text = $('#comment').val();
        var username = $("#username").text();
        var bid = document.getElementsByClassName("list-group-item active")[0].id;

        $.ajax({
            data:{ comment_text: comment_text, bid: bid },  
            dataType: "JSON",
            type: 'POST',
            url: "../comment_section/",
            success: function(result) 
            {
              $("#comment-text").prepend("<p><b>"+username+"</b>: "
                                          +comment_text+"</p><hr>")
            }
        });
    });

/* clear textarea on click button */

$('.comment').on('click', function(event) {
    event.preventDefault();
    $("#comment").val('');
});

$('[name="comment-button"]').attr('disabled', true);

$('textarea').on('keyup',function() {
    var textarea_value = $("#comment").val();
    if(textarea_value != '') {
        $('[name="comment-button"]').attr('disabled' , false);
    }
    else
    {
        $('[name="comment-button"]').attr('disabled' , true);
    }
});


});

/* bug list group active on click */

$(function(){
    
    $('.list-group a').click(function(e) {
        e.preventDefault()
        
        $that = $(this);
        $('.list-group').find('a').removeClass('active');
        $that.addClass('active');
    });
    $('a.bug').eq(0).trigger('click')
})

/* pass project id to view */

$('#project_id').change(function() {
    var selected_proj_id = $(this).val();
    window.location = "/bug_list/?pid="+selected_proj_id;
});


$(document).ready(function() {
    $('#bug-list-column').DataTable();
} );
