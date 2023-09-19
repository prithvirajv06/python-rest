import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OnemoreLoginComponent } from './onemore-login.component';

describe('OnemoreLoginComponent', () => {
  let component: OnemoreLoginComponent;
  let fixture: ComponentFixture<OnemoreLoginComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OnemoreLoginComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OnemoreLoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
