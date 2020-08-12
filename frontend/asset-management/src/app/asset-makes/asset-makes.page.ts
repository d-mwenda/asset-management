import { Component, OnInit } from '@angular/core';

import { AssetMakeInterface } from '../interfaces/asset-make.interface';
import { AssetMakesService } from '../services/asset-makes.service';

@Component({
  selector: 'app-asset-makes',
  templateUrl: './asset-makes.page.html',
  styleUrls: ['./asset-makes.page.scss'],
})
export class AssetMakesPage implements OnInit {

  assetMakes: AssetMakeInterface[];

  constructor(private assetMakesService: AssetMakesService) { }

  ngOnInit() {
    this.showAssetMakes();
  }

  showAssetMakes(): void {
    this.assetMakesService.getAssetMakes()
    .subscribe(
      assetMakes => (this.assetMakes = assetMakes)
    );
  }

}
