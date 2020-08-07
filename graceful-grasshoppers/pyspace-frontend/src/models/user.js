export default class User {
  constructor(details) {
    this.id = details.id;
    this.username = details.username;
    this.password = details.password;
    this.email = details.email;
    this.name = details.name;
    this.age = details.age;
    this.friends = details.friends;
    this.about = details.about;
    this.greeting = details.greeting;
    this.picture = details.profilePicture;
    this.profileComments = details.profileComments;
    this.latest_post = {title: null, content: null};
  }
}
