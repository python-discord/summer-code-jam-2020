function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// // account 
// create user : createuser {username} {password} - create_User(username,password)
// login : login {username} {password} - login_User(username,password)
// logout : logout - logout_User()

// // character 
// - create character : createcha {name} - create_Character(name)
// - character list of now Login user - my-chracters - get_Character_list()
// character stats of now Login user -> timed polling 
//----- Update character stats of now Login user
// - Select Character : enter a room - startcha {name} - start_this_character(name)
// - GET charater list in same room(with my character) -> timed polling
// -  => chalist_in_my_room - get_user_list_in_same_room() 
// attack # mycharacter -> others 

