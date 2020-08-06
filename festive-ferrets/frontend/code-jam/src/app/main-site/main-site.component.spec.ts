import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainSiteComponent } from './main-site.component';

describe('MainSiteComponent', () => {
  let component: MainSiteComponent;
  let fixture: ComponentFixture<MainSiteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainSiteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainSiteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
