// url_mapping
let url_mapping = {
    "https://youtube.com": "/first_youtube",
    "https://google.com": "/first_google",
    "https://twitter.com": "/first_twitter",
    "https://blog-area.com": "/nintys_blog"
}

// change the page according to the address
function change_page() {
    let address = $("#address-bar").val();
    if (address in url_mapping){
        let django_address = fetch(url_mapping[address])
        django_address.then(r=>
            r.text()
        ).then(
            r => {
                document.getElementById("web-page").innerHTML = r
            }
        )
    } else {
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