import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AssetMakesPageRoutingModule } from './asset-makes-routing.module';

import { AssetMakesPage } from './asset-makes.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AssetMakesPageRoutingModule
  ],
  declarations: [AssetMakesPage]
})
export class AssetMakesPageModule {}
