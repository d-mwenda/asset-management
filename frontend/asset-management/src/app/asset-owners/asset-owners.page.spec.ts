import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { AssetOwnersPage } from './asset-owners.page';

describe('AssetOwnersPage', () => {
  let component: AssetOwnersPage;
  let fixture: ComponentFixture<AssetOwnersPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AssetOwnersPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(AssetOwnersPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
