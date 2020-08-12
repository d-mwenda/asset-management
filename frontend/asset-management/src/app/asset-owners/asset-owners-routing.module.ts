import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AssetOwnersPage } from './asset-owners.page';

const routes: Routes = [
  {
    path: '',
    component: AssetOwnersPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AssetOwnersPageRoutingModule {}
