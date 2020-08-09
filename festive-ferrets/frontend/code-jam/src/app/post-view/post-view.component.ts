import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {PostsService} from '../services/posts.service';
import {Post} from '../interfaces/post';
import {Comment} from '../interfaces/comment'

@Component({
  selector: 'app-post-view',
  templateUrl: './post-view.component.html',
  styleUrls: ['./post-view.component.scss']
})
export class PostViewComponent implements OnInit {

  constructor(private route: ActivatedRoute,
              private postService: PostsService) {
  }

  addComent:Boolean=false;
  comments: Comment[];
  credentials:any;
  post: Post = new class implements Post {
    board: number;
    id: number;
    poster: string;
    publication_date: string;
    text: string;
    title: string;
  };
  id:number;
  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('postId');
    this.postService.getCommentsForPost(this.id).subscribe(x =>{
      this.comments=x.results;
    });
    this.postService.getPost(this.id).subscribe(x => this.post = x);
  }


  get_cred($event:any){
    this.credentials=$event;
    this.postService.getCommentsForPost(this.id).subscribe(x =>{
      this.comments=x.results;
    });
  }
  check_coment($event:any){
    this.addComent=$event;
  }

}
