import { Component, OnInit } from '@angular/core';
import { AssetTypeInterface } from '../interfaces/asset-type.interface';
import { AssetTypesService } from '../services/asset-types.service';

@Component({
  selector: 'app-asset-types',
  templateUrl: './asset-types.page.html',
  styleUrls: ['./asset-types.page.scss'],
})
export class AssetTypesPage implements OnInit {

  assetTypes: AssetTypeInterface[];

  constructor(private assetTypesService: AssetTypesService) { }

  ngOnInit() {
    this.showAssetTypes();
  }

  showAssetTypes(): void {
    this.assetTypesService.getAssetTypes()
    .subscribe(
      assetTypes => (this.assetTypes = assetTypes)
    );
  }
}
