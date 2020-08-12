import { AssetOwnersService } from './../services/asset-owners.service';
import { AssetOwnerInterface } from './../interfaces/asset-owners.interface';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-asset-owners',
  templateUrl: './asset-owners.page.html',
  styleUrls: ['./asset-owners.page.scss'],
})
export class AssetOwnersPage implements OnInit {

  assetOwners: AssetOwnerInterface[];

  constructor(private assetOwnersService: AssetOwnersService) { }

  ngOnInit() {
    this.getAssetOwners();
  }

  getAssetOwners() {
    this.assetOwnersService.getAssetOwners().subscribe(
      assetOwners => this.assetOwners = assetOwners
    );
  }

}
