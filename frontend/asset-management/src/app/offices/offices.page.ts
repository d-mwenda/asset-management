import { OfficeInterface } from './../interfaces/office.interface';
import { OfficesService } from './../services/offices.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-offices',
  templateUrl: './offices.page.html',
  styleUrls: ['./offices.page.scss'],
})
export class OfficesPage implements OnInit {

  offices: OfficeInterface[];

  constructor(private officesService: OfficesService) { }

  ngOnInit() {
    this.showOffices();
  }

  showOffices(): void {
    this.officesService.getOffices().subscribe(
      offices => (this.offices = offices)
    );
  }

}
