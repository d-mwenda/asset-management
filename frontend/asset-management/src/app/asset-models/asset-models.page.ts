import { AssetModelsService } from './../services/asset-models.service';
import { Component, OnInit } from '@angular/core';

import { AssetModelInterface } from './../interfaces/asset-model.interface';

@Component({
  selector: 'app-asset-models',
  templateUrl: './asset-models.page.html',
  styleUrls: ['./asset-models.page.scss'],
})
export class AssetModelsPage implements OnInit {

  assetModels: AssetModelInterface[];

  constructor(private assetModelsService: AssetModelsService) { }

  ngOnInit() {
    this.showAssetModels();
  }

  showAssetModels(): void {
    this.assetModelsService.getAssetModels().subscribe(
      assetModels => (this.assetModels = assetModels)
    );
  }

}
