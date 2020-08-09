    clippy.load('Clippy', (agent) => {
    // do anything with the loaded agent
    agent.show();
    agentSpeak(agent,"Hey ! Welcome stranger.");
    setTimeout(() => {
      agentSpeak(agent,"Before connecting to internet, please enter your username and click Connect.");
    }, 3000);
    setTimeout(() => {
      agent.play("")
      agent.hide();
    }, 10000);

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
    agentSpeak(agent,"Welcome to world of Internet, "+username+". Ahh... I need to check something quickly..");
    agent.play("Reading")
    agentSpeak(agent,"Lorem ip elit. Quam voluptatibus exercitationem  reprehenderit officiis saepe labore vitae, rem eligendi?")

  });
        }, 5000);

      }

function agentSpeak(agent,text){
    agent.speak(text);
}