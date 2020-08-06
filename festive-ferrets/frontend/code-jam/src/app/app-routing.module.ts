import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {MainSiteComponent} from './main-site/main-site.component';

const routes: Routes = [
  {path: 'main-page', component: MainSiteComponent},
  {path: '', redirectTo: 'main-page', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
