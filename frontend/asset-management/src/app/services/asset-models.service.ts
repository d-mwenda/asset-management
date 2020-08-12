import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { AssetModelInterface } from '../interfaces/asset-model.interface';


@Injectable({
  providedIn: 'root'
})
export class AssetModelsService {

  assetModelsUrl = '/api/asset-register-management/asset-models/';

  constructor(private http: HttpClient) { }

  getAssetModels(): Observable<AssetModelInterface[]> {
    return this.http.get<AssetModelInterface[]>(this.assetModelsUrl);
  }

}
