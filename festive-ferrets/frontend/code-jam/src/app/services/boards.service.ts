import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Board} from '../interfaces/board';


@Injectable({
  providedIn: 'root'
})
export class BoardsService {

  constructor(private http: HttpClient) {
  }

  getBoards(): Observable<Board[]> {
    return this.http.get<Board[]>('assets/mock_boards.json');
  }
}
