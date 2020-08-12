import { TestBed } from '@angular/core/testing';

import { AssetModelsService } from './asset-models.service';

describe('AssetModelsService', () => {
  let service: AssetModelsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AssetModelsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
