import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {MainSiteComponent} from './main-site/main-site.component';
import {BoardViewComponent} from './board-view/board-view.component';
import {PostViewComponent} from './post-view/post-view.component';
import {CreatePostComponent} from './create-post/create-post.component';
import {BoardComponent} from './board/board.component';

const routes: Routes = [
  {path: 'main-page', component: MainSiteComponent},
  {path: '', redirectTo: 'main-page', pathMatch: 'full'},
  {path: 'main-page/:boardId', component: BoardViewComponent},
  {path: 'main-page/:boardId/create-post', component: CreatePostComponent},
  {path: 'main-page/:boardId/:postId', component: PostViewComponent},
  {path: 'tic-tac-toe', component: BoardComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
