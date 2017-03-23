
    $(document).ready(function() {
      $('#reg_form').bootstrapValidator({

feedbackIcons: {
  valid: 'glyphicon glyphicon-ok',
  invalid: 'glyphicon glyphicon-remove',
  validating: 'glyphicon glyphicon-refresh'
},
fields: {
  username: {
    validators: {
      stringLength: {
        min: 2,
      },
      notEmpty: {
        message: 'Please supply your first name'
      }
    }
  },

  email: {
    validators: {
      notEmpty: {
        message: 'Please supply your email address'
      },
      emailAddress: {
        message: 'Please supply a valid email address'
      }
    }
  },

  password: {
    validators: {
      identical: {
        field: 'confirmPassword',
        message: 'Confirm your password below - type same password please'
      }
    }
  },
  confirmPassword: {
    validators: {
      identical: {
        field: 'password',
        message: 'The password and its confirm are not the same'
      }
    }
  },
}
})
      
      .on('success.form.bv', function(e) {
$('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
$('#reg_form').data('bootstrapValidator').resetForm();

e.preventDefault();

var $form = $(e.target);

var bv = $form.data('bootstrapValidator');

$.post($form.attr('action'), $form.serialize(), function(result) {
  console.log(result);
}, 'json');
});
    });
