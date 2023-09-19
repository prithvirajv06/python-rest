import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OnemoreRegisterComponent } from './onemore-register.component';

describe('OnemoreRegisterComponent', () => {
  let component: OnemoreRegisterComponent;
  let fixture: ComponentFixture<OnemoreRegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OnemoreRegisterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OnemoreRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
