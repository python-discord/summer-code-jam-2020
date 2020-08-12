import {Component, OnInit} from '@angular/core';
import {BoardsService} from '../services/boards.service';
import {Board} from '../interfaces/board';

@Component({
  selector: 'app-main-site',
  templateUrl: './main-site.component.html',
  styleUrls: ['./main-site.component.scss']
})
export class MainSiteComponent implements OnInit {

  constructor(private boardsService: BoardsService) {
  }

  boards: Board[] = [];

  ngOnInit(): void {
    this.boardsService.getBoards().subscribe(x => this.boards = x.results);
  }


}
