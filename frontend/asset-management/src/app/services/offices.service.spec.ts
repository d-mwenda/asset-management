import { TestBed } from '@angular/core/testing';

import { OfficesService } from './offices.service';

describe('OfficesService', () => {
  let service: OfficesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OfficesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
