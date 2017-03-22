
function checkusername()
{
  var userbox = document.getElementById('username');
  var usermessage = document.getElementById('usermsg');
  re = /^\w+$/;
  if(!re.test(userbox.value)) 
  {
    usermessage.style.color = "#ff6666" ;
    usermessage.innerHTML ="Username must contain only letters, numbers and underscores!";
    checkusername();
  }
  else
  {
    usermessage.innerHTML = "";
  }
}

function checkemail() 
{
  var emailbox = document.getElementById('email');
  var mailmessage = document.getElementById('mailmsg');
  var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if(filter.test(emailbox.value) == "")
  {
    mailmessage.innerHTML = "";
  }
  if (!filter.test(emailbox.value)) 
  {
    mailmessage.style.color = "#ff6666" ;
    mailmessage.innerHTML = "Not a valid e-mail address";
  }
  else
  {
    mailmessage.innerHTML = "";
  }
}

$(function () 
{
  $("#regbtn").click(function () 
  {
    var pass1 = $("#password").val();
    var pass2 = $("#password_confirm").val();
    if (pass1 != pass2) 
    {
      alert("Passwords do not match.");
      return false;
    }
    return true;
  });
/*  $(document).ready(function(){
    $("#regbtn").click(function(){
      $("#successmsg").fadeIn(1000);
    });
  });*/
});
