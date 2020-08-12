import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AssetTypesPage } from './asset-types.page';

const routes: Routes = [
  {
    path: '',
    component: AssetTypesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AssetTypesPageRoutingModule {}
