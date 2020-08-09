export default class User {
  constructor(details) {
    this.id = details.id;
    this.username = details.username;
    this.password = details.password;
    this.confirm_password = details.confirm_password;
    this.email = details.email;
    this.name = details.name;
    this.age = details.age;
    this.friends = details.friends;
    this.about = details.about;
    this.greeting = details.greeting;
    this.profile_picture = details.profilePicture;
    this.profile_comments = details.profileComments;
    this.latest_post = {title: null, content: null};
  }
}
