import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TictactoeService {

  constructor(private http: HttpClient) {
  }

  url = 'http://127.0.0.1:8000/tictactoe';

  getPreview(): Observable<any> {
    return this.http.get<any>(`${this.url}/preview`);
  }

  startGame(): Observable<any> {
    return this.http.post<any>(`${this.url}/start-play`, {"turn": 1});
  }

  make_move(pos): Observable<any> {
    return this.http.post<any>(`${this.url}/make-move`, pos);
  }

}
