import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {MainSiteComponent} from './main-site/main-site.component';
import {BoardViewComponent} from "./board-view/board-view.component";

const routes: Routes = [
  {path: 'main-page', component: MainSiteComponent},
  {path: '', redirectTo: 'main-page', pathMatch: 'full'},
  {path: 'main-page/:name' , component:BoardViewComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
