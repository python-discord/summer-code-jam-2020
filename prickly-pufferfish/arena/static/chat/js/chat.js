$(function() {
    const battleID = JSON.parse($('#battle-id').html());

    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/chat/'
        + battleID
        + '/'
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        document.querySelector('#chat-log').value += (data.message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    const chatInput = $('.chat-input');

    chatInput.keyup(function (e) { 
        if (e.which == 13) {
            send();
        }
    });

    $('chat-submit').click(function (e) {
        send()
    });

    function send() {
        const msg = chatInput.val();
        chatSocket.send(JSON.stringify({
            'message': msg
        }));
        chatInput.val('');
    }

});
