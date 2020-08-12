import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AssetListPageRoutingModule } from './asset-list-routing.module';

import { AssetListPage } from './asset-list.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AssetListPageRoutingModule
  ],
  declarations: [AssetListPage]
})
export class AssetListPageModule {}
