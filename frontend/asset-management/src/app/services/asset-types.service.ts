import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { rootUrl } from './server-urls';
import { AssetTypeInterface } from './../interfaces/asset-type.interface';


@Injectable({
  providedIn: 'root'
})
export class AssetTypesService {

  assetTypesUrl = '/api/asset-register-management/asset-types/';

  constructor(private http: HttpClient) { }

getAssetTypes(): Observable<AssetTypeInterface[]> {
    return this.http.get<AssetTypeInterface[]> (this.assetTypesUrl);
  }
}
