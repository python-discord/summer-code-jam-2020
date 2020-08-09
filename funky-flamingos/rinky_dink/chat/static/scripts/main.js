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

// $('.chat-input input').each(function() {
//     if ($(this).val() !== '') {
//         $('#'+this.id+' + label').animate({
//             'fontSize': '0.8rem',
//             'top': '1.4rem',
//             'padding': '0.25rem'
//         }, 80);
//     }
//     $(this).focusin(() => {
//         $('#'+this.id+' + label').animate({
//             'fontSize': '0.8rem',
//             'top': '-.75em',
//             'padding': '0.25em'
//         }, 80);
//     });
//     $(this).focusout(function() {
//         if ($(this).val() === '') {
//             $('#'+this.id+' + label').animate({
//                 'fontSize': '1rem',
//                 'top': '1em',
//                 'padding': 0
//             }, 80);
//         }
//     });
// });

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
                $("#messages").append(
                    "<div class=\"message " + message.class_name
                    + "\"><span class=\"username\"></span><span class=\"body\"></span></div>"
                    );
                $(".message:last-child .username").text(message.username + ':');
                $(".message:last-child .body").text(message.content);
                console.log(message.username);
            }
        }
    });
});

$(".chat-input input").keypress(e => {
    if (e.keyCode === 13) {
        e.preventDefault();
        $("#messages").append("<div class=\"message self\"></div>");
        $(".message:last-child").text($(".chat-input input").val());
        $.ajax({
            url: "/chat/send_message",
            type: "POST",
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: {
                message: $(".chat-input input").val(),
            }
        }).done(result => {
            if (result.type !== "messages") {
                // Error
                alert(result.message);
            } else {
                $("#messages").empty();
                for (let i = 0; i < result.messages.length; i++) {
                    let message = result.messages[i]
                    $("#messages").append(
                        "<div class=\"message " + message.class_name
                        + "\"><span class=\"username\"></span><span class=\"body\"></span></div>"
                        );
                    $(".message:last-child .username").text(message.username + ':');
                    $(".message:last-child .body").text(message.content);
                    console.log(message.username);
                }
            }
        });
        $(".chat-input input").val("");
    }
});

// to scroll to bottom of chat
$(document).ready(function() {
    $('html, body').animate({scrollTop:$(document).height()}, 'slow');
});