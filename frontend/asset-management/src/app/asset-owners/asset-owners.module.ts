import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AssetOwnersPageRoutingModule } from './asset-owners-routing.module';

import { AssetOwnersPage } from './asset-owners.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AssetOwnersPageRoutingModule
  ],
  declarations: [AssetOwnersPage]
})
export class AssetOwnersPageModule {}
