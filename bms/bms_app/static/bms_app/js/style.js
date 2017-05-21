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
            notEmpty: {
                message: 'The username is required and can\'t be empty'
            },
            stringLength: {
                min: 6,
                max: 30,
                message: 'The username must be more than 6 and less than 30 characters long'
            },
            regexp: {
                regexp: /^[a-zA-Z0-9_\.]+$/,
                message: 'The username can only consist of alphabetical, number, dot and underscore'
            }
        }
    },

    email: {
        validators: {
            notEmpty: {
                message: 'Please enter your email address'
            },
            emailAddress: {
                message: 'Please enter a valid email address'
            }
        }
    },

    password: {
        validators: {
            regexp: {
                regexp: /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/,
                message: 'Password must contain Minimum 8 characters at least 1 Alphabet and 1 Number:'
            },

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
$('#success_message').slideDown({ opacity: "show" }, "slow")
$('#reg_form').data('bootstrapValidator').resetForm();


e.preventDefault();


var $form = $(e.target);
var bv = $form.data('bootstrapValidator');

$.post($form.attr('action'), $form.serialize(), function(result) {
}, 'json');
});
});
