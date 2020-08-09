import {Component, OnInit} from '@angular/core';
import {TictactoeService} from '../services/tictactoe.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {

  constructor(private tictactoeService: TictactoeService) {
  }

  fields: string[] = [];
  preview: JSON;
  done: boolean = false;
  winner: string = '';

  ngOnInit(): void {
    this.tictactoeService.startGame().subscribe();
    this.tictactoeService.getPreview().subscribe(x => {
      for (let val in x) {
        this.fields.push(x[val]);
      }
    });
  }

  onClickSquare(pos: string, id: number) {
    this.tictactoeService.make_move({'x': +pos[0], 'y': +pos[1]}).subscribe(x => {
      if (x['winner'] != null) {
        this.winner = x['winner'];
      }
    });
    this.fields = [];
    this.tictactoeService.getPreview().subscribe(x => {
      for (let val in x) {
        this.fields.push(x[val]);
      }
    });
  }

  resetGame() {
    this.fields = [];
    this.tictactoeService.startGame().subscribe();
    this.tictactoeService.getPreview().subscribe(x => {
      for (let val in x) {
        this.fields.push(x[val]);
      }
    });
  }


}
