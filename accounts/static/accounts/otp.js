$('#verify-button').click(function(){

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var numbers = "";
numbers += $('#number1').val();
numbers += $('#number2').val();
numbers += $('#number3').val();
numbers += $('#number4').val();

    $.ajax({
        url: '/accounts/verify_phone_number/',
        method: 'POST',
        data: {
            'code': numbers,
        },
        success: function(data){
            if(data.status == 'ok'){
                top.location.href=data.url
            }
            else{
            $('#verify-form').html(data.data);
            };
        }
    });

});
