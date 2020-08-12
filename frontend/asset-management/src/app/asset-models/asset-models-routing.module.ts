import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AssetModelsPage } from './asset-models.page';

const routes: Routes = [
  {
    path: '',
    component: AssetModelsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AssetModelsPageRoutingModule {}
