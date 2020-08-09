
var messages = [], // Array that hold the record of each string in chat
  botMessage = "", // Var keeps track of what the chatbot is going to say
  const name_json = JSON.parse(document.getElementById("namejson").textContent);
   
  botName = name_json['name'], // Name of the chatbot
  talking = true; // When false the speach function doesn't work

function chatbotResponse(lastUserMessage) {
    talking = true;
    botMessage = "I'm confused"; // The default message

    if (lastUserMessage === 'hi' || lastUserMessage =='hello') {
        const hi = ['hi','howdy','hello']
        botMessage = hi[Math.floor(Math.random()*(hi.length))];;
    }

    if (lastUserMessage === 'name') {
        botMessage = 'My name is ' + botName;
    }
}

function processMessage() {
    if ($('#inputbox').val() != "") {
        let lastUserMessage = $('#inputbox').val();
        $('#inputbox').val('');

        messages.push(lastUserMessage);
        chatbotResponse(lastUserMessage);

        messages.push("<b>" + botName + ":</b> " + botMessage);
        Speech(botMessage);

        /*for (var i = 1; i < 8; i++) {
            if (messages[messages.length - i]) {
                document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
            }
        }*/

        var userMessageLog = $('<p class="chatmessage">');
        userMessageLog.html(lastUserMessage);
        $('#chatlog').append(userMessageLog);

        var botMessageLog = $('<p class="chatmessage">');
        botMessageLog.html('<b>' + botName + ':</b> ' + botMessage);
        $('#chatlog').append(botMessageLog);
    }
}


//https://developers.google.com/web/updates/2014/01/Web-apps-that-talk-Introduction-to-the-Speech-Synthesis-API
function Speech(say) {
    if ('speechSynthesis' in window && talking) {
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

function progress_bar() {
    let progress = 0;
    let intervalID = setInterval(
        function() {
            if(progress <= 100) {
                $('[role=progressbar]').width(progress + '%');
                $('[role=progressbar]').prop('aria-valuenow', progress)
                progress++;
            } else {
                clearInterval(intervalID);
            }
        },
        5 // milliseconds per loop
    );
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
