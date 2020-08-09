import {Component, OnInit} from '@angular/core';
import {PostsService} from '../services/posts.service';
import {Post} from '../interfaces/post';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-create-post',
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.scss']
})
export class CreatePostComponent implements OnInit {

  constructor(private postService: PostsService,
              private route: ActivatedRoute,
             private loc:Location) {
  }

  id:number;
  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('boardId');
  }

  createPost(title, username, content) {
    let x: Post = new class implements Post {
      board: number;
      id?: number;
      poster: string;
      publication_date?: string;
      text: string;
      title: string;
    };
    x.title = title;
    x.poster = username;
    x.text = content;
    x.board = this.id;

    this.postService.addPost(x).subscribe();
    this.loc.back();
  }
}
