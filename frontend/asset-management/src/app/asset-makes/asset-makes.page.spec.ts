import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { AssetMakesPage } from './asset-makes.page';

describe('AssetMakesPage', () => {
  let component: AssetMakesPage;
  let fixture: ComponentFixture<AssetMakesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AssetMakesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(AssetMakesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
