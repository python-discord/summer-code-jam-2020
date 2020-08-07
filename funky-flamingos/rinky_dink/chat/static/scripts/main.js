function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$('.chat-input input').each(function() {
    if ($(this).val() !== '') {
        $('#'+this.id+' + label').animate({
            'fontSize': '0.8rem',
            'top': '1.4rem',
            'padding': '0.25rem'
        }, 80);
    }
    $(this).focusin(() => {
        $('#'+this.id+' + label').animate({
            'fontSize': '0.8rem',
            'top': '-.75em',
            'padding': '0.25em'
        }, 80);
    });
    $(this).focusout(function() {
        if ($(this).val() === '') {
            $('#'+this.id+' + label').animate({
                'fontSize': '1rem',
                'top': '1em',
                'padding': 0
            }, 80);
        }
    });
});

$(document).ready(() => {
    $(".chat-input input").focus();
    $.ajax({
        url: "/chat/get_messages",
        type: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        }
    }).done(result => {
        if (result.type !== "messages") {
            // Error
            alert(result.message);
        } else {
            for (let i = 0; i < result.messages.length; i++) {
                let message = result.messages[i]
                $("#messages").append("<div class=\"message " + message.class_name + "\"></div>");
                $(".message:last-child").text(message.content);
            }
        }
    });
});

$(".chat-input input").keypress(e => {
    if (e.keyCode === 13) {
        e.preventDefault();
        $("#messages").append("<div class=\"message self\"></div>");
        $(".message:last-child").text($(".chat-input input").val());
        // TODO make POST request here
        $(".chat-input input").val("");
    }
});
