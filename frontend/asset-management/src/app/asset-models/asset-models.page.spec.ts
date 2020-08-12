import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { AssetModelsPage } from './asset-models.page';

describe('AssetModelsPage', () => {
  let component: AssetModelsPage;
  let fixture: ComponentFixture<AssetModelsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AssetModelsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(AssetModelsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
