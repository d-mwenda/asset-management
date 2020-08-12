import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AssetMakeInterface } from '../interfaces/asset-make.interface';

@Injectable({
  providedIn: 'root'
})
export class AssetMakesService {

  assetMakesUrl = '/api/asset-register-management/asset-makes/';

  constructor(private http: HttpClient) { }

  getAssetMakes(): Observable<AssetMakeInterface[]> {
    return this.http.get<AssetMakeInterface[]>(this.assetMakesUrl);
  }
}
