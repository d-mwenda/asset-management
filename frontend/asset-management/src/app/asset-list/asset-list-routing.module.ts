import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AssetListPage } from './asset-list.page';

const routes: Routes = [
  {
    path: '',
    component: AssetListPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AssetListPageRoutingModule {}
