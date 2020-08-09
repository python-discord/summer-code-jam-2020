export default class Post {
  constructor({id, content, title, author, likes, dislikes, image}) {
    this.id = id;
    this.image = image;
    this.title = title;
    this.content = content;
    this.author = author;
    this.likes = likes;
    this.dislikes = dislikes;
  }
}
