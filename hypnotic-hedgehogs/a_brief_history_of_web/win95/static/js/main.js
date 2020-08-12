    clippy.load('Clippy', (agent) => {
    // do anything with the loaded agent
    agent.show();

    agentSpeak(agent,"Hello, stranger! Welcome to this nostalgic trip! Soon, you will witness events that completely changed the course of history and became the most important milestones in human history. Enjoy it!");
    setTimeout(() => {
      agentSpeak(agent,"A long time ago in a galaxy far far away, a brand new and abstract technology just entered the stage of history. Like any new technology, it was naive and flawed. Its beginning was also humble. Sic parvis magna! But remember, great events start with small steps!");
    }, 8000);
    setTimeout(() => {
      agentSpeak(agent,"Now, to begin this nostalgic trip, enter your name to the Username field and click to Connect.");
    }, 20000);
    setTimeout(() => {
      agent.play("")
      agent.hide();
    }, 26000);

});

function hideIt(params) {

  var username = $("#username").val();

        $("#app-mine").hide();
        $("#app-mine2").show();
        setTimeout(() => {
          $("#app-mine2").hide();
          $(".internet-explorer").css("display","inline");
          clippy.load("Merlin",(agent) => {
    agent.show();
    agentSpeak(agent,"Welcome to the world of Internet, "+username+". Ahh... I need to check something quickly...");
    agent.play("Reading")
agentSpeak(agent, "According to my book of Eternal Wisdom, the Internet is one of the most revolutionary, democratic, magical and beneficial technology ever invented. It's one of the greatest successes of mankind.")
                  agent.play("Reading")

agentSpeak(agent, "Once a wise man named Arthur Clarke said: Any sufficiently advanced technology is indistinguishable from magic.")
                      agent.play("GestureUp")

    agentSpeak(agent, "This magical technology has made knowledge accessible and equal to all. Thus, it provided us with the opportunity to obtain and share information and to create a brand new reality in a digital and abstract layer, in a layer where everything is possible, by getting rid of the constraints of physical conditions.")
                  agent.play("Reading")

    agentSpeak(agent,"Listen, there’s a hell of a good universe next door; choose one of the urls from the notepad on the left by descending order, then paste it to the address bar of the browser, click to Go button and let’s go!");
    agent.play("");
    setTimeout(() => {
        agent.hide();
    },56000)
    });
        }, 5000);
      }

function agentSpeak(agent,text){
    agent.speak(text);
}

