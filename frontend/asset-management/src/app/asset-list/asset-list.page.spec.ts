import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { AssetListPage } from './asset-list.page';

describe('AssetListPage', () => {
  let component: AssetListPage;
  let fixture: ComponentFixture<AssetListPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AssetListPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(AssetListPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
