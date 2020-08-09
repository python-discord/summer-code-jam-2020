import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {BoardsContext} from '../interfaces/boards-context';
import {Board} from '../interfaces/board';


@Injectable({
  providedIn: 'root'
})
export class BoardsService {

  constructor(private http: HttpClient) {
  }



  private appUrl='http://127.0.0.1:80/nchan/boards/';

  getBoards(): Observable<BoardsContext> {
    return this.http.get<BoardsContext>(`${this.appUrl}?format=json`);
  }


  getBoard(id): Observable<Board> {
    return this.http.get<Board>(`${this.appUrl}${id}?format=json`);
  }
}
