import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { OfficesPageRoutingModule } from './offices-routing.module';

import { OfficesPage } from './offices.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    OfficesPageRoutingModule
  ],
  declarations: [OfficesPage]
})
export class OfficesPageModule {}
