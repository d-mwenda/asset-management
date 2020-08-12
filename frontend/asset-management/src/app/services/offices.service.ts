import { OfficeInterface } from './../interfaces/office.interface';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class OfficesService {

  officesUrl = '/api/asset-register-management/offices/';

  constructor(private http: HttpClient) { }

  getOffices(): Observable<OfficeInterface[]> {
    return this.http.get<OfficeInterface[]>(this.officesUrl);
  }
}
