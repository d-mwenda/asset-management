import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AssetModelsPageRoutingModule } from './asset-models-routing.module';

import { AssetModelsPage } from './asset-models.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AssetModelsPageRoutingModule
  ],
  declarations: [AssetModelsPage]
})
export class AssetModelsPageModule {}
