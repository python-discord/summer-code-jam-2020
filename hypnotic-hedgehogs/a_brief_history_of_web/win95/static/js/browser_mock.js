// url_mapping
let url_mapping = {
    "https://youtube.com": "/first_youtube",
    "https://google.com": "/first_google",
    "https://twitter.com": "/first_twitter",
    "https://blog-area.com": "/nineties_blog"
}

// change the page according to the address
function change_page() {
    let address = $("#address-bar").val();
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