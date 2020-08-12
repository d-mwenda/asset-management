import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AssetTypesPageRoutingModule } from './asset-types-routing.module';

import { AssetTypesPage } from './asset-types.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AssetTypesPageRoutingModule
  ],
  declarations: [AssetTypesPage]
})
export class AssetTypesPageModule {}
