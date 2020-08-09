import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MainSiteComponent} from './main-site/main-site.component';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material/input';
import {MatGridListModule} from '@angular/material/grid-list';
import { HttpClientModule} from '@angular/common/http';
import { BoardViewComponent } from './board-view/board-view.component';
import {MatListModule} from '@angular/material/list';
import { PostViewComponent } from './post-view/post-view.component';
import { CreateCommentComponent } from './create-comment/create-comment.component';
import { CreatePostComponent } from './create-post/create-post.component';
import { BoardComponent } from './board/board.component';
import { SquareComponent } from './square/square.component';

@NgModule({
  declarations: [
    AppComponent,
    MainSiteComponent,
    BoardViewComponent,
    PostViewComponent,
    CreateCommentComponent,
    CreatePostComponent,
    BoardComponent,
    SquareComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatInputModule,
    MatGridListModule,
    HttpClientModule,
    MatListModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
