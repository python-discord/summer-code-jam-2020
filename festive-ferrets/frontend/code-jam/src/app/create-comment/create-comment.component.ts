import {Component, OnInit, Output, EventEmitter} from '@angular/core';
import {CommentService} from '../services/comment.service';
import {Comment} from '../interfaces/comment';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-create-comment',
  templateUrl: './create-comment.component.html',
  styleUrls: ['./create-comment.component.scss']
})
export class CreateCommentComponent implements OnInit {

  constructor(private commentService: CommentService,
              private route: ActivatedRoute) {
  }

  @Output() created = new EventEmitter();
  @Output() createComment = new EventEmitter();
  id: number;

  ngOnInit(): void {
    this.id = +this.route.snapshot.paramMap.get('postId');
  }

  publish(user, text) {
    this.createComment.emit({user: user, text: text});
    this.created.emit(false);
    let comment:Comment=new class implements Comment {
      commenter: string;
      id?: number;
      post: number;
      publication_date?: string;
      text: string;
    };
    comment.commenter=user;
    comment.text=text;
    comment.post=this.id;
    this.commentService.addComment(comment).subscribe();
  }
}
