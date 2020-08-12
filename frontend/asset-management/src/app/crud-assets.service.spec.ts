import { TestBed } from '@angular/core/testing';

import { CrudAssetsService } from './crud-assets.service';

describe('CrudAssetsService', () => {
  let service: CrudAssetsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CrudAssetsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
