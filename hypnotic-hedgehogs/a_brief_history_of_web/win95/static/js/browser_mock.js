// url_mapping
let url_mapping = {
    "https://youtube.com": "/first_youtube",
    "https://google.com": "/first_google",
    "https://twitter.com": "/first_twitter",
    "https://verycoolblog.com": "/nineties_blog"
}

// change the page according to the address
function change_page() {

    let address = $("#address-bar").val();
    console.log(address)
    if (address === "https://youtube.com"){
        clippy.load('Merlin', (agent) => {
                      // do anything with the loaded agent
                      agent.show();
                      agent.speak("Remember what we said before? Great events start with small steps? That's exactly what happened on YouTube. YouTube, which entered the internet environment by calling out from a zoo sincerely, is currently the most popular video and live streaming platform on the planet. We do not know what we would have done without YouTube; which functions as a movie theater, school, concert and game zone. Thank you YouTube for being so beneficial! To continue the trip, you can take another url from the notebook on the left by descending order, paste it in the address part of the browser, and press the Go button."
);
                      setTimeout(() =>{
                          agent.hide();
                      },23000)

                  });

    }else if (address === "https://google.com"){
        clippy.load('Merlin', (agent) => {
                      // do anything with the loaded agent
                      agent.show();
                      agent.speak( "Google, derived from the mathematical term Googol and created by two college students in the garage, literally changed the world, history, and people's lives. Changing the way we reach information, answers, questions, requests and people, this search engine has revolutionized every aspect of life. Thanks to Google, the world is now more integrated, people are more curious and wiser, and life is more interesting. Thank you Google! To continue the trip, you can take another url from the notebook on the left by descending order, paste it in the address part of the browser, and press the Go button."
);

                      setTimeout(() =>{
                          agent.hide();
                      },20000)

                  });

    }else if (address === "https://twitter.com"){
        clippy.load('Merlin', (agent) => {
                      // do anything with the loaded agent
                      agent.show();
                      agent.speak( "Jack was unaware that by setting up his 'twittr', he was building a site where he would make an unimaginable contribution to freedom of expression, thought sharing, polyphony and diversity. Thanks to Twitter, freedom of expression, polyphony, respect for differences and living in harmony have become possible and spread like never before. Thanks Twitter and Jack for supporting and spreading the freedoms! To continue the trip, you can take another url from the notebook on the left by descending order, paste it in the address part of the browser, and press the Go button."
);
                      setTimeout(() =>{
                          agent.hide();
                      },20000)

                  });

    }
    else if (address === "https://verycoolblog.com"){
        clippy.load('Merlin', (agent) => {
                      // do anything with the loaded agent
                      agent.show();
                      agent.speak( "In the '90s, when the Internet emerged and just started to spread, the most popular sites at first looked like this one. Personal blogs were in his place. Thanks to this democratic technology, everyone wanted to express themselves, share their thoughts and leave a mark in history. They did and are keep doing. To continue the trip, you can take another url from the notebook on the left by descending order, paste it in the address part of the browser, and press the Go button."
);
                      setTimeout(() =>{
                          agent.hide();
                      },20000)

                  });

    }    else if (address === "https://blog-area.com"){
        clippy.load('Merlin', (agent) => {
                      // do anything with the loaded agent
                      agent.show();
                      agent.speak( "And here we are, the end of the trip. But before we split our roads, let me say a few more words.This young technology, which is just 30 years old, has already changed our lives in ways we never imagined, and it continues to change. We hope that this short trip to the history of the Internet has been inspiring and informative for you. And we hope again that the Internet continues to be a democratic, revolutionary, magical and useful technology. To make sure the Internet will stay like this, don't just use these beautiful sites and the Internet, but also contribute. Create something and change the world, leave a mark. Do it so that when people will go on a nostalgic trip with a project like this in the future, they will be able to see your creation and contribution. Hokus pokus, abra kadabra! Let time flow forward and the magic of the Internet continues to spread! Keep staying online and magical!"
);

                      setTimeout(() =>{
                          agent.play("GestureUp");
                          agent.hide();
                      },35000)

                  });

    }
    if (address in url_mapping){
        // remove the 404 page if the 404 page is showing
        if (!document.getElementById("404-interface").classList.contains("d-none")){
            document.getElementById("404-interface").classList.add("d-none");
        }
        // fetch and render the page
        let django_address = fetch(url_mapping[address])
        django_address.then(r=>
            r.text()

        ).then(
            r => {

                document.getElementById("web-page").innerHTML = r
            }
        )
    } else {
        // clean up the current page
        document.getElementById("web-page").innerHTML = ""
        // show 404 page
        document.getElementById("404-interface").classList.remove("d-none");
    }
}

// App specific functions

// google search function
function googleSearch(){
    let search_text = $("#search-box").val()
    if (search_text.length === 0) {
        search_text = "google"
    }
    let search_results = fetch("/first_google/results/" + search_text)
    search_results.then(r=>
            r.text()
        ).then(
            r => {
                document.getElementById("web-page").innerHTML = r
            }
        )

}
