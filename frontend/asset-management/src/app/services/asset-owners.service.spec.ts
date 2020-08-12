import { TestBed } from '@angular/core/testing';

import { AssetOwnersService } from './asset-owners.service';

describe('AssetOwnersService', () => {
  let service: AssetOwnersService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AssetOwnersService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
