import { Component, OnInit } from '@angular/core';

import { AssetTypesService } from './../services/asset-types.service';
import { AssetTypesInterface } from '../interfaces/asset-type.interface';

@Component({
  selector: 'app-asset-list',
  templateUrl: './asset-list.page.html',
  styleUrls: ['./asset-list.page.scss'],
})
export class AssetListPage implements OnInit {

  assetTypes: AssetTypesInterface[];

  constructor(private assetTypesService: AssetTypesService) { }

  ngOnInit() {
    this.showAssetTypes();
    console.log('Asset list component Running');
  }

  showAssetTypes(): void {
    this.assetTypesService.getAssetTypes()
    .subscribe(
      assetTypes => (this.assetTypes = assetTypes)
    );
  }
}
