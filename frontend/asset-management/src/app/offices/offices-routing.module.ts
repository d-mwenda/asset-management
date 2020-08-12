import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { OfficesPage } from './offices.page';

const routes: Routes = [
  {
    path: '',
    component: OfficesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class OfficesPageRoutingModule {}
