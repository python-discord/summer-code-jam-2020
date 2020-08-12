/* Project specific Javascript goes here. */

logoutUrl = "/accounts/logout/";
changePwd = "/accounts/password/change/"


function changeToIfNotEqual(url) {
    if ( window.location.href.endsWith(url)) {
         alert("Already on that page!");

    } else {
       window.location.href = url;
    }
}

function goBack() {
  window.history.back();
}
