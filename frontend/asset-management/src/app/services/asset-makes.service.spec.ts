import { TestBed } from '@angular/core/testing';

import { AssetMakesService } from './asset-makes.service';

describe('AssetMakesService', () => {
  let service: AssetMakesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AssetMakesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
