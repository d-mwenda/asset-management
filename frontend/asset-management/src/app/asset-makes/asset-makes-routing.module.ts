import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AssetMakesPage } from './asset-makes.page';

const routes: Routes = [
  {
    path: '',
    component: AssetMakesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AssetMakesPageRoutingModule {}
