$(function() {
    const battleSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/battle/'
        + battleID
        + '/'
    );

    var color, colorName, colorBG;
    if (colorID == 'R') {
        color = 'red';
        colorName = 'Red';
        colorBG = 'red-bg';
    } else if (colorID == 'B') {
        color = 'blue';
        colorName = 'Blue';
        colorBG = 'blue-bg';
    } else {
        console.error('Did not get a valid color!');
    }

    $('.color').addClass(color).removeClass('color');
    $('.color-name').text(colorName).removeClass('color-name');
    $('.color-bg').addClass(colorBG).removeClass('color-bg');

    battleSocket.onopen = function(e) {
        battleSocket.send(JSON.stringify({
            'type': 'challenger.join',
            'username': username
        }));
    }

    var ready = false;
    battleSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        switch (data.type) {
            case 'battle.ready':
                $('#pre-ready').hide();
                $('#waiting-heading').hide();
                $('#ready-heading').show();
                $('#ready-btn').show();
                $('#not-ready').show();
                break;
            case 'battle.unready':
                $('#ready-btn').hide();
                $('#not-ready').hide();
                $('#ready-heading').hide();
                $('#ready-text').hide();
                $('#waiting-heading').show();
                $('#pre-ready').show();
                break;
            case 'battle.activate':
                $('#ready-btn').hide();
                $('#ready-text').hide();
                $('#ready-heading').hide();
                $('#pre-ready').hide();
                $('#not-ready').hide();
                $('#waiting-heading').hide();
                $('#you-are').hide();
                $('#activate-heading').show();
                break;
            case 'battle.start':
                $('#waiting').hide();
                $('#battle').show();
                $('#chat-input').prop('disabled', true);
                $('#chat-submit').prop('disabled', true);
                break;
            case 'chat.message':
                var newMessage = $('<p></p>')
                    .text(data.sender.username + ': ' + data.message)
                    .appendTo('#chat-view');
                if (data.sender.color) {
                    newMessage.addClass(data.sender.color);
                }
                var chatView = $('#chat-view');
                chatView.scrollTop(
                    chatView.prop('scrollHeight') - chatView.prop('clientHeight')
                );
                break;
        }
    }

    battleSocket.onclose = function(e) {
        console.error('Battle socket closed unexpectedly');
    };

    const chatInput = $('#chat-input');

    chatInput.keyup(function (e) {
        if (e.which == 13) {
            chat_send();
        }
    });

    $('#chat-submit').click(function (e) {
        chat_send()
    });

    function chat_send() {
        const msg = chatInput.val().trim();
        if (msg.length > 0) {
            battleSocket.send(JSON.stringify({
                'type': 'chat.message',
                'sender': {
                    'username': username,
                    'color': color
                },
                'message': msg
            }));
            chatInput.val('');
        }
    }

    $(window).on('beforeunload', function() {
        return confirm();
    });

    $('#ready-btn').click(function(e) {
        ready = !ready;
        $('#not-ready').toggle();
        $('#ready-text').toggle();
        if (ready) {
            $('#ready-btn').text('Changed your mind?');
        } else {
            $('#ready-btn').text('Ready!');
        }
        battleSocket.send(JSON.stringify({
            'type': 'challenger.decide',
            'username': username,
            'decision': ready
        }))
    });

    $('#submission-area').linedtextarea();

    $('#submission-area').change(function(e) {
        hljs.highlightBlock($('#submission-area')[0]);
    });
});
