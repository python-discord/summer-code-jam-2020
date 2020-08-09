// Name of the chatbot
const botName = JSON.parse($('#namejson').text());
var messages = [];

async function chatbotResponse(lastUserMessage) {
    let botMessage = "I'm confused"; // The default message
    if(lastUserMessage.startsWith('wiki')) {
        let article_name = /[Ww]iki "?(.+)"?$/.exec(lastUserMessage)[1];
        await $.get('/getwiki/', {'article_name': article_name}, function(article) {
            botMessage = article.name + ': ' + article.summary;
        });
    } else if(lastUserMessage.toLowerCase() === 'hi' || lastUserMessage.toLowerCase() === 'hello') {
        const hi_messages = ['hi', 'howdy', 'hello'];
        botMessage = hi_messages[Math.floor(Math.random() * hi_messages.length)];
    } else if(lastUserMessage.toLowerCase().includes('your name')) {
        botMessage = 'My name is ' + botName + '.';
    }

    return botMessage;
}

async function processMessage() {
    if ($('#inputbox').val() != "") {
        let lastUserMessage = $('#inputbox').val();
        $('#inputbox').val('');

        messages.push(lastUserMessage);
        botMessage = await chatbotResponse(lastUserMessage);

        var botMessageLog = $('<p class="chatmessage">');
        botMessageLog.html('<b>' + botName + ':</b> ' + botMessage);
        messages.push(botMessageLog);
        botSpeak(botMessage);

        for (var i = 1; i < 8; i++) {
            if (messages[messages.length - i]) {
                $('#chatlog' + i).html(messages[messages.length - i]);
            }
        }
    }
}


// https://developers.google.com/web/updates/2014/01/Web-apps-that-talk-Introduction-to-the-Speech-Synthesis-API
function botSpeak(say) {
    if ('speechSynthesis' in window) {
        var utterance = new SpeechSynthesisUtterance(say);
        //msg.voice = voices[10]; // Note: some voices don't support altering params
        //msg.voiceURI = 'native';
        //utterance.volume = 1; // 0 to 1
        //utterance.rate = 0.1; // 0.1 to 10
        //utterance.pitch = 0; //0 to 2
        //utterance.text = 'Hello World';
        //utterance.lang = 'en-US';
        speechSynthesis.speak(utterance);
    }
}

$('#inputbox').on({
    keypress: function(e) {
        if(e.which == 13) {
            processMessage();
        }
    },
    focus: function() {
        $(this).prop('placeholder', '');
    }
});
