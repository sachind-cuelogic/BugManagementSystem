$(document).ready(function(){
	if(document.getElementById('message')!==null){
		$.notify.defaults({ className: "success" })
		$.notify( 
			"You have successfully created bug",
			{ position:"top center" }
			);
	}
});

$(document).ready(function(){
  $(".editor-header a").click(function(e){
    e.preventDefault();

    var _val = $(this).data("role"),
        _sizeValIn = parseInt($(this).data("size-val") + 1),
        _sizeValRe = parseInt($(this).data("size-val") - 1),
        _size = $(this).data("size");
    if(_size == "in-size"){
      document.execCommand(_val, false, _sizeValIn + "px");
    } else{
      document.execCommand(_val, false, _sizeValRe + "px");
    }
  });
});

$(document).ready(function(){
  var $text = $("#text"),
      $submit = $("input[type='submit']"),
      $listComment = $(".list-comments"),
      $loading = $(".loading"),
      _data,
      $totalCom = $(".total-comment");
  $totalCom.text($(".list-comments > div").length);

  $($submit).click(function(){
    if($text.html() == ""){
      alert("Plesae write a comment!");
      $text.focus();
    } else{
      _data = $text.html();
      $.ajax({
        type: "GET",
        url: window.local,
        data: _data,
        cache: false,
        success: function(html){
          $loading.show().fadeOut(300);
          $listComment.append("<div>"+_data+"</div>");
          $text.html("");
          $totalCom.text($(".list-comments > div").length);
        }
      });
      return false;
    }
  });
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
        console.log(bug_id);
        console.log(bug_id);

        $.ajax({
            data:{ bug_id: bug_id },  
            dataType: "JSON",
            type: 'POST',
            url: "bug_list/",
            success: function(result) 
            {
              console.log(result[0]['project_name']);
              $("#project_name").text(result[0]['project_name']);
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
});

$(function(){
    console.log('ready');
    
    $('.list-group a').click(function(e) {
        e.preventDefault()
        
        $that = $(this);
        $('.list-group').find('a').removeClass('active');
        $that.addClass('active');
    });
    $('a.bug').eq(0).trigger('click')
})

$('#project_id').change(function() {
    var selected_proj_id = $(this).val();
    window.location = "/bug_list/?pid="+selected_proj_id;
});
