import {Component, OnInit} from '@angular/core';
import {PostsService} from '../services/posts.service';
import {Post} from '../interfaces/post';
import {ActivatedRoute} from '@angular/router';
import {Board} from '../interfaces/board';
import {BoardsService} from '../services/boards.service';

@Component({
  selector: 'app-board-view',
  templateUrl: './board-view.component.html',
  styleUrls: ['./board-view.component.scss']
})
export class BoardViewComponent implements OnInit {

  constructor(private postService: PostsService,
              private route: ActivatedRoute,
              private boardsService:BoardsService) {
  }

  posts: Post[];
  board:Board=new Board();

  ngOnInit(): void {
    const id = +this.route.snapshot.paramMap.get('boardId');
    this.postService.getPostsForBoard(id).subscribe(x =>{
      this.posts=x.results;
    });
    this.boardsService.getBoard(id).subscribe(x=>this.board=x)
  }


}
