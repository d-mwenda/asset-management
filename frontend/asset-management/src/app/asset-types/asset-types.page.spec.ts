import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { AssetTypesPage } from './asset-types.page';

describe('AssetTypesPage', () => {
  let component: AssetTypesPage;
  let fixture: ComponentFixture<AssetTypesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AssetTypesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(AssetTypesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
