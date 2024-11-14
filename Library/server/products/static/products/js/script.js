function getCookie(name){

    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i=0;i<cookies.length;i++) {
            let cookie = jQuery.trim(cookies[i]);
            console.log(cookie);
            if (cookie.substring(0, name.length) === (name)) {
                cookieValue = cookie.split('=');
                cookieValue = decodeURIComponent(cookieValue[1]);
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)&/.test(method));
}

const add_to_favorites_url = '/favorites/add/';
const remove_from_favorites_url = '/favorites/remove/';
const favorites_api_url ='/favorites/api/';

$(document).ready(function(){
    $('.button_add').click(function(){
        console.log('Done');
        console.log(getCookie('csrftoken'));

        $.ajax({
            url: '/favorites/add/',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                id: $(this).data('id'),
            },
            type: 'POST',
            success: function(data){
                console.log(data);
                console.log(data.ses);
            },
            error: function(err){
                console.log(err);
            }
        });
    });
});
$(document).ready(function(){
    $('.button_remove').click(function(){
        console.log('Done');
        console.log(getCookie('csrftoken'));

        $.ajax({
            url: '/favorites/remove/',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                id: $(this).data('id'),
            },
            type: 'POST',
            success: function(data){
                console.log(data);
            },
            error: function(err){
                console.log(err);
            }
        });
    });
});

