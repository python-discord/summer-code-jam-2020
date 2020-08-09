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
              setTimeout(() =>{
                      agentSpeak(agent, "According to my book of Eternal Wisdom, the Internet is one of the most revolutionary, democratic, magical and beneficial technology ever invented. It's one of the greatest successes of mankind.")
,3000
              })
                            setTimeout(() =>{
                          agentSpeak(agent, "Once a wise man named Arthur Clarke said: Any sufficiently advanced technology is indistinguishable from magic."),5000
              })
    agentSpeak(agent, "This magical technology has made knowledge accessible and equal to all. Thus, it provided us with the opportunity to obtain and share information and to create a brand new reality in a digital and abstract layer, in a layer where everything is possible, by getting rid of the constraints of physical conditions.")
    agentSpeak(agent,"Listen, there’s a hell of a good universe next door; choose one of the urls from the notepad on the left, paste it to the address bar of the browser, click to Go button and let’s go!");

    /*For the blog page*/
    agentSpeak(agent, "In the '90s, when the Internet emerged and just started to spread, the most popular sites at first looked like this one. Personal blogs were in his place. Thanks to this democratic technology, everyone wanted to express themselves, share their thoughts and leave a mark in history. They did and are keep doing.")
    agentSpeak(agent, "To continue the tour, you can take another url from the notebook on the left, paste it in the address part of the browser, and press the Go button.")

    /*For Google.*/
    agentSpeak(agent, "Google, derived from the mathematical term Googol and created by two college students in the garage, this site literally changed the world, history, and people's lives. Changing the way we reach information, answers, questions, requests and people, this search engine has revolutionized every aspect of life. Thanks to Google, the world is now more integrated, people are more curious and wiser, and life is more interesting. Thank you Google!")
    agentSpeak(agent, "To continue the tour, you can take another url from the notebook on the left, paste it in the address part of the browser, and press the Go button.")

    /*For YouTube*/
    agentSpeak(agent, "Remember what we said before? Great events start with small steps? That's exactly what happened on YouTube. YouTube, which entered the internet environment by calling out from a zoo sincerely, is currently the most popular video and live streaming platform on the planet. We do not know what we would have done without YouTube; which functions as a movie theater, school, concert and game zone. Thank you YouTube for being so beneficial!")
    agentSpeak(agent, "To continue the tour, you can take another url from the notebook on the left, paste it in the address part of the browser, and press the Go button.")

    /*For Twitter*/
    agentSpeak(agent, "Jack was unaware that by setting up his 'twittr', he was building a site where he would make an unimaginable contribution to freedom of expression, thought sharing, polyphony and diversity. Thanks to Twitter, freedom of expression, polyphony, respect for differences and living in harmony have become possible and spread like never before. Thanks Twitter and Jack for supporting and spreading the freedoms!")

    /*The End*/
    agentSpeak(agent, "And here we are, the end of the trip. But before we split our roads, let me say a few more words.")
    agentSpeak(agent, "This young technology, which is just 30 years old, has already changed our lives in ways we never imagined, and it continues to change. We hope that this short trip to the history of the Internet has been inspiring and informative for you. And we hope again that the Internet continues to be a democratic, revolutionary, magical and useful technology.")
    agentSpeak(agent, "Don't just use these beautiful sites and the Internet, but also contribute. Create something and change the world, leave a mark. Do it so that when people will go on a nostalgic trip with a project like this in the future, they will be able to see your creation and contribution.")
    agentSpeak(agent, "Hokus pokus, abra kadabra! Let time flow forward and the magic of the Internet continues to spread! Keep staying online and magical! :)")
    });
        }, 5000);

      }

function agentSpeak(agent,text){
    agent.speak(text);
}
