import {Component, Input, OnInit, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-square',
  templateUrl: './square.component.html',
  styleUrls: ['./square.component.scss']
})
export class SquareComponent implements OnInit {

  constructor() {
  }

  @Input() value: string;
  @Input() winColor: boolean;
  @Output() click = new EventEmitter<string>();

  ngOnInit(): void {
  }

  handleClick() {
    this.click.emit();
  }

}
