import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AssetOwnerInterface } from '../interfaces/asset-owners.interface';

@Injectable({
  providedIn: 'root'
})
export class AssetOwnersService {

  assetOwnersUrl = '/api/asset-register-management/asset-owners/';

  constructor(private http: HttpClient) { }

  getAssetOwners(): Observable<AssetOwnerInterface[]> {
    return this.http.get<AssetOwnerInterface[]>(this.assetOwnersUrl);
  }
}
