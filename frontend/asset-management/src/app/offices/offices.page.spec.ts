import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { OfficesPage } from './offices.page';

describe('OfficesPage', () => {
  let component: OfficesPage;
  let fixture: ComponentFixture<OfficesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OfficesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(OfficesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
